# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:53:10 2018

@author: hztengkezhen
"""

import keras
from keras.layers import Input,Dense
from keras.models import Model

inputs = Input(shape=(784,))

x = Dense(64,activation='relu')(inputs)
x = Dense(64,activation='relu')(x)
predictions = Dense(10,activation='softmax')(x)

model = Model(inputs = inputs,outputs = predictions)
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

import numpy as np
x_train = np.random.rand(1000,784)
y_label_train = np.random.randint(10,size=(1000,1))
y_train = keras.utils.to_categorical(y_label_train,num_classes=10)
model.fit(x_train,y_train,batch_size=16,epochs=5)

from keras.layers import TimeDistributed

input_sequences = Input(shape=(20,784))

processed_sequences = TimeDistributed(model)(input_sequences)