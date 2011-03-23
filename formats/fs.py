# fs.py
# Parsing FreeSurfer output
# Copyright (c) 2011 Washington University
# Author: Kevin A. Archie <karchie@wustl.edu>

from pyparsing import Combine, OneOrMore, Optional, Word, ZeroOrMore, alphas, alphanums, nums

header = '#' + ZeroOrMore(Word(alphanums))
number = Combine(Word("-"+nums, nums) + Optional('.' + Optional(Word(nums))))
content = Word(alphas) + OneOrMore(number)
any = header | content

def read_header(f):
    index = {}
    for line in f:
        fields = header.parseString(line)
        # TODO: verify alignment of column definitions
        if len(fields) > 1 and "ColHeaders" == fields[1]:
            break

def read_stats(f):
    row = []
    for line in f:
        fields = content.parseString(line)
        # TODO: verify alignment of structure rows
        # fields not included:
        #  structure name
        #  number of vertices
        # TODO: convert SD to CV
        row = row + map(float, fields[2:])
    return row

