#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:14:13 2018

@author: ubuntu
"""

from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense,Dropout,Embedding
from keras.layers import LSTM,Bidirectional
from keras.datasets import imdb
import numpy as np

max_features = 20000
maxlen = 100
batch_size = 32

print('Loading data...')
(x_train,y_train),(x_test,y_test) = imdb.load_data(num_words=max_features)
print(len(x_train),'train sequences')
print(len(x_test),'test sequences')

print('Pad sequences (sample x time)')
x_train = sequence.pad_sequences(x_train,maxlen=maxlen)
x_test = sequence.pad_sequences(x_test,maxlen=maxlen)
print('x_train shape:',x_train.shape)
print('x_test shape:',x_test.shape)
y_train = np.array(y_train)
y_test = np.array(y_test)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features,128,input_length=maxlen))
model.add(Bidirectional(LSTM(64)))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train,y_train,
          batch_size=batch_size,
          epochs=4,
          validation_data=(x_test,y_test))
score,acc = model.evaluate(x_test,y_test,batch_size=batch_size)

print('Test score:',score)
print('Test accuracy:',acc)