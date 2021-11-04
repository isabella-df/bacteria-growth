import numpy as np

def dataLoad(filename):
    mat1=np.loadtxt(filename)
    t=0
    data=np.array([-1,-1,-1])
    for row in mat1:
        t=t+1
        datarowisvalid=True
        if row[0]<10 or row[0]>60:
           datarowisvalid=False
           print('Error in row',t,'Temperature')
        if row[1]<0:
            datarowisvalid=False
            print('Error in row',t,'Growth Rate')
        if row[2]<1 or row[2]>4:
            datarowisvalid=False
            print('Error in row',t,'Bacteria')
        if datarowisvalid:
            data=np.vstack((data,row))           
    return data[1:,:]
#print(dataLoad('testforreals.txt'))
def dataStatistics(data, Statistic):
    if Statistic=='Mean Temperature':
        calculation=data[:,0].mean()
        
    result=calculation
    return result