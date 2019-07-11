#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:33:27 2019

@author: kal @ Dilip Kalagolta (kalagodk@mail.uc.edu)

Add code summary below:
    Script counts number of lines in a file
    
"""

def simplecount(filename):
        n = 0
        for line in open(filename):
            n += 1
        print('Number of time steps ' + filename + ' = ', n)
        return n-1