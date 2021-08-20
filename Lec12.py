#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:18:20 2021

@author: ashishbansal
"""

my_list=[10,20,30]


{x*2:x for x in my_list if x ==20}
x

names=['ram','sham','vipul']

roll=[1,2,3]


zip1=list(zip(names,roll))

name1,roll1=zip(*zip1)

name1
roll1


def sum1(x,y=100):
    return x+y,x-y

sum1(20)


x=lambda x,y=100:(x+y,x-y)

x(20)



x=[1,2,3,4]


list(map(lambda x:x**3,x))


for i in range(0,10):
    print(i,end="")

