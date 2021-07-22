# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:42:58 2021

@author: dkjua
"""
i=0
import random
y=random.randint(1,20)
z=0
while i<5 and z<1:
    x=input('數字(1-10)?')
    x=int(x)
    if x ==y: 
        print('you win')
        print('你玩了'+str(i+1)+'次')
        z=1
    else:
        print('no')
        i=i+1
        if x>y:
            print('太大')
        else:
            print('太小')
if z==0:
    print('you lose')
        
        