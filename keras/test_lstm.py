# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:37:18 2018

@author: hztengkezhen
"""

import keras
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Dense,Dropout

model = Sequential()
model.add(Embedding(input_dim=1024,output_dim=256))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

import numpy as np
x_train = np.random.randint(1024,size=(128,10))
y_train = np.random.randint(2,size=(128,1))
model.fit(x_train,y_train,epochs=5,batch_size=16)
