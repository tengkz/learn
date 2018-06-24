#!/usr/bin/python
#coding:utf-8
"""
Created on Thu Feb 16 15:51:52 2017

@author: hztengkezhen
"""

import numpy as np

class HMM:
    def __init__(self,Ain,Bin,pin):
        self.A = np.array(Ain)
        self.B = np.array(Bin)
        self.pi = np.array(pin)
        self.istate = self.A.shape[0]
        self.ostate = self.B.shape[1]
        
    def printhmm(self):
        print "="*50
        print "HMM content: istate = ",self.istate,",ostate = ",self.ostate
        for i in xrange(self.istate):
            if i==0:
                print "hmm.A  ",self.A[i,:],"  hmm.B  ",self.B[i,:]
            else:
                print "       ",self.A[i,:],"         ",self.B[i,:]
        print "hmm.pi ",self.pi
        print "="*50
        
    def forwardScale(self,T,O,alpha,scale,pprob):
        """Forward algorithm.

        To overcome underfitting, we use parameter 'scale' to
        record normalization coeffieients. Remember alpha and 
        beta should have same scale at same pos.
        """
        scale[0] = 0.0
        
        for i in xrange(self.istate):
            alpha[0,i] = self.pi[i]*self.B[i,O[0]]
            scale[0] += alpha[0,i]
        for i in xrange(self.istate):
            alpha[0,i] /= scale[0]
        
        for t in xrange(T-1):
            scale[t+1] = 0.0
            for j in xrange(self.istate):
                s = 0.0
                for i in xrange(self.istate):
                    s += alpha[t,i]*self.A[i,j]
                alpha[t+1,j] = s*self.B[j,O[t+1]]
                scale[t+1] += alpha[t+1,j]
            for j in xrange(self.istate):
                alpha[t+1,j] /= scale[t+1]
        
        for t in xrange(T):
            pprob[0] += np.log(scale[t])
    
    def backwardScale(self,T,O,beta,scale):
        """Backward algorithm.

        To overcome underfitting, we use parameter 'scale' to 
        record normalization coefficients. Remember alpha and 
        beta should have same scale at same pos.
        """
        for i in xrange(self.istate):
            beta[T-1,i] = 1.0
        
        for t in xrange(T-2,-1,-1):
            for i in xrange(self.istate):
                s = 0.0
                for j in xrange(self.istate):
                    s += self.A[i,j]*self.B[j,O[t+1]]*beta[t+1,j]
                beta[t,i] = s/scale[t+1]
    
    def gamma(self,T,alpha,beta,gamma):
        """Get gamma.
        
        Probability of state i at time t.
        """
        for t in xrange(T):
            denominator = 0.0
            for j in xrange(self.istate):
                gamma[t,j] = alpha[t,j]*beta[t,j]
                denominator += gamma[t,j]
            for i in xrange(self.istate):
                gamma[t,i] = gamma[t,i]/denominator
    
    def epsilon(self,T,O,alpha,beta,gamma,epsilon):
        """Get epsilon. 
        
        Probability of transform from state i to 
        state j at time t.
        """
        for t in xrange(T-1):
            s = 0.0
            for i in xrange(self.istate):
                for j in xrange(self.istate):
                    epsilon[t,i,j] = alpha[t,i]*beta[t+1,j]*self.A[i,j]*self.B[j,O[t+1]]
                    s += epsilon[t,i,j]
            for i in xrange(self.istate):
                for j in xrange(self.istate):
                    epsilon[t,i,j] /= s
    
    def BaumWelch(self,L,T,O,alpha,beta,gamma):
        """BaumWelch algorithm.

        For learning process of hmm, use EM algorithm.
        Output lambda given only observed sequence.
        """
        #probf should be fixed in function, so it's a mutable list instead of a immutable float
        DELTA = 0.01; rnd = 0; flag = 1; probf = [0.0]
        delta = 0.0; deltaprev = 0.0; probprev = 0.0; ratio = 0.0; deltaprev = 10e-70
        
        epsilon = np.zeros((T,self.istate,self.istate))
        pi = np.zeros((T),np.float)
        denominatorA = np.zeros((self.istate),np.float)
        denominatorB = np.zeros((self.istate),np.float)
        numeratorA = np.zeros((self.istate,self.istate),np.float)
        numeratorB = np.zeros((self.istate,self.ostate),np.float)
        scale = np.zeros((T),np.float)
        
        while True:
            probf[0] = 0
            
            #E step
            for l in xrange(L):
                self.forwardScale(T,O[l],alpha,scale,probf)
                self.backwardScale(T,O[l],beta,scale)
                self.gamma(T,alpha,beta,gamma)
                self.epsilon(T,O[l],alpha,beta,gamma,epsilon)
                for i in xrange(self.istate):
                    pi[i] += gamma[0,i]
                    for t in xrange(T-1):
                        denominatorA[i] += gamma[t,i]
                        denominatorB[i] += gamma[t,i]
                    denominatorB[i] += gamma[T-1,i]
                    
                    for j in xrange(self.istate):
                        for t in xrange(T-1):
                            numeratorA[i,j] += epsilon[t,i,j]
                    for k in xrange(self.ostate):
                        for t in xrange(T):
                            if O[l][t] == k:
                                numeratorB[i,k] += gamma[t,i]
            
            #M step
            for i in xrange(self.istate):
                self.pi[i] = 0.001/self.istate+0.999*pi[i]/L
                for j in xrange(self.istate):
                    self.A[i,j] = 0.001/self.istate+0.999*numeratorA[i,j]/denominatorA[i]
                    numeratorA[i,j] = 0.0
                for k in xrange(self.ostate):
                    self.B[i,k] = 0.001/self.istate + 0.999*numeratorB[i,k]/denominatorB[i]
                    numeratorB[i,k] = 0.0
                pi[i], denominatorA[i], denominatorB[i] = 0.0,0.0,0.0
            
            if flag==1:
                flag = 0
                probprev = probf[0]
                ratio = 1
                continue
            
            delta = probf[0]-probprev
            ratio = delta/deltaprev
            probprev = probf[0]
            deltaprev = delta
            rnd+=1
            
            if ratio <= DELTA:
                print "num iteration ",rnd
                break

    def viterbi(self,O):
        """Viterbi algorithm.

        For inference process of hmm, 
        output most likely state sequence given lambda and output sequence.
        """
        T = len(O)
        theta = np.zeros((T,self.istate),np.float)
        phi = np.zeros((T,self.istate),np.float)
        ret = np.zeros(T,np.int)

        for i in xrange(self.istate):
            theta[0,i] = self.pi[i]*self.B[i,O[0]]  
            phi[0,i] = 0

        for t in xrange(1,T):
            for i in xrange(self.istate):
                theta[t,i] = self.B[i,O[t]]*np.array([theta[t-1,j]*self.A[j,i] for j in xrange(self.istate)]).max()
                phi[t,i] = np.array([theta[t-1,j]*self.A[j,i] for j in xrange(self.istate)]).argmax()
        prob = theta[T-1,:].max()
        ret[T-1] = theta[T-1,:].argmax()

        for t in xrange(T-2,-1,-1):
            ret[t] = phi[t+1,ret[t+1]]

        return ret,prob
                        
if __name__ == "__main__":
    #A = [[0.8125,0.1875],[0.2,0.8]]
    #B = [[0.875,0.125],[0.25,0.75]]
    #pi = [0.5,0.5]
    #hmm = HMM(A,B,pi)
    #
    #O = [[1,0,0,1,1,0,0,0,0],
    #     [1,1,0,1,0,0,1,1,0],
    #     [0,0,1,1,0,0,1,1,1]]
    #L = len(O)
    #T = len(O[0])
    #alpha = np.zeros((T,hmm.istate),np.float)
    #beta = np.zeros((T,hmm.istate),np.float)
    #gamma = np.zeros((T,hmm.istate),np.float)
    #hmm.BaumWelch(L,T,O,alpha,beta,gamma)
    #hmm.printhmm()
    #a,b = hmm.viterbi(O[0])
    #print a,b
    A = [[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]]
    B = [[0.5,0.5],[0.4,0.6],[0.7,0.3]]
    pi = [0.2,0.4,0.4]
    hmm = HMM(np.array(A),np.array(B),np.array(pi))
    O = [0,1,0]
    a,b = hmm.viterbi(O)
    print a,b
