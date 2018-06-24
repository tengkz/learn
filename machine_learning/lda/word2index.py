#!/usr/bin/python
#coding:utf-8

import sys

LOW_LIMIT = 10
HIGH_LIMIT = 3000

f = open('c','r')
content = f.readlines()

# word count
wc = {}
for line in content:
    for item in line.strip().split(' '):
        if item not in wc:
            wc[item] = 1
        else:
            wc[item] += 1

# high frequent words
d = {}
idx = 0
for line in content:
    for item in line.strip().split(' '):
        if item not in d and wc[item]>=LOW_LIMIT and wc[item]<=HIGH_LIMIT:
        #if item not in d and wc[item]>=LOW_LIMIT:
            d[item] = str(idx)
            idx+=1
for k in d:
    print k,d[k]

f_out = open('d','w')
output = []
for line in content:
    output = []
    for item in line.strip().split(' '):
        if item in d:
            output.append(d[item])
    f_out.write(' '.join(output))
    f_out.write('\n')
