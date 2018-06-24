#!/usr/bin/python
#coding:utf-8

from numpy import *
from deltaLDA import deltaLDA
import pickle
import math
import sys

# alpha and beta *must* be NumPy Array objects
#
# Their dimensionalities implicitly specify:
# -the number of topics T
# -the vocabulary size W
# -number of f-label values F (just 1 for 'standard' LDA)
#
# alpha = F x T
# beta = T x W
#
topic_cnt = int(sys.argv[1])
alpha = .1 * ones((1,topic_cnt))
beta = ones((topic_cnt,649))

# docs must be a Python List of Python lists
# Each individual List contains the indices of word tokens
# (That is, docs[0] = "w1 w1 w2", docs[1] = "w1 w1 w1 w1 w2", etc) 
#
f = open('d','r')
content = f.readlines()
docs = []
for line in content:
    l = [int(item) for item in line.split(' ')]
    docs.append(l)

# numsamp specifies how many samples to take from the Gibbs sampler
numsamp = 50

# randseed is used to initialize the Gibbs sampler random number generator
randseed = 194582

# This command will run the standard LDA model
#
(phi,theta,sample) = deltaLDA(docs,alpha,beta,numsamp,randseed)

# This command will initialize the Gibbs sampler from a user-supplied sample
#
#(phi,theta,sample) = deltaLDA(docs,alpha,beta,numsamp,randseed,init=sample)

# This command will run standard LDA, but show Gibbs sampler output
# ("Gibbs sample X of Y")
#
#(phi,theta,sample) = deltaLDA(docs,alpha,beta,numsamp,randseed,verbose=1)

# These commands will run deltaLDA
# (use different alpha vectors for different docs, depending on value of f)
#
#delta_f = [0, 0, 0, 0, 1, 1]
#delta_alpha = array([[.1, .1, 0],[.1, .1, .1]])
#(phi,theta,sample) = deltaLDA(docs,delta_alpha,beta,numsamp,randseed,f=delta_f)




# theta is the matrix of document-topic probabilities
# (estimated from final sample)
# 
# theta = D x T
# theta[di,zj] = P(z=zj | d=di)
#
#print ''
#print 'Theta - P(z|d)'
#print str(theta)
#print ''

# phi is the matrix of topic-word probabilities 
# (estimated from final sample)
# 
# phi = T x W
# phi[zj,wi] = P(w=wi | z=zj)
#
#print ''
#print 'Phi - P(w|z)'
#print str(phi)
#print ''

# Since the simple documents we created and fed into deltaLDA exhibit such
# clearly divided word usage patterns, the resulting phi and theta
# should reflect these patterns nicely

pmatrix = dot(theta,phi)

s = 0.0
M = 0.0

for idx,line in enumerate(docs):
    M += len(line)
    for word in line:
        s += pmatrix[idx][word]

perplexity = math.exp(-s/M)
print perplexity
