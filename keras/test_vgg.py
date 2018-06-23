#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:41:08 2018

@author: ubuntu
"""

import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras.optimizers import SGD

x_train = np.random.rand(1000,100,100,3)
y_train_label = np.random.randint(10,size=(1000,1))
y_train = keras.utils.to_categorical(y_train_label,num_classes=10)
x_test = np.random.rand(100,100,100,3)
y_test_label = np.random.randint(10,size=(100,1))
y_test = keras.utils.to_categorical(y_test_label,num_classes=10)

model = Sequential()

model.add(Conv2D(32,(3,3),activation='relu',input_shape=(100,100,3)))
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

sgd = SGD(lr=0.01,momentum=0.9,decay=1e-6,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=32,epochs=10)
score = model.evaluate(x_test,y_test,batch_size=32)