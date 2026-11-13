#!/usr/bin/env python3
"""Check that every internal link in the built site resolves.

Both halves of a link matter.  The file has to be there, and so does the
anchor: an anchor name is part of a URL, renaming one breaks an inbound
link just as surely as deleting the page, and it is the failure this
migration was most at risk of.

This runs against the build alone, with no reference to the txt2html
manual, so unlike parity-check.py and equation-check.py it keeps working
after the migration is over.  It is what CI runs.

Usage:
    link-check.py HTML_DIR
"""
import argparse
import html
import pathlib
import re
import sys

# <a name="..."> is the anchor form the conversion kept for the names the
# old manual published; id="..." on any element is Sphinx's own.  Scoped to
# inside a tag, because the manual's prose contains things like
# 'the default mixture has an ID = "all"', which is text, not an anchor.
NAME = re.compile(r'<a\b[^>]*?\bname\s*=\s*"([^"]+)"', re.I)
TAG = re.compile(r'<[a-zA-Z][^>]*>')
ID = re.compile(r'\bid\s*=\s*"([^"]+)"', re.I)
HREF = re.compile(r'<a\b[^>]*?href\s*=\s*"([^"]*)"', re.I)

# The manual is a separate Sphinx project, in the SPARTA repository, whose
# built pages are copied in under doc/ when a release is made.  It is
# legitimately absent from a build of the site alone, so links into it are
# counted separately rather than reported as broken -- but only links into
# doc/, and only when doc/ is not there at all.  Once it has been copied in
# they are checked like any other link.
MANUAL = 'doc'

# What is left is not a broken link but a missing file: four things the
# pages point at that this repository has never carried.  No edit to a
# link can fix them -- either the file gets added or the reference gets
# dropped, and both are editorial calls rather than link repair.
#
# Everything else that used to be listed here has been fixed at the
# source: commands renamed since the release note was written
# (fix_inflow -> fix_emit_face, accelerate_kokkos -> Section_accelerate
# #acc_3), four typoed targets, five manual pages linked without their
# doc/ prefix, two bench anchors, and other.txt's missing pizza alias.
KNOWN_BROKEN = {
    # three patch listings the repository does not contain, though the
    # patches on either side of those dates are there
    'bug.html': {'patches/files.11Jun16', 'patches/files.24May16',
                 'patches/files.4Apr17'},
    # a 165 MB QuickTime movie, which is presumably why it was never
    # committed; the still beside it is present and does resolve
    'pictures.html': {'movies/rti_longtime.mov'},
}


def anchors(text):
    found = set(NAME.findall(text))
    for tag in TAG.finditer(text):
        found |= set(ID.findall(tag.group(0)))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html_dir')
    args = ap.parse_args()
    root = pathlib.Path(args.html_dir)
    if not root.is_dir():
        print(f'no such directory: {root}', file=sys.stderr)
        return 2

    # Every page in the tree, keyed by its path below the root, so that a
    # link from bench/plot_free.html into ../index.html is resolved against
    # the directory it was written in.  The manual under doc/ is indexed as
    # a link target -- the site links into it constantly -- but not walked
    # as a source: it is a separate project and checks its own links.
    pages = sorted(p for p in root.rglob('*.html')
                   if p.relative_to(root).parts[0] != MANUAL)
    have = {p.relative_to(root).as_posix(): anchors(p.read_text(errors='replace'))
            for p in root.rglob('*.html')}

    bad = []
    known = 0
    unbuilt = set()
    for page in pages:
        name = page.relative_to(root).as_posix()
        text = page.read_text(errors='replace')
        for m in HREF.finditer(text):
            href = html.unescape(m.group(1))
            if href.startswith(('http', 'mailto', 'ftp', 'javascript:')):
                continue
            target, _, frag = href.partition('#')
            allowed = KNOWN_BROKEN.get(name, ())
            if href in allowed or (target and target in allowed):
                known += 1
                continue
            if target and not (page.parent / target).exists():
                # The manual is a separate project, copied in under doc/ at
                # release time, so it is legitimately absent from a build of
                # the site alone.  Only doc/, and only when it is not there.
                if target.split('/')[0] == MANUAL and not (root / MANUAL).is_dir():
                    unbuilt.add(target)
                    continue
                bad.append(f'{name} -> {target} (no such file)')
                continue
            # the anchor is looked for in the file the link actually reaches
            dest = name
            if target:
                resolved = (page.parent / target).resolve()
                try:
                    dest = resolved.relative_to(root.resolve()).as_posix()
                except ValueError:      # a link that climbs out of the tree
                    continue
            if frag and dest in have and frag not in have[dest]:
                if '#' + frag in allowed:
                    known += 1
                    continue
                bad.append(f'{name} -> {href} (no such anchor)')

    for b in sorted(set(bad)):
        print(f'  {b}')
    if known:
        print(f'  note: {known} link(s) already broken before the conversion, '
              f'listed in KNOWN_BROKEN')
    if unbuilt:
        print(f'  note: {len(unbuilt)} link(s) into doc/ not checked; the '
              f'manual is copied in from the SPARTA repository at release')
    n = len(set(bad))
    print(f'  {n} dead internal link(s) or anchor(s) in {len(pages)} pages')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())
