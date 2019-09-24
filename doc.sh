#! /bin/sh
# Generates the documentation for temci

SPHINXDOC=True sphinx-apidoc -o doc -F -H "ldrand" -A "Johannes Bechberger" -V `ldrandv` ldrand -d 100
cd doc; make html; rm README_.rst
