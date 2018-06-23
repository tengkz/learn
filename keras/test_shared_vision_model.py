#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:01:18 2018

@author: ubuntu
"""

import keras
from keras.models import Model
from keras.layers import Input,Conv2D,MaxPooling2D
from keras.layers import Flatten,Dense

digit_input = Input(shape=(27,27,1))
x = Conv2D(64,(3,3))(digit_input)
x = Conv2D(64,(3,3))(x)
x = MaxPooling2D((2,2))(x)
out = Flatten()(x)

vision_model = Model(digit_input,out)

digit_a = Input(shape=(27,27,1))
digit_b = Input(shape=(27,27,1))

out_a = vision_model(digit_a)
out_b = vision_model(digit_b)

concatenated = keras.layers.concatenate([out_a,out_b])
out = Dense(1,activation='sigmoid')(concatenated)

classification_model = Model([digit_a,digit_b],out)