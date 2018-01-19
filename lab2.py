# lab 2: Analyze and plot scores
# Name: Khang Vinh Tran, Mega Putra


def readExcel(  ) :
    pass

def readCSV(fileName) :
    try:
        listO = list()
        listH = list()        
        with open(fileName, "r") as inFile:
            for row in inFile:
                temp = row.split(',')
                temp[-1] = temp[-1].replace("\n", "")
                if temp[0] == "O" : listO.append(temp[1:])
                elif temp[0] == "H" : listH.append(temp[1:])
        return(tuple([listH, listO]))
    except FileNotFoundError as e:
        print(str(e))
 
#a = readCSV("data2.csv")


def readFile(   ) :
    pass
            
def analyze(   ) :
    pass3


def main() :
    (arrH, arrO)= readFile('data1.xlsx', 'data2.csv','data3.csv')
    analyze(arrH, arrO)

#main()


"""
fileName = 'data2.csv'
try:
    with open(fileName, "r") as inFile:

        
        listO = list()
        listH = list()
        for row in inFile:
            temp = row.split(',')
            temp[-1] = temp[-1].replace("\n", "")
            if temp[0] == "O" : listO.append(temp[1:])
            elif temp[0] == "H" : listH.append(temp[1:])
        
        '''
        listO = [row.split(',')[1:] for row in inFile if row.split(',')[0] == "O"]
        inFile.seek(0)     # get back to head of file
        listH = [row.split(',')[1:] for row in inFile if row.split(',')[0] == "H"]
        '''
        print(listH)
        print(listO)
        
        #print(len(listO))
        #print(len(listO[0]))

        
except FileNotFoundError as e:
    print(str(e))
"""