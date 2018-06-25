#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:37:25 2018

@author: ubuntu
"""

from __future__ import print_function,division
from collections import Counter
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dense,Activation
from keras.optimizers import RMSprop
from keras.callbacks import LambdaCallback
import random
import sys

def process_chinese_text(text):
    before_char = [u'"',u'“',u'”',u'？',u'：',u'；']
    after_char = [u'',u'',u'',u'。',u'',u'。']
    for b,a in zip(before_char,after_char):
        text = text.replace(b,a)
    return text
    
def read_chinese_file(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    data = []
    for i in range(len(lines)):
        line = lines[i].decode('utf-8').strip()
        if line:
            data.append(line)
    data = ''.join(data)
    return data

def char_indices(text,num_words=100):
    counter = Counter()
    for char in text:
        counter[char]+=1
    counter = counter.most_common()[0:num_words]
    chars = [item[0] for item in counter]
    char_indices = dict((c,i) for i,c in enumerate(chars))
    indices_char = dict((i,c) for i,c in enumerate(chars))
    return char_indices,indices_char

def vectorize(text,char_indices):
    return [char_indices.get(c,1000) for c in text]

filename = '/data/text/antusheng.txt'
text = read_chinese_file(filename)
text = process_chinese_text(text)
print('Corpus length:',len(text))

valid_chars = 1000
num_chars = valid_chars+1
char_indices,indices_char = char_indices(text,valid_chars)
char_indices['#'] = valid_chars
indices_char[valid_chars] = '#'
print('Valid chars:',len(char_indices))

data = vectorize(text,char_indices)

maxlen = 10
step = 3
sentences = []
next_chars = []

for i in range(0,len(data)-maxlen,step):
    sentences.append(data[i:i+maxlen])
    next_chars.append(data[i+maxlen])
print('nb sentences:',len(sentences))

x = np.zeros((len(sentences),maxlen,num_chars),dtype=np.bool)
y = np.zeros((len(sentences),num_chars),dtype=np.bool)
for i,sentence in enumerate(sentences):
    for t,index in enumerate(sentence):
        x[i,t,index] = 1
    y[i,next_chars[i]] = 1

print('Build model...')
model = Sequential()
model.add(LSTM(128,input_shape=(maxlen,num_chars)))
model.add(Dense(num_chars))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',optimizer=RMSprop(lr=0.01))

def sample(preds,temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)/temperature
    exp_preds = np.exp(preds)
    preds = exp_preds/np.sum(exp_preds)
    probas = np.random.multinomial(1,preds,1)
    return np.argmax(probas)

def on_epoch_end(epoch,logs):
    print()
    print('--- Generating text after epoch: {}'.format(epoch))
    start_index = random.randint(0,len(data)-maxlen-1)
    for diversity in [0.2,0.5,1.0,1.2]:
        print('--- diversity:',diversity)
        generated = ''
        sentence = data[start_index:start_index+maxlen]
        sentence = ''.join([indices_char[i] for i in sentence])
        generated += sentence
        print('--- Generating with seed: "'+sentence+'"')
        sys.stdout.write(generated)
        for i in range(10):
            x_pred = np.zeros((1,maxlen,num_chars))
            for t,char in enumerate(sentence):
                x_pred[0,t,char_indices[char]] = 1.
            preds = model.predict(x_pred,verbose=0)[0]
            next_index = sample(preds,diversity)
            next_char = indices_char[next_index]
            generated += next_char
            sentence = sentence[1:]+next_char
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()

print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x,y,
          batch_size=128,
          epochs=10,
          callbacks=[print_callback])
