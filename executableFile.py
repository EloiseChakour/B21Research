#Import my files

import importingFiles as imp
import DiversityIndices as ent


#Import relevant libraries

import numpy as np
#from openpyxl import load_workbook
import xlsxwriter


#Gets the name of the excel file and the sheet from the user
def userInfo():
    fileName = input("Name of file (without .xlsx) in single quotes ")
    relevantSheet = 'Sheet' + input("Number of sheet in single quotes ")
    size = input("Number of classes ")
    
    return fileName, relevantSheet, size

#Calculates Shanon Entropy
def calculateShanonEntropy(allData):
    shanonEntropies = np.zeros((size, 2), dtype = float)
    for i in range(size):
        shanon = ent.shanon(imp.reshaping(allData, i))
        shanonEntropies[i, 1] = shanon
        shanonEntropies[i, 0] = int(allData[i, 0])
    
    return shanonEntropies

#Calculates Simpson Entropy  
def calculateSimpsonEntropy(allData):
    simpsonEntropies = np.zeros((size, 2), dtype = float)
    for i in range(size):
        simpson = ent.shanon(imp.reshaping(allData, i))
        simpsonEntropies[i, 1] = simpson
        simpsonEntropies[i, 0] = int(allData[i, 0])
    
    return simpsonEntropies

#Gets parameters from user info
#fileName, sheet, size = userInfo()

#Static parameters for testing
fileName = 'F15_Math'
sheet = 'Sheet1'
size = 62

#Gets all data
fullData = imp.reshapeData(imp.loadData(fileName, sheet), size)

#Calculates entropies
shanon = calculateShanonEntropy(fullData)
simpson = calculateSimpsonEntropy(fullData)



def saveIndex(array, nameOfFunction):
    
    name = str(nameOfFunction) + "_" +fileName
    
    workbook = xlsxwriter.Workbook(name + ".xlsx")
    worksheet = workbook.add_worksheet()
    
    worksheet.write('A' + str(1), "Course Code")
    worksheet.write('B' + str(1), nameOfFunction + " Index")
    for i in range(2, len(array)):
        worksheet.write('A'+ str(i), "Math " + str(int(array[i, 0])))
        worksheet.write('B' + str(i), array[i, 1])

    workbook.close()    




saveIndex(shanon, "Shanon")
saveIndex(simpson, "Simpson")
