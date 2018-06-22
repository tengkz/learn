# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:40:09 2018

@author: hztengkezhen
"""

from keras.models import Sequential
from keras.layers import Dense,LSTM
import numpy as np

timesteps = 8
data_dim = 16
num_classes = 10

model = Sequential()
model.add(LSTM(32,return_sequences=True,stateful=True,batch_input_shape=(8,timesteps,data_dim)))
model.add(LSTM(32,return_sequences=True,stateful=True))
model.add(LSTM(32,stateful=True))
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

x_train = np.random.rand(128,timesteps,data_dim)
y_train = np.random.rand(128,num_classes)

model.fit(x_train,y_train,epochs=5,batch_size=8)
model.evaluate(x_train,y_train,batch_size=8)