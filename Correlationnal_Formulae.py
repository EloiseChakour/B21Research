#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:41:52 2018

@author: eloisechakour
"""
#import importingFiles as iF


import numpy as np
#from openpyxl import load_workbook


def smallReshapeData(indexSheet, size):
    
    Array = []

    for i in range(size):
        b = 'B' + str(2+i)
        Array.append(indexSheet[b].value)
    
    return Array

x = [1, 2, 3, 4, 5, 6]
y = [1 ,2, 3, 4, 5, 6]

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

#TODO: make something to check for and deal with repeated values. 
def kendall(size, arrayOfDivIndices, arrayOfCompVar):
    
    counter1 = 0
    counter2 = 0
    
    orderedArrayInd = [0 for j in range(size)]
    orderedArrayComp = [0 for m in range(size)]
    
    i=0
    for i in range(size):
        if len(arrayOfDivIndices) != 0:
            if arrayOfDivIndices[i] == max(arrayOfDivIndices):
                orderedArrayInd[i] = counter1
                arrayOfDivIndices = np.delete(arrayOfDivIndices, i)
                counter1 += 1
                print len(arrayOfDivIndices)
        
    k=0
    for k in range(size):
        if len(arrayOfDivIndices) != 0:
            if orderedArrayComp[k] == max(arrayOfCompVar):
                orderedArrayComp[k] = counter2
                orderedArrayComp = np.delete(orderedArrayComp, k)
                counter2 += 1
            
            
    concordant = 0
    discordant = 0
    
    for p in range(size):
        if orderedArrayInd[p] == orderedArrayComp[p]:
            concordant += 1
            #print concordant
        else:
            discordant +=1
            
    t = 2*(concordant - discordant)/float((size*(size-1)))

    
    return t


t = kendall(6, x, y)

print t
























