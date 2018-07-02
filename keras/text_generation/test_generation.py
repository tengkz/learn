# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:01:23 2018

@author: hztengkezhen
"""

from collections import Counter

def word_indices(text):
    counter = Counter()
    for words in text:
        for word in words:
            counter[word]+=1
    return counter

filename = 'F:/data/text/antusheng_words.txt'
with open(filename,'r') as f:
    lines = f.readlines()

text = [line.strip().split('#') for line in lines]
        
counter = word_indices(text)