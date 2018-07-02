# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 09:11:50 2018

@author: hztengkezhen
"""

import numpy as np
import math
from operator import itemgetter

def read_ratings(filename):
    with open(filename,'r') as f:
        content = f.readlines()
    data = [line.strip().split('::') for line in content]
    data = [(item[0],item[1]) for item in data]
    return data

def list_to_dict(data):
    result = {}
    for element in data:
        user,item = element
        if user not in result:
            result[user] = set([])
        result[user].add(item)
    return result

def train_test_split(data,k,M=10):
    s = np.random.randint(M,size=(len(data),))
    train = [item for i,item in enumerate(data) if s[i]!=k]
    test = [item for i,item in enumerate(data) if s[i]==k]
    data_train = list_to_dict(train)
    data_test = list_to_dict(test)
    return data_train,data_test

def user_similarity(data):
    item_users = {}
    user_cnt = dict([(k,len(v)) for k,v in data.iteritems()])
    for user,items in data.iteritems():
        for item in items:
            if item not in item_users:
                item_users[item] = set([])
            item_users[item].add(user)
    user_matrix = {}
    for item,users in item_users.iteritems():
        for u in users:
            for v in users:
                if u==v:
                    continue
                if u not in user_matrix:
                    user_matrix[u] = {}
                if v not in user_matrix[u]:
                    user_matrix[u][v] = 0
                user_matrix[u][v]+=1
    for u,vs in user_matrix.iteritems():
        for v in vs:
            user_matrix[u][v] = user_matrix[u][v]*1.0/math.sqrt(user_cnt[u]*user_cnt[v])
    return user_matrix

def recommend_usercf(user,train,user_matrix,K):
    rank = dict()
    iteracted_items = train[user]
    for v,wuv in sorted(user_matrix[user].items(),key=itemgetter(1),reverse=True)[0:K]:
        for i in train[v]:
            if i in iteracted_items:
                continue
            if i not in rank:
                rank[i] = 0
            rank[i] += wuv
    return rank

filename = 'F:\\data\\rec\\movielens_1m\\ml-1m\\ratings.dat'
data = read_ratings(filename)
print 'read finish'
data_train,data_test = train_test_split(data,0,10)
print 'split finish'
user_matrix = user_similarity(data_train)
print 'similarity finish'

K = 10
precision = []
recall = []
for user in data_test.keys():
    if user in data_test.keys():
        rec = recommend_usercf(user,data_train,user_matrix,K)
        rec_items = sorted(rec.items(),key=itemgetter(1),reverse=True)[0:10]
        rec_items = set([item[0] for item in rec_items])
        p = 1.0*len(rec_items&data_test[user])/len(rec_items)
        r = 1.0*len(rec_items&data_test[user])/len(data_test[user])
        precision.append(p)
        recall.append(p)
print 'Precision: ',sum(precision)/len(precision)
print 'Recall: ',sum(recall)/len(recall)