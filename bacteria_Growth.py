# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:29:57 2021

@author: isabe
"""
import pandas as pd
import numpy as np

#why do birds suddenly appearrrrrr

def dataLoad(filename):
    file = open(filename, 'r')
    data = []
    for row in file:
        data.append([int(x) for x in row.split()])
    return data

print(dataLoad(test))