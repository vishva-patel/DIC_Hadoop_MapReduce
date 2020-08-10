#!/usr/bin/python3

import sys

#using stdin for input
for line in sys.stdin:

    #.strip() to remove spaces
    line = line.strip()

    #using .split() to segregate words
    words = line.split()

    #using '/t' to separate words and '1'
    #instead of doing "print([word, "1"])"
    #because reducer will separate and count
    #using the '\t' .split() partitioning
    for word in words:
        print('%s\t%s' % (word, "1"))
