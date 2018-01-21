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
        raise SystemExit("System Exit: Unable to open xls file.")

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
        raise SystemExit("System Exit: Unable to open csv file.")
        

def readFile(*args) :
    listH = list()
    listO = list()
    for fileName in args:
        if ".xlsx" in fileName:
            temp = readExcel(fileName)
            [listH.append(record) for record in temp[0]]
            [listO.append(record) for record in temp [1]]
        elif ".csv" in fileName:
            temp = readCSV(fileName)
            [listH.append(record) for record in temp[0]]
            [listO.append(record) for record in temp [1]]
            
    arrH = np.array(listH)
    arrO = np.array(listO)
    return(tuple([arrH, arrO]))


(arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')


totalPoints = 519
sucessCountH = sum(100 * arrH.sum(1) / totalPoints >= 70)
totalH = arrH.shape[0]
sucessRateH = round(100 * sucessCountH/totalH, 2)
sucessCountO = sum(100 * arrO.sum(1)/totalPoints >= 70)
totalO = arrO.shape[0]
sucessRateO = round(100 * sucessCountO/totalO, 2)




def analyze(arrH, arrO):
    print("*** Analysis for Hybrid v.s online class ***", "\n")
    
    # Measuring sucess Rate for O and H
    totalPoints = 519
    sucessCountH = sum(100 * arrH.sum(1) / totalPoints >= 70)
    totalH = arrH.shape[0]
    sucessRateH = round(100 * sucessCountH/totalH, 2)
    
    sucessCountO = sum(100 * arrO.sum(1)/totalPoints >= 70)
    totalO = arrO.shape[0]
    sucessRateO = round(100 * sucessCountO/totalO, 2) 
    
    print("- The sucess rate for hybrid classes is %.2f" %(sucessRateH))
    print("- The sucess rate for online classes is %.2f" %(sucessRateO))
    


def main() :
    (arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')
    analyze(arrH, arrO)

main()

