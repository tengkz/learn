# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:01:15 2018

@author: hztengkezhen
"""

from keras.models import Sequential
from keras.layers import Conv1D,MaxPooling1D,GlobalAveragePooling1D
from keras.layers import Dense,Dropout

seq_length = 64
model = Sequential()
model.add(Conv1D(32,3,input_shape=(seq_length,10)))
model.add(Conv1D(32,3))
model.add(MaxPooling1D(3))
model.add(Conv1D(64,3))
model.add(Conv1D(64,3))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

import numpy as np
x_train = np.random.rand(128,seq_length,10)
y_train = np.random.randint(2,size=(128,1))

model.fit(x_train,y_train,epochs=5,batch_size=16)
model.evaluate(x_train,y_train,batch_size=32)