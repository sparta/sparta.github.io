#!/usr/bin/env python3
"""Compare the Sphinx web site against the txt2html web site, page by page.

The Sphinx migration must not change what the manual says.  This extracts
the things a reader depends on -- the words, where the links go, and what
anchors exist for other pages to link to -- from both builds and diffs
them.  Presentation differs by design and is ignored: tag soup, CSS
classes, and the navigation chrome Sphinx adds around every page.

Usage:
    parity-check.py OLD_HTML_DIR NEW_HTML_DIR [--verbose] [--page NAME]
                    [--no-allow-equations]

Exits non-zero if any page differs outside the agreed deltas, which are
DELTAS for the ones that recur and DECLARED for the individual fixes.

OLD_HTML_DIR has to be a complete doc/ tree -- the pages *and* the Eqs and
JPG directories beside them -- because the check also verifies that a link
which resolved in the old manual still resolves in the new one.  Generate
it by running txt2html over the .txt sources of the commit being compared
against, rather than reusing the .html committed next to them: two of those
had drifted from their own sources by the time of the migration, and a
baseline regenerated from the branch's own edited sources proves nothing.
"""
import argparse
import collections
import html
import pathlib
import posixpath
import re
import sys
import unicodedata
import urllib.parse

# Intentional differences, agreed before the migration.  Anything not
# covered here is a regression and fails the check.
DELTAS = {
    'mailto_cloaked': (
        'Sphinx publishes a mailto address entity-encoded, as spam '
        'protection, so "mailto:a@b.com" is served as '
        '"mailto:a&#37;&#52;&#48;b&#46;com".  The link is the same one and '
        'works the same way; the comparison decodes it before matching.'
    ),
    'markup_typos_fixed': (
        'Markup typos in the txt2html sources that made a page render '
        'wrongly, fixed in the reST.  Each is listed individually in '
        'DECLARED below with the source line it came from, so the diff it '
        'produces is reviewed rather than waved through.'
    ),
}

# Differences that are individually agreed, page by page and run by run.
#
# A heuristic cannot tell an intended fix from a regression, so the fixes
# this conversion makes are written out: the exact words the old page
# showed, the exact words the new one shows, and why.  Anything else is a
# regression.  Each entry is (old run, new run, delta key, reason).
DECLARED = {
    # One typo, two visible consequences.  features.txt:60 opened a link
    # with ":triangulated" where it meant a quote, so txt2html could not
    # pair the quotes: it ran the two links together into
    #   <A HREF = "doc/read_grid.html<A HREF = "...#intro_3">>read from file</A>
    # which leaks a ">" in front of "read from file" and leaves the ":"
    # in front of "triangulated".  The source is fixed, so both are gone.
    #
    # Declared as the two single-word runs the diff actually produces.  As
    # one four-word run it matched nothing and this page failed the check.
    'features.html': [
        ('>read', 'read', 'markup_typos_fixed',
         'the ">" txt2html leaked out of the unterminated <A HREF>'),
        (':triangulated', 'triangulated', 'markup_typos_fixed',
         'the ":" that should have been the link\'s opening quote'),
    ],
}

