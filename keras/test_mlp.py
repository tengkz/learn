#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:23:59 2018

@author: ubuntu
"""

import keras
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.optimizers import SGD

import numpy as np
x_train = np.random.rand(10000,20)
y_train_label = np.random.randint(10,size=(10000,1))
y_train = keras.utils.to_categorical(y_train_label,num_classes=10)
x_test = np.random.rand(1000,20)
y_test_label = np.random.randint(10,size=(1000,1))
y_test = keras.utils.to_categorical(y_test_label,num_classes=10)

model = Sequential()
model.add(Dense(64,activation='relu',input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

sgd = SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=20,batch_size=128)
score = model.evaluate(x_test,y_test,batch_size=128)