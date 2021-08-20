#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:43:26 2021

@author: ashishbansal
"""


print("hello")

try:
    1/0

except :
    print("exception occured")
    
else:
    print("no exception send email")

finally:
    print("this is finally block")
    
print("hello again")



import os 
import shutil

import Pathlib

curr_path=os.getcwd()

os.listdir(curr_path)

os.mkdir('test')

shutil.copy('lec9.py','./test/Lec9.py')



os.remove('./test/Lec9.py')


os.rmdir('test')

shutil.make_archive()



data="data.jpg"
my_path=os.path.join(os.getcwd(),data)

filename, filepath=os.path.split(my_path)

os.path.splitext(filepath)

import math



f=open('alice.txt')
print(f.read())
f.close()




with open('alice.txt',"r") as f:
    f.seek(10)
    print(f.tell())
    print(f.readlines())
    print(f.tell())

x[0:5]
# modes 

read 
write 
a) if file exits   ---> overriiden 
b) if file doesnot exits --> new file 
    
append 
a) if file exist --> append
    
b) if file doesnot exits --> new file


with open('alice2.txt',"a") as f:
    f.write("this is my new file4")


