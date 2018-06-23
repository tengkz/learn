#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 08:37:11 2018

@author: ubuntu
"""

import keras
from keras.layers import Input,LSTM,Dense
from keras.models import Model

tweet_a = Input(shape=(280,256))
tweet_b = Input(shape=(280,256))

shared_lstm = LSTM(64)

encoded_a = shared_lstm(tweet_a)
encoded_b = shared_lstm(tweet_b)

merged_vector = keras.layers.concatenate([encoded_a,encoded_b],axis=-1)

predictions = Dense(1,activation='sigmoid')(merged_vector)

model = Model(inputs=[tweet_a,tweet_b],outputs=predictions)

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

import numpy as np
data_a = np.random.rand(1000,280,256)
data_b = np.random.rand(1000,280,256)
labels = np.random.randint(2,size=(1000,1))

model.fit([data_a,data_b],labels,epochs=10)