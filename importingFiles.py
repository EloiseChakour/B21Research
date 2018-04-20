import numpy as np
#import pandas as pd
from openpyxl import load_workbook

#Some useless stuff from early testing
"""
file = 'Reformatted_W16_Math_Data.xlsx'


W16 = pd.ExcelFile(file)

pW16 = W16.parse('Sheet1')



print(pW16)
"""
#Loads data from a data file in the same folder
#INSERT PATHS TO SIMPLIFY FILING EC
def loadData(nameOfFile, sheetName):
    wb = load_workbook('./'+ nameOfFile +'.xlsx')
    sheet = wb.get_sheet_by_name(sheetName)
    
    return sheet
    
#print(wb.get_sheet_names())



#print(sheet['A1'].value)


#Takes data and puts it into a useable form
def reshapeData(mySheet, size):
    Array = np.zeros((size, 12), dtype = int)

    for i in range(size):

        b = 'B' + str(4+i)
        if size > 0:
            #Checks for repeated values
            check = 'B' + str(3+i)
            if mySheet[b].value != mySheet[check].value:
                Array[i, 0] = mySheet[b].value
                c = 'C' + str(4+i)
                Array[i, 1] = mySheet[c].value
                d = 'D' + str(4+i)
                Array[i, 2] = mySheet[d].value
                e = 'E' + str(4+i)
                Array[i, 3] = mySheet[e].value
                f = 'F' + str(4+i)
                Array[i, 4] = mySheet[f].value
                g = 'G' + str(4+i)
                Array[i, 5] = mySheet[g].value
                h = 'H' + str(4+i)
                Array[i, 6] = mySheet[h].value
                I = 'I' + str(4+i)
                Array[i, 7] = mySheet[I].value
                j = 'J' + str(4+i)
                Array[i, 8] = mySheet[j].value
                k = 'K' + str(4+i)
                Array[i, 9] = mySheet[k].value
                l = 'L' + str(4+i)
                Array[i, 10] = mySheet[l].value
                #m = 'M' + str(4+i)
                #Array[i, 11] = mySheet[m].value
                n = 'N' + str(4+i)
                Array[i, 11] = mySheet[n].value
        
    #Converts the data to a list, to reshape the data more easily 
    totalList = []
    for i in range(len(Array)):
        testList = []
        if Array[i, 0] != 0:
            for j in range(12):
                testList.append(Array[i, j])
            totalList.append(testList)
    
    #This part of the code checks thtat there are no remaining repeated values.        
    newList = []      
    for k in range(len(totalList)):
        newList.append(totalList[k][0])
    
    newList.sort
    for counter in range(len(newList)):
        if counter > 0:
            if newList[counter] == newList[counter-1]:
                print("Error: still have repeated courses! Please fix the spreadsheet.")
                break
    
    #Converts the data back to an array 
    nArray = np.asarray(totalList) 
    
    return nArray

#Reshapes the data to put it into a for compatible with the entropy calculations
def reshaping(allData, index):
    array = []
    for i in range(0, len(allData[0])):
        array.append(allData[index, i]/100.0)
    
    return array 

"""
For testing purposes
"""

#mySheet = loadData('F15_Math', 'Sheet1')
#mySheet = loadData('Reformatted_W16_Math_Data', 'Sheet1')
#testArray = reshapeData(mySheet, 51)