# Link targets that this branch deliberately moved, as a per-page map of
# the target the published page used to the target it uses now.  A "None"
# replacement means the link now points off-site and so leaves the
# internal set entirely.
#
# Anything not named here still fails, in both directions: a link that
# moves without a declaration, and a declared one that does not move.
RETARGETED = {
    'bench.html': {
        'doc/accelerate_kokkos.html': (
            'doc/Section_accelerate.html#acc_3',
            'the KOKKOS package has its own page no longer; it is section '
            '5.3 of Section_accelerate'),
    },
    'bug.html': {
        # commands renamed or absorbed since the release note was written
        'doc/accelerate_kokkos.html': (
            'doc/Section_accelerate.html#acc_3', 'as above'),
        'doc/compute_distsurf.html': (
            'doc/compute_distsurf_grid.html',
            'the compute is distsurf/grid, and the note calls it that'),
        'doc/dump_grid.html': (
            'doc/dump.html', 'dump grid is a style of the dump command'),
        'doc/fix_adapt_grid.html': (
            'doc/fix_adapt.html', 'fix adapt/grid is now fix adapt'),
        'doc/fix_emit.html': (
            'doc/fix_emit_face.html',
            'both notes are about the face variants -- one names the '
            'subsonic keyword, the other says "fix emit face commands"'),
        'doc/fix_inflow.html': (
            'doc/fix_emit_face.html', 'fix inflow became fix emit/face'),
        'doc/fix_inflow_file.html': (
            'doc/fix_emit_face_file.html',
            'fix inflow/file became fix emit/face/file'),
        # typos in the target itself
        'doc/write_suf.html': (
            'doc/write_surf.html', 'the link text says write_surf'),
        'doc/collide/html': (
            'doc/collide.html', 'a slash where the dot belonged'),
        'doc/create_particles': (
            'doc/create_particles.html', 'no extension'),
        'doc/Section_tools.html#stlsurf': (
            'doc/Section_tools.html#stl2surf',
            'the anchor Section_tools defines is stl2surf'),
        # manual pages linked without the doc/ prefix, so they resolved
        # against the site root and 404ed
        'global.html': ('doc/global.html', 'missing doc/ prefix'),
        'stats_style.html': ('doc/stats_style.html', 'missing doc/ prefix'),
        'fix_ave_time.html': ('doc/fix_ave_time.html', 'missing doc/ prefix'),
        'compute_distsurf_grid.html': (
            'doc/compute_distsurf_grid.html', 'missing doc/ prefix'),
        'fix_emit_face_file.html': (
            'doc/fix_emit_face_file.html', 'missing doc/ prefix'),
    },
    'features.html': {
        'doc/fix_inflow.html': (
            'doc/fix_emit_face.html', 'fix inflow became fix emit/face'),
        'doc/read_grid.html<A HREF =': (
            'doc/read_grid.html',
            'the unterminated <A HREF> from the features.txt:60 typo'),
    },
    'other.html': {
        'pizza': (
            None,
            'the page used the "pizza" alias without defining it, so '
            'txt2html published the word itself as the href; the alias is '
            'now defined as index.txt and features.txt define it'),
        '../download.html': (
            None,
            'the path was written relative to the Pizza.py site, not this '
            'one, so it climbed above the site root; it now points at the '
            'Pizza.py page the same sentence already links'),
    },
}

# External URLs this branch deliberately retargeted, listed per page as
# the URL the published page linked.  External links are compared on
# losses only (see below), so naming the old URL is what clears it; any
# other external link that stops being made still fails.
#
# Every replacement was fetched before being written, and only ones that
# answered 200 were used.  The two that matter beyond tidiness:
#
#   gnu.org retired /copyleft/ and redirects it to gpl-3.0.html, so the
#   site's "GPL" link was landing readers on version 3.  SPARTA's LICENSE
#   is "GNU GENERAL PUBLIC LICENSE, Version 2, June 1991" -- as is
#   LAMMPS's -- so it now points at gpl-2.0.html.
#
#   "this page"_../download.html climbed above the site root.  It was
#   written when the site lived under sjplimp.github.io/sparta/, where it
#   meant sjplimp.github.io/download.html -- which is still there, still
#   lists Pizza.py and still serves tars/pizza.tar.gz.
#
# gnu.org is left on http: its https reset the connection from here, so
# an https URL could not be verified and was not guessed at.
EXTERNAL_RETARGETED = {
    'authors.html': {'http://www.doe.gov'},
    'bug.html': {'http://www.paraview.org'},
    'features.html': {'http://www.python.org'},
    'index.html': {'http://sourceforge.net/projects/sparta',
                   'http://www.doe.gov',
                   'http://www.gnu.org/copyleft/gpl.html',
                   'http://www.gnu.org/licenses/lgpl-2.1.html',
                   'http://www.paraview.org',
                   'http://www.sandia.gov'},
    'open_source.html': {'http://www.gnu.org/copyleft/gpl.html',
                         'http://www.gnu.org/licenses/lgpl-2.1.html',
                         'http://www.opensource.org'},
    'other.html': {'http://en.wikipedia.org/wiki/Direct_simulation_Monte_Carlo',
                   'http://mt.seas.upenn.edu/Archive/Graphics/A',
                   'http://www.paraview.org',
                   'http://www.python.org',
                   'http://www.tecplot.com'},
    'pictures.html': {'http://www.paraview.org',
                      'http://www.tecplot.com'},
}


