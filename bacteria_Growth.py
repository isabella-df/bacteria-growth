
import pandas as pd
import numpy as np

#why do birds suddenly appearrrrrr

def dataLoad(filename):
    file = open(filename, 'r')
    data=[]
    for row in file:
        data.append([float(x) for x in row.split(' ')])
    return data
print(dataLoad('testforreals.txt'))