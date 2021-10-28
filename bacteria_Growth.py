import numpy as np

def dataLoad(filename):
    mat1=np.loadtxt(filename)
    #Made matrix from txt file
    t=0
    data=np.array([-1,-1,-1])
    #set data as an arbitrary array with same no of columns as matrix mat1
    for row in mat1:
    #for loop to go through the 3 elements of each row
        t=t+1
        datarowisvalid=True
#all below if statements set datarowisvalid=false if the values do not meet the given specifications e.g. GrowthRate is negative.
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
#takes every row where the datarowisvalid=true and stacks it in a matrix
            data=np.vstack((data,row))           
    return data[1:,:]
#print(dataLoad('testforreals.txt'))
data = dataLoad("test2.txt")

def dataStatistics(data, statistic):
    if statistic == 'Mean Temperature':
    #takes the mean of the 0th column     
        result = data[:,0].mean()
    if statistic == 'Mean Growth rate': 
        result = data[:,1].mean()
    if statistic == 'Std Temperature':
        result = data[:,0].std()
    if statistic == 'Std Growth rate':
        result = data[:,1].std()
    if statistic == 'Rows':
        result = len(data)
    if statistic == 'Mean Cold Growth rate':
    #coldData is a new array where all temps are less than 20    
        coldData = data[data[:,0]< 20]
    #gets the mean of the growth rate of the new array where all temps are less than 20    
        result = coldData[:,1].mean()
    if statistic == 'Mean Hot Growth rate':
        hotData = data[data[:,0]>50]
        result = hotData[:,1].mean()
    return result

print(dataStatistics(data, "Rows"))