# Links the published page could not make at all, restored by a fix
# declared above.  Exact, and only on pages that have a declaration.
RESTORED = {
    'features.html': {
        'doc/Section_intro.html#intro_3':
            'the second of the two links the unterminated <A HREF> ran '
            'together into one unusable target',
    },
}

# What MathJax leaves in the static HTML: the LaTeX between \\[..\\] for a
# displayed equation and \\(..\\) for an inline one.
MATHJAX_SPAN = re.compile(r'\\\[.*?\\\]|\\\(.*?\\\)', re.S)

# The two equation images that were tables of surface reactions, keyed by
# page and the start of the text that replaced them.  They are the only
# sites where something other than maths may stand where an image stood;
# what they say is checked by equation-check.py.
EQ_TABLES = {
    ('surf_react_adsorb.html', 'Symbol Reaction type Examples AA Associative'),
    ('surf_react_adsorb.html', 'Symbol Reaction type Examples DS Desorption'),
}

# Where an equation image stood in the old page.  Marking the site lets the
# equation allowance be scoped to the text that replaced that image, rather
# than to any smallish difference on a page that happens to contain one.
EQ_MARK = '\x01EQIMG\x01'
EQ_IMG = re.compile(r'<img\b[^>]*?src\s*=\s*"(?:\./)?Eqs/[^"]+"[^>]*>', re.I)

# Sphinx wraps every page in navigation the old manual did not have.
CHROME = re.compile(
    r'<(nav|header|footer)\b.*?</\1>'
    r'|<div[^>]+role="navigation".*?</div>'
    r'|<div[^>]+class="[^"]*\b(sphinxsidebar|related|footer|headerlink)\b[^"]*".*?</div>',
    re.S | re.I)

# Every txt2html page opens with a navigation line -- command pages carry
# "SPARTA WWW Site - Documentation - Commands", chapter pages add Previous
# and Next Section links around it.  Sphinx replaces both with its own
# navigation, so neither is content.
# bounded so it cannot swallow a later <CENTER> block (the pages use them
# for figures too)
# The manual's checker strips the "SPARTA WWW Site" banner as chrome,
# because Sphinx replaces it there with its own navigation.  On the site it
# is content: a link home at the top of every page, and the only navigation
# these pages have.  It is kept, on both sides, so it is compared.
OLD_BANNER = re.compile(r'(?!x)x')

# Tags that separate one run of text from the next.  Everything else is
# inline and must not introduce a space: Pygments wraps each token of a
# literal block in its own <span>, so replacing inline tags with a space
# would split "/path/to/x" into "/ path / to / x".
BLOCK = re.compile(
    r'</(p|div|h[1-6]|li|tr|td|th|pre|ul|ol|dl|dd|dt|table|blockquote)>'
    r'|<(br|hr)\b[^>]*>', re.I)
TAG = re.compile(r'<[^>]+>')
SCRIPT = re.compile(r'<(script|style)\b.*?</\1>', re.S | re.I)


HEAD = re.compile(r'<head\b.*?</head>', re.S | re.I)
# the theme appends a permalink anchor to every heading
HEADERLINK = re.compile(r'<a\b[^>]*class="[^"]*headerlink[^"]*"[^>]*>.*?</a>',
                        re.S | re.I)


def content_only(markup):
    """Strip everything that is page furniture rather than content.

    Both banner styles are removed from both inputs, so every comparison
    built on this is symmetric: a build compared against itself always
    reports parity.
    """
    # <head> is the browser tab title and document metadata, not content
    t = HEAD.sub(' ', markup)
    t = HEADERLINK.sub(' ', t)
    t = SCRIPT.sub(' ', t)
    t = OLD_BANNER.sub(' ', t)
    return CHROME.sub(' ', t)


def eq_image_names(markup):
    """Basenames of the equation images the old page embedded."""
    return {posixpath.basename(m) for m in
            re.findall(r'<img\b[^>]*?src\s*=\s*"(?:\./)?(Eqs/[^"]+)"',
                       markup, re.I)}


