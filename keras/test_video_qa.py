#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:19:21 2018

@author: ubuntu
"""

import keras
from keras.layers import Conv2D,MaxPooling2D,Flatten
from keras.layers import Input,LSTM,Embedding,Dense
from keras.models import Model,Sequential
from keras.layers import TimeDistributed

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

video_input = Input(shape=(100,224,224,3))
encoded_frame_sequence = TimeDistributed(vision_model)(video_input)
encoded_video = LSTM(256)(encoded_frame_sequence)

question_input = Input(shape=(100,),dtype='int32')
embedded_question = Embedding(input_dim=10000,output_dim=256,input_length=100)(question_input)
encoded_question = LSTM(128)(embedded_question)
question_encoder = Model(inputs=question_input,outputs=encoded_question)

video_question_input = Input(shape=(100,),dtype='int32')
encoded_video_question = question_encoder(video_question_input)

merged = keras.layers.concatenate([encoded_video,encoded_video_question])
output = Dense(1000,activation='softmax')(merged)
video_qa_model = Model(inputs=[video_input,video_question_input],outputs=output)
