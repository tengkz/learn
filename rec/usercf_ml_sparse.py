# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 14:27:26 2018

@author: hztengkezhen
"""

import numpy as np
from scipy.sparse import csr_matrix
from operator import itemgetter

def read_ratings(filename):
    with open(filename,'r') as f:
        content = f.readlines()
    data = [line.strip().split('::') for line in content]
    data = [(int(item[0]),int(item[1])) for item in data]
    return data

def train_test_split(data,k,M=10):
    s = np.random.randint(M,size=(len(data),))
    train = [item for i,item in enumerate(data) if s[i]!=k]
    test = [item for i,item in enumerate(data) if s[i]==k]
    return train,test

def data_to_sparse(data):
    rows = [item[0] for item in data]
    cols = [item[1] for item in data]
    data_csr = csr_matrix((np.ones(shape=(len(data),)),(np.array(rows),np.array(cols))))
    return data_csr

def user_similarity(data_csr):
    print data_csr.shape
    numerator = (data_csr*data_csr.transpose()).todense()
    diag = numerator.diagonal()
    num_users = data_csr.shape[0]
    tile_matrix= np.tile(diag,[num_users,1])
    denominator = np.multiply(tile_matrix,tile_matrix.transpose())
    user_matrix = numerator/np.sqrt(denominator)
    where_are_nan = np.isnan(user_matrix)
    user_matrix[where_are_nan] = 0.0
    return user_matrix

def recommend_usercf(user,train,user_matrix,topk):
    buyed_items = set(train.getrow(user).nonzero()[1])
    user_nums = train.shape[0]
    user_range = range(user_nums)
    rank = np.zeros(shape=(user_nums,))
    for v,wuv in sorted(zip(user_range,user_matrix[user].tolist()[0]),key=itemgetter(1),reverse=True)[0:topk]:
        for i in train.getrow(v).nonzero()[1]:
            if i in buyed_items:
                continue
            rank[i] += wuv
    ret = sorted(zip(user_range,rank),key=itemgetter(1),reverse=True)[0:K]
    return [item[0] for item in ret]

def evaluation(data_train,data_test):
    data_train_csr = data_to_sparse(data_train)
    data_test_csr = data_to_sparse(data_test)
    user_matrix = user_similarity(data_train_csr)
    pp = np.zeros(shape=(data_test_csr.shape[0],))
    rr = np.zeros(shape=(data_test_csr.shape[0],))
    for u in range(1,data_test_csr.shape[0]):
        rec = set(recommend_usercf(u,data_train_csr,user_matrix,topk))
        real = set(data_test_csr.getrow(u).nonzero()[1].tolist())
        p = 1.0*len(rec&real)/len(rec)
        r = 1.0*len(rec&real)/(1.0 if len(real)==0 else len(real))
        pp[u] = p
        rr[u] = r
    return pp.mean(),rr.mean()

K = 5
topk = 10
filename = 'F:\\data\\rec\\movielens_1m\\ml-1m\\ratings.dat'
data = read_ratings(filename)

precision = []
recall = []
for iteration in range(5):
    print 'Iteration: ',iteration
    data_train,data_test = train_test_split(data,iteration,10)
    p,r = evaluation(data_train,data_test)
    precision.append(p)
    recall.append(r)
    
print 'Precision: ',sum(precision)/len(precision)
print 'Recall: ',sum(recall)/len(recall)