def visible_text(markup):
    """The words a reader sees, normalized so formatting cannot matter."""
    t = content_only(markup)
    # An equation image shows text but contributes no words, so leave a
    # marker where it stood; without one the words that replaced it look
    # like an insertion at an arbitrary point in the page.
    t = EQ_IMG.sub(' ' + EQ_MARK + ' ', t)
    # keep block boundaries as separators so words do not run together
    t = BLOCK.sub('\n', t)
    t = TAG.sub('', t)
    t = html.unescape(t)
    t = unicodedata.normalize('NFKC', t)
    # Icon glyphs live in the Unicode private use area; the theme uses one
    # for the permalink marker.  They are decoration, not words.
    t = ''.join(' ' if '\ue000' <= c <= '\uf8ff' else c for c in t)
    t = t.replace('¶', ' ')
    return [w for w in t.split() if w]


def links(markup):
    """Where each link points, ignoring the text it is attached to.

    The banner and breadcrumb links are page furniture: every old page
    carries a fixed "SPARTA WWW Site - Documentation - Commands" header and
    Sphinx replaces it with its own navigation.  Those are excluded, so what
    is compared is the links the page's own content makes.
    """
    out = []
    for m in re.finditer(r'<a\b[^>]*?href\s*=\s*"([^"]*)"', content_only(markup), re.I):
        href = html.unescape(m.group(1)).strip()
        # Sphinx writes a mailto address entity-encoded, as spam
        # protection: "mailto:a@b.com" is published as
        # "mailto:a&#37;&#52;&#48;b&#46;com".  Unescaping the entities
        # leaves the percent-encoding, so undo that too -- the address is
        # the same one, and the link works either way.
        if href.lower().startswith('mailto:'):
            href = 'mailto:' + urllib.parse.unquote(href[7:])
        if not href or href.startswith('javascript:'):
            continue
        if href == '#':
            # a link to the top of the page it is on; txt2html spelled the
            # same thing as "thispage.html"
            out.append('#')
            continue
        if href.startswith('#'):
            continue
        out.append(href)
    return out


def anchors(markup):
    """Anchor names other pages can link to.

    Only attributes inside a tag count.  The manual's own prose contains
    things like 'the default mixture has an ID = "all"', which is text, not
    an anchor, so the search is scoped to tags rather than run over the
    whole file.
    """
    out = set()
    # <a name="..."> is the txt2html anchor form; id="..." on any element is
    # the Sphinx one.  name= on other elements is not an anchor -- <meta
    # name="author"> is document metadata, not a link target.
    for m in re.finditer(r'<a\b[^>]*?\bname\s*=\s*"([^"]+)"', markup, re.I):
        out.add(m.group(1))
    for tag in re.finditer(r'<[a-zA-Z][^>]*>', markup):
        for m in re.finditer(r'\bid\s*=\s*"([^"]+)"', tag.group(0), re.I):
            out.add(m.group(1))
    return out



def hidden_by_unescaped_lt(raw, old_run, new_run):
    """Is this one difference text a browser could not show?

    True only if the new words contain the "<" that caused the swallowing
    *and* are present verbatim in the old file's raw markup.  That second
    check is what makes it safe: it proves the text was published and
    hidden, rather than being new text.
    """
    if not new_run or not any('<' in w for w in new_run):
        return False
    # Where the hidden span ends mid-paragraph the browser joins the word
    # before it to the word after -- "x" + "These" becomes the one token
    # "xThese" -- so the run picks up trailing words that belong to the
    # visible text.  Trim them, but only if what is trimmed is really the
    # tail of that merged token.
    k = len(new_run)
    while k > 0 and ' '.join(new_run[:k]) not in raw:
        k -= 1
    if k == 0 or not any('<' in w for w in new_run[:k]):
        return False
    tail = ''.join(new_run[k:])
    return not tail or ''.join(old_run).endswith(tail)


def classify(name, raw, old_run, new_run, allow_equations):
    """Name the agreed delta this one difference falls under, or None.

    Every difference is judged on its own.  That cuts both ways and both
    ways matter: one unexplained difference no longer discards the
    verification of the others on the page, and an explained one no longer
    covers for an unexplained one somewhere else.
    """
    o, n = ' '.join(old_run), ' '.join(new_run)
    for d_old, d_new, key, _why in DECLARED.get(name, ()):
        if o == d_old and n == d_new:
            return key
    # Scoped to the marker: the words have to be what replaced that image,
    # not merely a difference somewhere on a page that has one.  And what
    # replaced it has to be maths: without that, a paragraph inserted next
    # to an equation lands in the same difference and is waved through with
    # it.  Once the maths is removed nothing may be left over -- except on
    # the two sites where the image was a table of reactions rather than an
    # equation, which equation-check.py compares row by row.
    if allow_equations and old_run and all(w == EQ_MARK for w in old_run):
        if (any(name == p_ and n.startswith(s) for p_, s in EQ_TABLES)
                or MATHJAX_SPAN.sub('', n).strip() == ''):
            return 'equations'
        return None
    if hidden_by_unescaped_lt(raw, old_run, new_run):
        return 'unescaped_lt'
    return None


