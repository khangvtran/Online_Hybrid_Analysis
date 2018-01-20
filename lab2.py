# lab 2: Analyze and plot scores
# Name: Khang Vinh Tran, Mega Putra

import openpyxl
import csv
import numpy as np


def readExcel(fileName) :
    try:
        listO = list()
        listH = list()
        wb = openpyxl.load_workbook(fileName)
        sheet = wb.active
        for row in sheet:
            temp = list()
            if (row[0].value == "H"):
                for cell in row[1:] : temp.append(cell.value)
                listH.append(temp)
            elif (row[0].value == "O"):
                for cell in row[1:] : temp.append(cell.value)
                listO.append(temp)
        return(tuple([listH, listO]))
    except FileNotFoundError as e:
        print(str(e))
        
#fileName = "data1.xlsx"
#a = readExcel(fileName)
#print(a)



def readCSV(fileName) :
    try:
        listO = list()
        listH = list()        
        with open(fileName, "r") as inFile:
            reader = csv.reader(inFile)
            for row in reader:
                if (row[0] == "H") : listH.append(list(map(float, row[1:])))
                elif (row[0] == "O") : listO.append(list(map(float, row[1:])))
            inFile.close()   # close the file
            return(tuple([listH, listO]))
    except FileNotFoundError as e:
        print(str(e))
 
#b = readCSV("data2.csv")
#print(b)

def readFile(*args) :
    listH = list()
    listO = list()
    for fileName in args:
        if ".xlsx" in fileName:
            print("XLSX")
            temp = readExcel(fileName)
            [listH.append(record) for record in temp[0]]
            [listO.append(record) for record in temp [1]]
        elif ".csv" in fileName:
            print("CSV")
            temp = readCSV(fileName)
            [listH.append(record) for record in temp[0]]
            [listO.append(record) for record in temp [1]]
            
    arrH = np.array(listH)
    arrO = np.array(listO)
    return(tuple([arrH, arrO]))

(arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')
print(arrH.shape)
print(arrH)
print(arrO.shape)
print(arrO)


def analyze(   ) :
    pass

'''
def main() :
    (arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')
    analyze(arrH, arrO)

#main()

'''