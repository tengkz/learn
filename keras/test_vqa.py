#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:06:54 2018

@author: ubuntu
"""

import keras
from keras.layers import Conv2D,MaxPooling2D,Flatten
from keras.layers import Input,LSTM,Embedding,Dense
from keras.models import Model,Sequential

vision_model = Sequential()
vision_model.add(Conv2D(64,(3,3),activation='relu',padding='same',input_shape=(224,224,3)))
vision_model.add(Conv2D(64,(3,3),activation='relu'))
vision_model.add(MaxPooling2D((2,2)))
vision_model.add(Conv2D(128,(3,3),activation='relu',padding='same'))
vision_model.add(Conv2D(128,(3,3),activation='relu'))
vision_model.add(MaxPooling2D(2,2))
vision_model.add(Conv2D(256,(3,3),activation='relu',padding='same'))
vision_model.add(Conv2D(256,(3,3),activation='relu'))
vision_model.add(Conv2D(256,(3,3),activation='relu'))
vision_model.add(MaxPooling2D((2,2)))
vision_model.add(Flatten())

image_input = Input(shape=(224,224,3))
encoded_image = vision_model(image_input)

question_input = Input(shape=(100,),dtype='int32')
embedded_question = Embedding(input_dim=10000,output_dim=256,input_length=100)(question_input)
encoded_question = LSTM(128)(embedded_question)

print encoded_question.shape

merged = keras.layers.concatenate([encoded_question,encoded_image])
output = Dense(1000,activation='softmax')(merged)

vqa_model = Model(inputs=[image_input,question_input],outputs=output)