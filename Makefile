# Build the SPARTA web site with Sphinx.
#
# Sphinx and its dependencies are installed into a virtualenv under
# siteenv the first time a build runs, so the only prerequisite is a
# python3 with venv available.
#
# The manual is not built here.  It is a separate Sphinx project in the
# SPARTA repository, under doc/, and its built pages are copied into doc/
# here when a release is made.  This build leaves doc/ alone.

SHELL          = /bin/bash
BUILDDIR       = $(shell pwd)
RSTDIR         = $(BUILDDIR)/src
VENV           = $(BUILDDIR)/siteenv
SPHINXCONFIG   = $(BUILDDIR)/utils/sphinx-config
PYTHON         = python3
SPHINXEXTRA    =

.PHONY: help clean clean-all html check publish

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "  html          build the site into html/"
	@echo "  check         verify every internal link and anchor in html/"
	@echo "  publish       copy html/ over the served pages at the repo root"
	@echo "  clean         remove the build tree, keep the virtualenv"
	@echo "  clean-all     also remove the virtualenv"
	@echo ""
	@echo "  SPHINXEXTRA=... passes extra flags to sphinx-build, e.g."
	@echo "  make html SPHINXEXTRA=\"-j auto -W --keep-going\""

clean:
	rm -rf $(BUILDDIR)/html $(BUILDDIR)/doctrees

clean-all: clean
	rm -rf $(VENV)

# A partial virtualenv is removed on the way out: it would otherwise be
# left newer than requirements.txt, so the next make would take it for a
# finished one and build against half-installed dependencies.
$(VENV): utils/requirements.txt
	@rm -rf $(VENV)
	@{ $(PYTHON) -m venv $(VENV) && \
	   . $(VENV)/bin/activate && \
	   pip install --upgrade pip wheel > /dev/null && \
	   pip install -r $(BUILDDIR)/utils/requirements.txt; \
	 } || { rm -rf $(VENV); exit 1; }
	@touch $(VENV)

# && rather than ; so a failed sphinx-build fails the target: with ; the
# recipe's status is that of the last command in the list, and a broken
# site would look like a good one.
html: $(VENV)
	@. $(VENV)/bin/activate && \
	 sphinx-build $(SPHINXEXTRA) -b html \
	   -c $(SPHINXCONFIG) -d $(BUILDDIR)/doctrees $(RSTDIR) html
	@echo "Build finished. The site is in html."

check: html
	@$(PYTHON) $(BUILDDIR)/utils/link-check.py $(BUILDDIR)/html

# GitHub Pages serves this repository from its root, so the built pages
# have to sit beside doc/ rather than inside html/.  Kept as an explicit
# step rather than building into the root directly: sphinx-build owns its
# output directory, and the root is not something to hand over to it --
# doc/, images/, movies/ and the rest live there.
#
# The site is served from a branch, so GitHub runs it through Jekyll first,
# and Jekyll drops every directory whose name starts with "_" -- Sphinx's
# _static (stylesheet) and _images (thumbnails) among them.  .nojekyll at
# the root turns that off.  It is committed, and recreated here in case it
# has gone missing, because without it the published site loses its
# styling and its pictures without any error.
publish: html
	@cp -r $(BUILDDIR)/html/. $(BUILDDIR)/
	@touch $(BUILDDIR)/.nojekyll
	@echo "Published. Commit the changed pages at the repository root."
