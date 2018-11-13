# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:06:37 2018

@author: ktm
"""
#%%
var1=10

class Human():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def wave(self):
        print("손을 흔든다")

class Dog():
    def walk(self):
        return "걷는다"
    
    def eat(self):
        print("먹는다")
    
    def wag(self):
        print("꼬리를 흔든다")
#%%

def sum(a,b):
    return a+b

def minus(a,b):
    return a-b