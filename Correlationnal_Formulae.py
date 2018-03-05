#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:41:52 2018

@author: eloisechakour
"""
import importingFiles as iF


import numpy as np
#from openpyxl import load_workbook


def smallReshapeData(indexSheet, size):
    
    Array = []

    for i in range(size):
        b = 'B' + str(2+i)
        Array.append(indexSheet[b].value)
    
    return Array

#x = [1, 1, 1, 1, 1, 2]
#y = [1 ,2, 3, 4, 5, 6]

def pearson(size, arrayOfDivIndices, arrayOfCompVar):
    xAvg = np.mean(arrayOfDivIndices)
    yAvg = np.mean(arrayOfCompVar)
    xStd = np.std(arrayOfDivIndices)
    yStd = np.std(arrayOfCompVar)
    
    numerator = 0
    for i in range(size):
        numerator += (arrayOfDivIndices[i] - xAvg)*(arrayOfCompVar[i] - yAvg)
    
    denom = (size-1)*xStd*yStd
    
    p = numerator/denom
    
    return p

#p = pearson(6, x, y)
#print(p)






























