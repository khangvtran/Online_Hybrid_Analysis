# lab 2: Analyze and plot scores
# Name: Khang Vinh Tran, Mega Putra

import openpyxl
import csv
import numpy as np
import matplotlib.pyplot as plt


def readExcel(fileName) :
    """
    read in one .xls file name
    return a tuple of 2 lists (Hybrid, Online) of lists (Scores)
    Handle exception if the file is not found, follow by system exit.
    """
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
    """
    read in one .csv file name
    return a tuple of 2 lists (Hybrid, Online) of lists (Scores)
    Handle exception if the file is not found, follow by system exit.
    """    
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
    """
    take in argument as a list of slx and csv files with unknown number of files
    return a tuple of two numpy array (Hybrid, Online)
    """
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


def analyze(arrH, arrO):
    """
    Compute Success rate for Hybrid and Online class
    Plot the histogram to present distribution of percentage of hybrid vs online
    Plot the lines show the time series of mean of assignment score of online vs hybrid
    """
    
    print("*** Analysis for Hybrid v.s online class ***", "\n")
    
    # Measuring success rate for Online and Hybrid
    totalPoints = 519
    
    percentageH = 100 * arrH.sum(1) / totalPoints
    successCountH = sum( percentageH >= 70)
    totalH = arrH.shape[0]
    successRateH = round(100 * successCountH/totalH, 2)
    
    percentageO = 100 * arrO.sum(1) / totalPoints
    successCountO = sum(percentageO >= 70)    
    totalO = arrO.shape[0]
    successRateO = round(100 * successCountO/totalO, 2) 
    
    print("- The success rate for hybrid classes is %.2f" %(successRateH))
    print("- The success rate for online classes is %.2f" %(successRateO))
    
    # Plotting Histogram to show distribution of Online and Hybrid 
    plt.hist((percentageH, percentageO), color=("teal", "firebrick"), label=("Hybrid","Online"), alpha=0.8, bins=10)
    plt.xticks(np.arange(0, 101, 5))
    plt.xlabel("Grade Percentage")
    plt.yticks(np.arange(0, 30, 2))
    plt.ylabel("Distribution")
    plt.title("Grade Distribution")    
    plt.legend(loc = "best")
    plt.show()
    
    
    # Compute, and plot the mean assignment grade
    numAssignment = 8
    meanAssignmentH = arrH.copy().mean(0)[ :numAssignment]
    meanAssignmentO = arrO.copy().mean(0)[ :numAssignment]
    assignment = np.arange(1, numAssignment+1)
    plt.plot(assignment, meanAssignmentH,
             assignment, meanAssignmentH, 'ro',
             label = "Hybrid")
    plt.plot(assignment, meanAssignmentO,
             assignment, meanAssignmentO, 'go',
             label = "Online")
    plt.legend(loc="best")
    plt.yticks(np.arange(8, 15, 0.5))
    plt.xlabel("Assignment")
    plt.ylabel("Average Grade of All Students")     
    plt.title("Assignment Grade Time Series")     
    plt.show()
    

def main() :
    (arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')
    analyze(arrH, arrO)

main()

