#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 08:49:54 2018

@author: ubuntu
"""

from keras.layers import Input
from keras.layers import Conv2D

a = Input(shape=(32,32,3))
b = Input(shape=(64,64,3))

conv = Conv2D(16,(3,3),padding='same')
conved_a = conv(a)

assert conv.input_shape == (None,32,32,3)

conved_b = conv(b)

assert conv.get_input_shape_at(0) == (None,32,32,3)
assert conv.get_input_shape_at(1) == (None,64,64,3)