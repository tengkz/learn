#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:11:10 2018

@author: ubuntu
"""

from __future__ import print_function

from keras.models import Sequential,Model
from keras.layers.embeddings import Embedding
from keras.layers import Input,Activation,Dense,Permute,Dropout,add,dot,concatenate
from keras.layers import LSTM
from keras.utils.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
from functools import reduce
import tarfile
import numpy as np
import re

def tokenize(sent):
    return [x.strip() for x in re.split('(\W+)?',sent) if x.strip()]

def parse_stories(lines,only_supporting=False):
    data = []
    story = []
    for line in lines:
        line = line.decode('utf-8').strip()
        nid,line = line.split(' ',1)
        nid = int(nid)
        if nid == 1:
            story = []
        if '\t' in line:
            q,a,supporting = line.split('\t')
            q = tokenize(q)
            substory = None
            if only_supporting:
                supporting = map(int,supporting.split())
                substory = [story[i-1] for i in supporting]
            else:
                substory = [x for x in story if x]
            data.append((substory,q,a))
            story.append('')
        else:
            sent = tokenize(line)
            story.append(sent)
    return data

def get_stories(f,only_supporting=False,max_length=None):
    data = parse_stories(f.readlines(),only_supporting=only_supporting)
    flatten = lambda data:reduce(lambda x,y:x+y,data)
    data = [(flatten(story),q,answer) for story,q,answer in data if not max_length or len(flatten(story))<max_length]
    return data

def vectorize_stories(data):
    inputs,queries,answers = [],[],[]
    for story,query,answer in data:
        inputs.append([word_idx[w] for w in story])
        queries.append([word_idx[w] for w in query])
        answers.append(word_idx[answer])
    return (pad_sequences(inputs,maxlen=story_maxlen),
            pad_sequences(queries,maxlen=query_maxlen),
            np.array(answers))
    
try:
    path = get_file('babi-tasks-v1-2.tar.gz',origin='https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz')
except:
    print('Error downloading dataset, please download it mannually:\n'
          '$ wget https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz\n')
    raise

challenges = {
        'single_supporting_fact_10k':'tasks_1-20_v1-2/en-10k/qa1_single-supporting-fact_{}.txt',
        'two_supporting_facts_10k':'tasks_1-20_v1-2/en-10k/qa2_two-supporting-facts_{}.txt',
        }
challenge_type = 'two_supporting_facts_10k'
challenge = challenges[challenge_type]

print('Extracting stories for the challenge:',challenge_type)

with tarfile.open(path) as tar:
    train_stories = get_stories(tar.extractfile(challenge.format('train')))
    test_stories = get_stories(tar.extractfile(challenge.format('test')))
    
vocab = set()
for story,q,answer in train_stories+test_stories:
    vocab |= set(story+q+[answer])
vocab = sorted(vocab)

vocab_size = len(vocab)+1
story_maxlen = max(map(len,(x for x,_,_ in train_stories+test_stories)))
query_maxlen = max(map(len,(x for _,x,_ in train_stories+test_stories)))

print('-')
print('Vocab size:',vocab_size,'unique words')
print('Story max length:',story_maxlen,'words')
print('Query max length:',query_maxlen,'words')
print('Number of training stories:',len(train_stories))
print('Number of test stories:',len(test_stories))
print('-')
print('Here\'s what a "story" tuple looks like (input,query,answer):')
print(train_stories[0])
print('-')
print('Vectorizing the word sequences...')

word_idx = dict((c,i+1) for i,c in enumerate(vocab))
inputs_train,queries_train,answers_train = vectorize_stories(train_stories)
inputs_test,queries_test,answers_test = vectorize_stories(test_stories)

input_sequence = Input((story_maxlen,))
question = Input((query_maxlen,))

input_encoder_m = Sequential()
input_encoder_m.add(Embedding(input_dim=vocab_size,output_dim=64))
input_encoder_m.add(Dropout(0.3))

input_encoder_c = Sequential()
input_encoder_c.add(Embedding(input_dim=vocab_size,output_dim=query_maxlen))
input_encoder_c.add(Dropout(0.3))

question_encoder = Sequential()
question_encoder.add(Embedding(input_dim=vocab_size,output_dim=64,input_length=query_maxlen))
question_encoder.add(Dropout(0.3))

input_encoded_m = input_encoder_m(input_sequence)
input_encoded_c = input_encoder_c(input_sequence)
question_encoded = question_encoder(question)

match = dot([input_encoded_m,question_encoded],axes=(2,2))
match = Activation('softmax')(match)

response = add([match,input_encoded_c])
response = Permute((2,1))(response)

answer = concatenate([response,question_encoded])
answer = LSTM(32)(answer)

answer = Dropout(0.3)(answer)
answer = Dense(vocab_size)(answer)
answer = Activation('softmax')(answer)

model = Model([input_sequence,question],answer)
model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit([inputs_train,queries_train],answers_train,
          batch_size=32,
          epochs=120,
          validation_data=([inputs_test,queries_test],answers_test))