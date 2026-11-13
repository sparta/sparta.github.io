# SPARTA web site build configuration file.
#
# This is the site -- index, features, papers, the abstracts and the
# benchmark tables.  The manual is a separate Sphinx project, in the SPARTA
# repository under doc/, and is copied in under doc/ here at release time.
# The two are kept apart deliberately: a landing page is not a manual
# chapter, and the manual has its own theme, its own table of contents and
# its own release cycle.  LAMMPS separates them the same way.
#
# Because they are separate, every link from here into the manual is an
# ordinary relative URL (doc/read_surf.html), not a :doc: reference.  There
# are around 400 of them and they resolve against whatever manual is
# sitting in doc/, which is what makes the release-time copy work.

import os

project = 'SPARTA'
copyright = 'Sandia National Laboratories'
author = 'The SPARTA Developers'

extensions = []

# Three pages embed raw HTML inline -- a "new" badge beside recent
# releases, and the linked thumbnails on the pictures page.  txt2html
# passed such runs through untouched; this role is how reST does the same.
rst_prolog = '''
.. role:: raw-html(raw)
   :format: html
'''
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []

# The site quotes input-script syntax and command names constantly, and the
# pages it replaces used straight quotes throughout, so leave the
# characters as written rather than curling them.
smartquotes = False

# One page carries a ":pre" block -- the four commands that build SPARTA
# for a benchmark machine -- and it was published as a plain <PRE>.
# Sphinx would run it through Pygments and colour it as Python, which is
# both wrong and a change to the page.
highlight_language = 'none'

# -- HTML ------------------------------------------------------------------
#
# "basic" rather than a documentation theme.  These pages are a web site:
# they have their own navigation table on the front page and no chapter
# hierarchy, so a theme that puts a 140-entry sidebar beside them would be
# showing the reader something that does not exist.  It also keeps this
# conversion close to what the site looks like today, which is what makes
# it reviewable.  Restyling is a separate change.
html_theme = 'basic'
html_title = 'SPARTA'
html_short_title = 'SPARTA'
html_sidebars = {'**': []}
html_show_sourcelink = False
html_copy_source = False
html_use_index = False
html_domain_indices = False

# site.css is what makes "basic" look like the published pages: full
# width, <H3>/<H4> headings, bordered centred tables, and none of the
# theme's own navigation.  See the comments in that file.
html_static_path = [os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '_static')]
html_css_files = ['site.css']

# The published pages have no per-heading permalinks, so none are emitted
# rather than emitted and hidden.
html_permalinks = False

# doc/ holds the manual, copied in from the SPARTA repository at release
# time.  It is a finished Sphinx build, not source for this one.
exclude_patterns = ['doc']


# -- The files the site serves alongside the pages -------------------------
#
# images, movies, inputs, patches and pdf are content the pages link to,
# not pages themselves.  Sphinx copies only what a page embeds, so they are
# copied wholesale, the same way the manual copies its JPG directory.
SITE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
EXTRA_DIRS = ('images', 'movies', 'inputs', 'patches', 'pdf', 'bench')


def copy_site_assets(app, exception):
    import shutil

    if exception is not None or app.builder.name not in ('html', 'dirhtml'):
        return
    for name in EXTRA_DIRS:
        src = os.path.join(SITE_DIR, name)
        if not os.path.isdir(src):
            continue
        dest = os.path.join(app.outdir, name)
        # bench holds 120 pages this project builds from its own sources,
        # so its .txt and .html are skipped -- but inputs/ is the opposite
        # case: those .txt files are the content, served verbatim as the
        # example input scripts the pages link to.
        skip = ('*.html',) if name == 'inputs' else ('*.txt', '*.html')
        shutil.copytree(src, dest, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(*skip))


def setup(app):
    app.connect('build-finished', copy_site_assets)
