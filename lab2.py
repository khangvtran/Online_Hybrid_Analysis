# lab 2: Analyze and plot scores
# Name: Mega Putra

import csv                  #for csv objects
import openpyxl             # to use excel files
import numpy as np          # for numpy

def readExcel( filename ) :
    '''accepts a filename and returns a tuple of 2 list of lists, one for hybrid and one for online scores'''
    try: 
        wb = openpyxl.load_workbook(filename)           # get a workbook object
        sheet = wb.get_sheet_by_name("Grades")          # get the current active sheet   
        
        list_H = list()
        list_O = list()
  
   
        #listO = list([cell for cell in sheet.rows[1] if cell.value == "O"])
        
        for i in range(0, sheet.max_row):
            if (sheet.cell(row = i + 1, column = 1).value) == "H" :
                Hlist = list()
                for cell in sheet.rows[i]:
                    Hlist.append(cell.value)
                list_H.append(Hlist) # .append(list([sheet.rows[i]]))          # append a list of cell values
            else :
                Olist = list()
                for cell in sheet.rows[i]:
                    Olist.append(cell.value)
                list_O.append(Olist) # .appendlist([sheet.rows[i]]))

        '''        
        print("Checking list_H")
        for rows in list_H:
            for cols in rows:
                print (cols, end = " ")
                # print(type(cols))
                # print ([i.value for i in cols])
            print()
        '''  
        print("Checking list_O")    
        for rows in list_O:
            for cols in rows:
                print (cols, end = " ")
            print()              

        
        return tuple([list_H, list_O])
            
    except FileNotFoundError as e:
        print(str(e))
        exit() #end the program if exception is triggered
    
def readCSV(   ) :
    pass
 
def readFile(   ) :
    pass
            
def analyze(   ) :
    pass

def main() :
    #(arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')
    #analyze(arrH, arrO)
    readExcel('data1.xlsx')

main()