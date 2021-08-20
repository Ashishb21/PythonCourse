#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:06:30 2021

@author: ashishbansal
"""

import numpy as np

my_list=[[1,2],[2,3]]

x=np.array(my_list)

x.shape

[1,2,3,1,1]

{1:3,2:1,3:1}

lis1t = [1,2,2,3,1,1]
print([number,count() for x,y in list1])

my_list=[1,2,3,4]
{1:1,2:4,3:9,4:16}


x=[[1],[2],[3]]

{x:x*x for x in my_list}

count(x)


x=['a','b','c','d','e']

out=[[]]

for item in x:
    out =out +[t+[item] for t in out]

["".join(x) for x in out]



a="aabaas"

x=list(a)


out=[[]]

for item in x:
    out =out+[t +[item]for t in out]

set([tuple(item) for item in out])





import collections

s="abccccdd"
ans = 0
for v in collections.Counter(s).itervalues():
    ans += v / 2 * 2
    if ans % 2 == 0 and v % 2 == 1:
        ans += 1