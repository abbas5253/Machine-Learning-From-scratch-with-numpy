# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 00:39:42 2019

@author: Abbas Ismail(abbas.tel2342@gmail.com)
"""
import numpy as np

class LinearReg:
    
    def __init__(self,lr = 0.05,itr = 1000):
        self.lr = lr
        self.itr = itr
        self.m = 0
        self.n = 0
        self.cost_ = []
        
    def fit(self,X,Y):
       self.n = X.shape[0]
       self.m = X.shape[1]
       self.w = np.ones((self.m,1))
       self.b = 1
       for i in range(self.itr):
           m = X.shape[1]
           y_preds = np.dot(X,self.w)+self.b
           self.w = self.w - (self.lr/self.m)*np.dot(X.T,(y_preds-Y))
           self.b = (self.b - (self.lr/self.m)*(y_preds-Y))[0]
           cost = np.sum((y_preds-Y)**2)
           self.cost_.append(cost)
           
           
    def predict(self,X):
       return(np.dot(X,self.w)+self.b)      
      
        
class LogisticReg:
    
    def sigmoid(X):
        return (1/(1+np.exp(-X)))

    def __init__(self,lr=0.05,itr = 1000):
        self.lr = lr
        self.m = 0
        self.n = 0
        self.cost = []
        self.b = 0
        self.itr = itr

    def fit(self,X,Y):
        self.m = X.shape[1]
        self.n = X.shape[0]
        
        self.w  = np.ones((self.m,1))
        
        for i in range(itr):
            y_preds = sigmoid(np.dot(X,self.w)+b)
            w = w - (self.lr/self.m)*(np.dot(y_preds-Y,X.T))
            b = b - (self.lr/self.m)*(y_preds-Y)[0]
            cost = -(1/self.m)*(y_preds*np.log(Y) + (1-y_preds)*np.log(1-Y))
            self.cost.append(cost)
            
    def predict(self,X):
        return (sigmoid(np.dot(X,self.w)+self.b))
    
       
       
       
       