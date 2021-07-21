# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:42:58 2021

@author: dkjua
"""
i=0
import random
y=random.randint(1,10)
print("y is "+str(y))
z=0
while i<5 and z<1:
    x=input('數字(1-10)?')
    x=int(x)
    if x ==y: 
        print('you win')
        z=1
    else:
        print('no')
        i=i+1
if z==0:
    print('you lose')        
        