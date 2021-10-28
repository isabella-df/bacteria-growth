import numpy as np

def dataLoad(filename):
    file = open(filename, 'r')
    datawrong=[]
    for row in file:
        datawrong.append([float(x) for x in row.split(' ')])
    print(datawrong)
    t=0
    data=[]
    for row in datawrong:
        t=t+1
        if row[0]<10 and row[0]>60:
            row[0]=0
        if row[1]<0:
            row[1]=0
        if row[2]<1 or row[2]>4:
            row[2]=0
        for i in row:
            if i>0:
              np.row_stack(row, data)
            else:
               print('Error in row',t)  
            
                
    return data

print(dataLoad('testforreals.txt'))