#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:46:13 2021

@author: ashishbansal
"""

my_list=['ram',22,'google']

my_tup=('ram',22,'google')

type(my_tup)

my_list[0]

my_tup[0:2]+['delhi','india']

my_tup[0]='sham'


name,empid,com,loc=my_tup
com


my_tup1='ram','sunil'

type(my_tup1)

my_tup1


my_list1=list(my_tup)

my_list1[0]='sham'

my_tup2=tuple(my_list1)


my_list4=[('ram',22,'google'),('sham',34,'apple'),('raj',43,'microst')]

my_list4


for item in my_list4:
    print(item[0:2])



dict1={['ashish','vipul']:['sunil','assshish']}


dict1=dict()

dict1={1:'sunil'}


dict1[0]

dict1={'name':'sunil','emp':222,'loc':'google','emp':777}

dict1['name']='vipul'

dict1

keys are unique 

datatypes 

int  ok
float ok
boolean ok
list not ok  muta
tupple ok
dict not ok  muta


my_dict={{1:'amit'}:'amit'}

# mutable datatypes are not allowed in dict keys 

my_dict={([1,2]):'amit'}

# values 


dict1.keys()
dict1.values()
dict1.items()



for item in dict1:
    print(dict1[item])

for item in dict1.values():
    print(item)
    
    
for item in dict1.items():
    print(item)
    
    