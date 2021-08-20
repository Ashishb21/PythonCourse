#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:24:08 2021

@author: ashishbansal
"""

my_list=[1,2,3,4]

for item in my_list:
    print(item)
    
my_iter=iter(my_list)

next(my_iter)


def square(n):
    for i in range(n):
        yield n**3
        
for item in square(4):
    print(item)