def compare_text(name, old_markup, old_words, new_words, allow_equations):
    """Classify every difference between two pages.

    Returns (Counter of agreed deltas, list of unexplained differences).
    """
    import difflib
    raw = ' '.join(html.unescape(old_markup).split())
    agreed = collections.Counter()
    unexplained = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
            a=old_words, b=new_words, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        old_run, new_run = old_words[i1:i2], new_words[j1:j2]
        key = classify(name, raw, old_run, new_run, allow_equations)
        if key:
            agreed[key] += 1
        else:
            unexplained.append({
                'tag': tag,
                'old': ' '.join(old_words[max(0, i1 - 6):i2 + 6]),
                'new': ' '.join(new_words[max(0, j1 - 6):j2 + 6]),
                'n_old': i2 - i1,
                'n_new': j2 - j1,
            })
    return agreed, unexplained


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('old')
    ap.add_argument('new')
    ap.add_argument('--verbose', '-v', action='store_true')
    ap.add_argument('--page', help='check only this page')
    ap.add_argument('--no-allow-equations', dest='allow_equations',
                    action='store_false',
                    help='treat the MathJax equations as regressions too')
    args = ap.parse_args()

    old_dir, new_dir = pathlib.Path(args.old), pathlib.Path(args.new)
    pages = sorted(p.name for p in old_dir.glob('*.html'))
    if args.page:
        pages = [p for p in pages if p == args.page or p == args.page + '.html']

    missing, text_bad, link_bad, anchor_bad, ok = [], [], [], [], 0
    figure_bad = []
    dangling = []
    all_new_anchors = {}
    agreed_total = collections.Counter()
    agreed_pages = collections.Counter()

    for name in pages:
        new_path = new_dir / name
        if not new_path.exists():
            missing.append(name)
            continue
        o = (old_dir / name).read_text(errors='replace')
        n = new_path.read_text(errors='replace')

        ow, nw = visible_text(o), visible_text(n)

        page_ok = True
        agreed = collections.Counter()
        if ow != nw:
            agreed, unexplained = compare_text(
                name, o, ow, nw, args.allow_equations)
            agreed_total.update(agreed)
            for key in agreed:
                agreed_pages[key] += 1
            if args.verbose and agreed:
                detail = ', '.join(f'{n_} {k}' for k, n_ in sorted(agreed.items()))
                print(f'  ~ {name}: {detail} (agreed)')
            if unexplained:
                text_bad.append((name, unexplained))
                page_ok = False

        # Compare intra-manual targets as a multiset, so replacing one of
        # several links to the same page is still caught, and report added
        # targets as well as lost ones -- a link retargeted to a page that
        # happens to exist elsewhere on the page is still a regression.
        internal = lambda L: collections.Counter(
            x for x in L if not x.startswith(('http', 'mailto')))
        oc, nc = internal(links(o)), internal(links(n))

        # External links were left out of the comparison entirely, so a link
        # retargeted from gnu.org to somewhere else went unreported.  They
        # are compared on losses only: the manual gains external links --
        # the unescaped "<" hid some, and two markup typos printed their URL
        # as text -- and the two generators draw the line between banner and
        # body differently, so a gained URL is not evidence of anything.  A
        # URL that stopped being linked always is, and a retargeted link
        # shows up as the old one lost.
        external = lambda L: collections.Counter(
            x for x in L if x.startswith(('http', 'mailto', 'ftp')))
        e_lost = external(links(o)) - external(links(n))
        n_ext = sum(e_lost.pop(url, 0)
                    for url in EXTERNAL_RETARGETED.get(name, ()))
        if n_ext:
            agreed_total['external_retargeted'] += n_ext
            agreed_pages['external_retargeted'] += 1
        # Losses alone cannot police these.  A declared fix that gets
        # reverted puts the old URL back, which loses nothing and so
        # looks exactly like the published page.  So the new build is
        # also required not to link the URL that was declared away.
        e_new = external(links(n))
        still = sorted(u for u in EXTERNAL_RETARGETED.get(name, ())
                       if e_new[u])
        if still:
            link_bad.append((name + ' (external, declared fix reverted)',
                             still, []))
            page_ok = False
        if e_lost:
            link_bad.append((name + ' (external)', sorted(e_lost.elements()), []))
            page_ok = False

        # Figures are content.  visible_text drops every tag, so an image
        # that disappeared left no trace in the words and nothing else was
        # looking.  Compared by file name, ignoring the directory: Sphinx
        # republishes them under _images/ while txt2html referenced JPG/
        # directly.
        figures = lambda t: collections.Counter(
            b for b in (posixpath.basename(html.unescape(m.group(1)))
                        for m in re.finditer(
                            r'<img\b[^>]*?src\s*=\s*"([^"]*)"',
                            content_only(t), re.I))
            if b)
        fo, fn = figures(o), figures(n)
        # the equation images are the documented delta; they are gone by
        # design and equation-check.py is what verifies what replaced them
        fo = collections.Counter({k: v for k, v in fo.items()
                                  if k not in eq_image_names(o)})
        f_lost = fo - fn
        if f_lost:
            figure_bad.append((name, sorted(f_lost.elements())))
            page_ok = False
        # A fragment whose case changed is equivalent only if the anchor it
        # names actually exists in the new build, so both spellings resolve.
        # Verified per link rather than assumed.
        def resolve(href):
            # txt2html writes a self-reference as "thispage.html"; Sphinx
            # writes it as "#".  Same destination.
            if href == name:
                return '#'
            page, _, frag = href.partition('#')
            if not frag:
                return href
            target = new_dir / (page or name)
            if not target.exists():
                return href
            if frag in all_new_anchors.setdefault(
                    target.name, anchors(target.read_text(errors='replace'))):
                return page + '#' + frag.lower()
            return href
        oc = collections.Counter(resolve(k) for k in oc.elements())
        nc = collections.Counter(resolve(k) for k in nc.elements())
        lost = oc - nc
        added = nc - oc
        # Links the old page did not make are not automatically a fault: the
        # unescaped "<" swallowed some of them, and variable.txt's stray reST
        # left others as literal text, so recovering the words recovers the
        # link with them.  Allowed only where this page's text differences
        # were themselves agreed for one of those two reasons, and never
        # where a link was also lost.
        recoverable = agreed['unescaped_lt'] or agreed['rst_markup_in_source']
        # Rewrite the old page's targets through the declared moves, so a
        # declared retarget cancels out and everything else still shows.
        retarget = RETARGETED.get(name, {})
        if retarget:
            moved = collections.Counter()
            for target, count in oc.items():
                if target in retarget:
                    replacement = retarget[target][0]
                    if replacement is None:      # now points off-site
                        continue
                    moved[replacement] += count
                else:
                    moved[target] += count
            oc = moved
            lost, added = oc - nc, nc - oc
            for target in RESTORED.get(name, ()):
                if added[target]:
                    del added[target]
            if not lost and not added:
                agreed_total['links_retargeted'] += len(retarget)
                agreed_pages['links_retargeted'] += 1
        if added and not lost and recoverable:
            agreed_total['links_recovered'] += len(list(added.elements()))
            agreed_pages['links_recovered'] += 1
            if args.verbose:
                print(f'  ~ {name}: {len(list(added.elements()))} link(s) the '
                      f'old page hid, now visible (agreed)')
        elif lost or added:
            link_bad.append((name, sorted(lost.elements()), sorted(added.elements())))
            page_ok = False

        # A link that still points where it always did is only half the
        # check: the file it points at has to be in the build.  Sphinx
        # copies only the images a page displays, so a link to a file the
        # page merely points at -- the full-size version of a thumbnail --
        # silently 404s unless something else puts it there.
        #
        # Judged against the old tree rather than absolutely, so this
        # reports what the migration broke and not what was already broken.
        # Manual.pdf, for one, is built separately and dropped in beside the
        # manual; it is absent from both trees and is not this check's
        # business.
        for href in {h for h in nc.elements() if h != '#'}:
            target = href.split('#', 1)[0]
            if not target or target.startswith(('http', 'mailto', 'ftp')):
                continue
            if not (new_dir / target).exists() and (old_dir / target).exists():
                dangling.append((name, target))
                page_ok = False

        oa, na = anchors(o), anchors(n)
        # No filtering.  There used to be one here for anchors named
        # index*/search*, on the theory that they were Sphinx artifacts --
        # but those only ever appear in the new page, and this set is what
        # the old page had and the new one lost, so the filter could only
        # ever have hidden a real loss.
        lost_a = oa - na
        if lost_a:
            anchor_bad.append((name, sorted(lost_a)))
            page_ok = False

        if page_ok:
            ok += 1

    # Every file the old manual published under JPG/ has to still be
    # published.  Six full-size images were dropped during the conversion
    # and nothing noticed, because no page links to them -- they are the
    # large versions of thumbnails that are shown inline, reachable only by
    # typing the URL, which is exactly what an outside link does.  Compared
    # as an inventory rather than through the pages for that reason.
    #
    # Eqs/ is excluded: those images were equations, they are typeset now,
    # and equation-check.py verifies what replaced each one.
    assets_lost = []
    for sub in ('JPG',):
        o_dir, n_dir = old_dir / sub, new_dir / sub
        if not o_dir.is_dir():
            continue
        have = {f.name for f in n_dir.iterdir()} if n_dir.is_dir() else set()
        for f in sorted(o_dir.iterdir()):
            if f.is_file() and f.name not in have:
                assets_lost.append(f'{sub}/{f.name}')

    total = len(pages)
    print(f'\n  pages compared      {total}')
    print(f'  clean               {ok}')
    print(f'  missing in new      {len(missing)}')
    print(f'  text differs        {len(text_bad)}')
    print(f'  link targets moved  {len(link_bad)}')
    print(f'  figures lost        {len(figure_bad)}')
    print(f'  published files gone {len(assets_lost)}')
    print(f'  links that 404      {len(dangling)}')
    print(f'  anchors lost        {len(anchor_bad)}')
    if agreed_total:
        print('\n  agreed deltas:')
        for k in sorted(agreed_total):
            print(f'    {agreed_total[k]:4d} on {agreed_pages[k]:3d} page(s)  {k}')

    if dangling:
        print('\nLINKS THAT 404 (target not in the build):')
        seen = collections.Counter(t for _, t in dangling)
        for target, n_ in seen.most_common(20):
            print(f'  {target}  ({n_} link(s))')
    if missing:
        print('\nMISSING PAGES (URL would 404):')
        for m in missing:
            print(f'  {m}')
    if anchor_bad:
        print('\nANCHORS LOST (inbound links would break):')
        for name, a in anchor_bad[:20]:
            print(f'  {name}: {a[:8]}{" ..." if len(a) > 8 else ""}')
    if assets_lost:
        print('\nFILES THE OLD MANUAL PUBLISHED AND THIS BUILD DOES NOT:')
        for a in assets_lost[:20]:
            print(f'  {a}')
    if figure_bad:
        print('\nFIGURES LOST:')
        for name, figs in figure_bad[:20]:
            print(f'  {name}: {figs}')
    if link_bad:
        print('\nLINK TARGETS CHANGED:')
        for name, lost, added in link_bad[:20]:
            if lost:
                print(f'  {name}  lost:  {lost[:6]}{" ..." if len(lost) > 6 else ""}')
            if added:
                print(f'  {name}  added: {added[:6]}{" ..." if len(added) > 6 else ""}')
    if text_bad:
        print('\nTEXT DIFFERS (not covered by any agreed delta):')
        for name, diffs in text_bad[:15]:
            for d in diffs[:4]:
                print(f'  {name}  [{d["tag"]}: -{d["n_old"]} +{d["n_new"]}]')
                print(f'      old: ...{d["old"][:150]}...')
                print(f'      new: ...{d["new"][:150]}...')
            if len(diffs) > 4:
                print(f'      ... and {len(diffs) - 4} more on this page')

    failed = bool(missing or text_bad or link_bad or anchor_bad
                  or dangling or figure_bad or assets_lost)
    print('\n  RESULT: ' + ('PARITY FAILED' if failed else 'PARITY OK'))
    if not failed:
        print('  agreed deltas, in full:')
        for k, v in DELTAS.items():
            print(f'    {k}: {v}')
        for name, entries in sorted(DECLARED.items()):
            for d_old, d_new, key, why in entries:
                if why:
                    print(f'    {name} [{key}]: {why}')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
