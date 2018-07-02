#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:26:39 2018

@author: ubuntu
"""

def process_chinese_text(text):
    before_char = [u'"',u'“',u'”',u'？',u'：',
                   u'；',u'，',u'。',u'！',u'（',
                   u'）',u'——',u'']
    after_char = [u'',u'',u'',u'.',u',',
                  u'.',u',',u'.',u'.',u',',
                  u'',u',',u'']
    for b,a in zip(before_char,after_char):
        text = text.replace(b,a)
    return text

def read_chinese_file(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    text = []
    for i in range(len(lines)):
        line = lines[i].decode('utf-8').strip()
        if line:
            text.append(line)
    text = ''.join(text)
    return text

def text_to_words(text):
    import jieba
    result = jieba.cut(text)
    result = '#'.join(list(result))
    return result.split('.')

def src_to_words(filename):
    text = read_chinese_file(filename)
    text = process_chinese_text(text)
    result = text_to_words(text)
    basename,extension = filename.split('.')
    words_filename = basename+'_words.'+extension
    with open(words_filename,'w') as f:
        f.write(('.\n'.join(result)).encode('utf-8'))
    
if __name__ == '__main__':
    filename = 'F:/data/text/antusheng.txt'
    src_to_words(filename)