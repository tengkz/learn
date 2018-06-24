#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:41:48 2018

@author: ubuntu
"""

from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Conv1D,MaxPooling1D
from keras.datasets import imdb

max_features = 20000
maxlen = 100
embedding_dims = 128

filters = 64
kernel_size = 5
pool_size = 4

lstm_output_size = 70

batch_size = 32
epochs = 2

print('Loading data...')
(x_train,y_train),(x_test,y_test) = imdb.load_data(num_words=max_features)
print(len(x_train),'train sequences')
print(len(x_test),'test sequences')

print('Pad sequences (sample x time)')
x_train = sequence.pad_sequences(x_train,maxlen=maxlen)
x_test = sequence.pad_sequences(x_test,maxlen=maxlen)
print('x_train shape:',x_train.shape)
print('x_test shape:',x_test.shape)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features,embedding_dims,input_length=maxlen))
model.add(Dropout(0.25))
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
model.add(MaxPooling1D(pool_size=pool_size))
model.add(LSTM(lstm_output_size))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train,y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test,y_test))
score,acc = model.evaluate(x_test,y_test,batch_size=batch_size)

print('Test score:',score)
print('Test accuracy:',acc)