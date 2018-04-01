#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:41:52 2018

@author: eloisechakour
"""
#import importingFiles as iF


import numpy as np
#from openpyxl import load_workbook

#Takes as input the excel sheet and outputs an array containing the diversity indices of each class.  
def smallReshapeData(indexSheet, size):
    
    Array = []

    for i in range(size):
        b = 'B' + str(2+i)
        Array.append(indexSheet[b].value)
    
    return Array

#Test Arrays
x = [1, 2, 3, 4, 5, 6]
y = [1 ,2, 3, 4, 5, 6]
z = [6, 5, 4, 3, 2, 1]

#Takes as input the size of the array (i.e. how many classes), an array of the diversity indices for each class and an array containing the variable we want to compare it to. The function outputs the Pearson Correlation Index. 

def pearson(size, arrayOfDivIndices, arrayOfCompVar):
    #Calculate relevant values for both the diversity indices and the comparison values.
    xAvg = np.mean(arrayOfDivIndices)
    yAvg = np.mean(arrayOfCompVar)
    xStd = np.std(arrayOfDivIndices)
    yStd = np.std(arrayOfCompVar)
    
    #Find the numerator of the Pearson Index.
    numerator = 0
    for i in range(size):
        numerator += (arrayOfDivIndices[i] - xAvg)*(arrayOfCompVar[i] - yAvg)
    
    #Find the denominator of the Pearson Index.
    denom = (size-1)*xStd*yStd
    
    #Calculate the Pearson Index.
    p = numerator/denom
    
    return p

#p = pearson(6, x, y)
#print(p)

"""TODO: make something to check for and deal with repeated values.""" 

#Takes as input the size of the array (i.e. how many classes), an array of the diversity indices for each class and an array containing the variable we want to compare it to. The function outputs the Kendall Correlation Index.

def kendall(size, arrayOfDivIndices, arrayOfCompVar):
    #Create counters to order the arrays.
    counter1 = 0
    counter2 = 0
    
    #Create arrays that will contain ordered values.
    orderedArrayInd = [0 for j in range(size)]
    orderedArrayComp = [0 for m in range(size)]
    
    #Order the diversity indices.
    i=0
    for i in range(size):
        if len(arrayOfDivIndices) != 0:
            if arrayOfDivIndices[i] == max(arrayOfDivIndices):
                orderedArrayInd[i] = counter1
                arrayOfDivIndices = np.delete(arrayOfDivIndices, i)
                counter1 += 1
                #print (len(arrayOfDivIndices))
    
    #Order the comparison value.  
    k=0
    for k in range(size):
        if len(arrayOfDivIndices) != 0:
            if orderedArrayComp[k] == max(arrayOfCompVar):
                orderedArrayComp[k] = counter2
                orderedArrayComp = np.delete(orderedArrayComp, k)
                counter2 += 1
            
    #Create counters for concordant and discordant ordering of variables.         
    concordant = 0
    discordant = 0
    
    #Count how many orderes are concordant and discordant. 
    for p in range(size):
        if orderedArrayInd[p] == orderedArrayComp[p]:
            concordant += 1
            #print (concordant)
        else:
            discordant +=1
        
    #Calculate the Kendall Correlation Coefficient. 
    t = 2*(concordant - discordant)/float((size*(size-1)))

    
    return t


t = kendall(6, x, y)
print ("kendall")
print (t)

#Takes as input the size of the array (i.e. how many classes), an array of the diversity indices for each class and an array containing the variable we want to compare it to. The function outputs the Spearman Correlation Index.
    
def spearman(size, arrayOfDivIndices, arrayOfCompVar):
    #Create arrays for ordered values.
    nArrayOfDivIndices = np.zeros(size)
    nArrayOfCompVar = np.zeros(size)
    
    #Create counters to represent the order of the values.
    counter1 = 0
    counter2 = 0
    
    #Create the ordered values of the diversity indices array.
    counterA = 0
    for counterA in range(size):
        for i in range(size):
            if max(arrayOfDivIndices) == arrayOfDivIndices[i]:
                nArrayOfDivIndices[i] = counter1
                arrayOfDivIndices[i] = -1000000
                counter1 += 1
                #print (counter1)
            if counter1 >= size-1:
                #print (nArrayOfDivIndices)
                break
            counterA +=1
    
    #Create the ordered values of the comparison value.
    counterB=0
    for counterB in range(size):
        for j in range(size):
            if max(arrayOfCompVar) == arrayOfCompVar[j]:
                nArrayOfCompVar[j] = counter2
                arrayOfCompVar[j] = -1000000
                counter2 += 1
                #print(counter2)
            if counter2 >= size-1:
                #print (nArrayOfCompVar)
                break
            counterB += 1
        
 
    
    #Find the numerator of the Spearman Index.
    pNum = 0
    for k in range(size):
        d = nArrayOfDivIndices[k] - nArrayOfCompVar[k]
        pNum += 6*d**2
    
    #Denominator of the Spearman Index.
    pDenom = size**3 - size
    
    #Calculate the fraction of the Spearman Index.
    p = float(pNum)/float(pDenom)
    
    return (1-p)

spearman = spearman(6, x, z)
print ("Spearman")
print (spearman)




















