#!/usr/bin/env python
#
# Script to verify extensions entry point and report empty ones.
#
# Usage:
#
#   cd mediawiki/extensions
#   python check-entry-points.py
#
# Authors:
#  - Antoine "hashar" Musso, 2014
#  - Wikimedia Foundation Inc, 2014
#  - iSC Inc., 2014

import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Files which are often added straight after an extension repository has been
# created.  If we only have some of them, that means the repository can be
# considered empty.
DEFAULT_FILES = ['.git', '.gitignore', '.gitreview']


for extension in sorted(os.listdir(BASE_DIR)):

    ext_dir = os.path.join(BASE_DIR, extension)

    if (extension == '.git' or os.path.isfile(ext_dir)):
        continue

    entry_point = os.path.join(BASE_DIR, extension, extension + ".php")
    if not os.path.exists(entry_point):
        dir_items = os.listdir(ext_dir)
        cwd = os.getcwd()
        if set(dir_items) - set(DEFAULT_FILES):
            print "Missing entry point: %s" % os.path.relpath(entry_point, cwd)
        else:
            print "Empty repository: %s" % os.path.relpath(ext_dir, cwd)
