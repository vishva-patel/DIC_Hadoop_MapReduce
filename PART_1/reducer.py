#!/usr/bin/python3
import sys

#dictionarry to hold key-value pairs
#pair = word , its total count
ans_dict = {}

#using stdin for input
for line in sys.stdin:

    line = line.strip()

    #splitting the input from mapper.py
    #to get words and the "1"s associated
    word, count = line.split('\t', 1)

    #convert count(currently a string - "1") to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        ans_dict[word] = ans_dict[word]+count
    except:
        ans_dict[word] = count


for word in ans_dict.keys():
    #returning tuples of word - wordcount
    print([word, ans_dict[word]])

