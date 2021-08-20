#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:22:57 2021

@author: ashishbansal
"""

class Person():
    company="apple"
    def __init__(self,empid,salary):
        self.empid=empid
        self.salary=salary
    
    def do_job(self):
        pass

person=Person(12,1222)
arjun=Person(22,933)

arjun.__dict__

person.id=20
person.name="sunil"

person.id

person.__dict__

karun=Person()

arjun=Person()

print(karun)
print(arjun.__dict__)
print(person)

Person.__dict__





karun.




