#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 08:57:36 2018

@author: ubuntu
"""

import keras
from keras.layers import Input,Conv2D

x = Input(shape=(256,256,3))
y = Conv2D(3,(3,3),padding='same')(x)
z = keras.layers.add([x,y])