#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

replacements = (
    ("\\\"{a}", "�"),
    ("\\\"{o}", "�"),
    ("\\\"{u}", "�"),
    ("\\\"{A}", "�"),
    ("\\\"{O}", "�"),
    ("\\\"{U}", "�"),
    ("\\\"a", "�"),
    ("\\\"o", "�"),
    ("\\\"u", "�"),
    ("\\\"A", "�"),
    ("\\\"O", "�"),
    ("\\\"U", "�"),
    ("\\ss{}", "�"),
    ("{\\ss}", "�")
)

import fileinput
for line in fileinput.input():
    for fromStr, toStr in replacements:
        line = line.replace(fromStr, toStr)
    print line,
