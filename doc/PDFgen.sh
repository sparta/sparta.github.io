#!/bin/bash
# generate a PDF version of Manual

# NOTE: must be run with bash to get lexicographic ordering correct
#   for [a-z]*.html to NOT include filenames that start with upppercase letter

~/tools/txt2html/txt2html -b *.txt

htmldoc --title --toctitle "Table of Contents" --tocfooter ..i --toclevels 4 --header ... --footer ..1 --size letter --linkstyle plain --linkcolor blue -f Manual.pdf Manual.html Section_intro.html Section_start.html Section_commands.html Section_packages.html Section_accelerate.html Section_howto.html Section_example.html Section_perf.html Section_tools.html Section_modify.html Section_python.html Section_errors.html Section_history.html [a-z]*.html

~/tools/txt2html/txt2html *.txt
