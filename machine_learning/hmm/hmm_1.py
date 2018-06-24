#!/usr/bin/python
#coding:utf-8

import numpy as np

def hmm_learn_forback(seq,A,B,pai,alpha,beta):
    length = len(seq)
    istate = len(A)
    
    #forward
    for index,item in enumerate(seq):
        if index == 0:
            for i in xrange(istate):
                alpha[i][index] = pai[i]*B[i][item]
        else:
            for i in xrange(istate):
                tmp = 0.0
                for j in xrange(istate):
                    tmp += alpha[j][index-1]*A[j][i]
                tmp *= B[i][item]
                alpha[i][index] = tmp
    #backward
    for index in xrange(length-1,-1,-1):
        if index == length-1:
            for i in xrange(istate):
                beta[i][index] = 1.0
        else:
            for i in xrange(istate):
                tmp = 0.0
                for j in xrange(istate):
                    tmp += beta[j][index+1]*A[i][j]*B[j][seq[index+1]]
                beta[i][index] = tmp

def hmm_learn_forback_scale(seq,A,B,pai,alpha,beta):
    length = len(seq)
    istate = len(A)
    
    #forward
    for index,item in enumerate(seq):
        if index == 0:
            for i in xrange(istate):
                alpha[i][index] = pai[i]*B[i][item]
        else:
            for i in xrange(istate):
                tmp = 0.0
                for j in xrange(istate):
                    tmp += alpha[j][index-1]*A[j][i]
                tmp *= B[i][item]
                alpha[i][index] = tmp
    
    #scale forward result
    for i in xrange(length):
        s = 0.0
        for j in xrange(istate):
            s += alpha[j][i]
        for j in xrange(istate):
            alpha[j][i] /= s
    
    #backward
    for index in xrange(length-1,-1,-1):
        if index == length-1:
            for i in xrange(istate):
                beta[i][index] = 1.0
        else:
            for i in xrange(istate):
                tmp = 0.0
                for j in xrange(istate):
                    tmp += beta[j][index+1]*A[i][j]*B[j][seq[index+1]]
                beta[i][index] = tmp
    
    #scale backward result
    for i in xrange(length):
        s = 0.0
        for j in xrange(istate):
            s += beta[j][i]
        for j in xrange(istate):
            beta[j][i] /= s

def hmm_learn_repsilon(alpha,beta,seq,A,B,r,epsilon):
    length = len(seq)
    istate = len(A)
    
    #update r
    ab = [0.0 for i in xrange(length)]
    for t in xrange(length):
        for j in xrange(istate):
            ab[t] += alpha[j][t]*beta[j][t]
    for t in xrange(length):
        for j in xrange(istate):
            r[j][t] = alpha[j][t]*beta[j][t]/ab[t]

    #update epsilon
    for t in xrange(length-1):
        for i in xrange(istate):
            for j in xrange(istate):
                tmp = 0.0
                for m in xrange(istate):
                    for n in xrange(istate):
                        tmp += alpha[m][t]*A[m][n]*B[n][seq[t+1]]*beta[n][seq[t+1]]
                epsilon[t][i][j] = alpha[i][t]*A[i][j]*B[j][seq[t+1]]*beta[j][seq[t+1]]/tmp

def hmm_learn_e(seq,A,B,pai,alpha,beta,r,epsilon):
    hmm_learn_forback_scale(seq,A,B,pai,alpha,beta)
    hmm_learn_repsilon(alpha,beta,seq,A,B,r,epsilon)

def hmm_learn_abphi(seq,A,B,pai,r,epsilon):
    length = len(seq)
    istate = len(A)
    ostate = len(B[0])

    #update A
    for i in xrange(istate):
        for j in xrange(istate):
            tmp1,tmp2 = 0.0,0.0
            for t in xrange(length-1):
                tmp1 += epsilon[t][i][j]
                tmp2 += r[i][t]
            A[i][j] = 0.001/istate+0.999*tmp1/tmp2

    #update B
    for i in xrange(istate):
        for k in xrange(ostate):
            tmp1,tmp2 = 0.0,0.0
            for t in xrange(length):
                if seq[t] == k:
                    tmp1 += r[i][t]
                tmp2 += r[i][t]
            B[i][k] = 0.001/istate+0.999*tmp1/tmp2

    #update phi
    for i in xrange(istate):
        pai[i] = r[i][0]

def hmm_learn_m(seq,A,B,pai,r,epsilon):
    hmm_learn_abphi(seq,A,B,pai,r,epsilon)

def rand_dis(n):
    import random
    randint = random.Random()
    ret = np.zeros((n,1))
    for i in xrange(n):
        ret[i] = randint.randint(0,100)
    s = sum(ret)
    ret /=s
    return ret
    
def hmm_learn(seq,istate=3):
    
    #initialize parameters
    length = len(seq)
    ostate = len(set(seq))
    t1 = 1.0/istate
    t2 = 1.0/ostate
    A = np.zeros((istate,istate))
    for i in xrange(istate):
        tmp = rand_dis(istate)
        for j in xrange(istate):
            A[i,j] = tmp[j]
    B = np.ones((istate,ostate))*t2
    pai = np.ones((istate,1))*t1
    #A = [[t1 for i in xrange(istate)] for j in xrange(istate)]
    #B = [[t2 for i in xrange(ostate)] for j in xrange(istate)]
    #pai = [t1 for i in xrange(istate)]

    #map
    dic_for = {}
    dic_back = {}
    for index,item in enumerate(set(seq)):
        dic_for[item] = index
        dic_back[index] = item
    seq_trans = [dic_for[item] for item in seq]

    #forward and backward
    alpha = np.zeros((istate,length))
    beta = np.zeros((istate,length))
    r = np.zeros((istate,length))
    epsilon = np.zeros((length,istate,istate))
    #alpha = [[0.0 for i in xrange(istate)] for j in xrange(length)]
    #beta = [[0.0 for i in xrange(istate)] for j in xrange(length)]
    #r = [[0.0 for i in xrange(istate)] for j in xrange(length)]
    #epsilon = [[[0.0 for i in xrange(istate)] for j in xrange(istate)] for k in xrange(length)]

    for i in xrange(20):
        import copy
        pre_A = copy.deepcopy(A)        
        #e step
        hmm_learn_e(seq_trans,A,B,pai,alpha,beta,r,epsilon)
        #m step
        hmm_learn_m(seq_trans,A,B,pai,r,epsilon)
        print sum(sum(abs(A-pre_A)))
        print A

    return A,B,pai

if __name__ == "__main__":
    A,B,pai = hmm_learn("abcabc")
#    A = np.array([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
#    B = np.array([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
#    pai = np.array([0.2,0.4,0.4])
#    seq=[0,1,0]
#    alpha = np.zeros((3,3))
#    beta = np.zeros((3,3))
#    r = np.zeros((3,3))
#    epsilon = np.zeros((3,3,3))
#    hmm_learn_forback(seq,A,B,pai,alpha,beta)
#    hmm_learn_repsilon(alpha,beta,seq,A,B,r,epsilon)
    