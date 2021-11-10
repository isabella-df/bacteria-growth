#importing libraries

import numpy as np
import matplotlib.pyplot as plt
import os.path


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
        if row[0]<=10 or row[0]>=60:
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

#print(dataStatistics(data, "Rows"))
def dataPlot(data):
    #sorting data according to temperature
    srt = np.argsort(data[:,0])
    switch = srt[::-1]
    data = data[switch]
    #plotting the bar    
    salmonella=0
    bacillus=0
    listeria=0
    brocothrix=0
    for i in data:
        if i[2] ==1:
            salmonella=salmonella+1
        if i[2] ==2:
            bacillus=bacillus+1
        if i[2] ==3:
            listeria=listeria+1
        if i[2] == 4:
            brocothrix=brocothrix+1
    dataPoints = {'Salomenlla enterica':salmonella,"Bacillus cereus":bacillus, "Listeria":listeria, "Brocothrix thermosphacta":brocothrix}
    bacteriaNames = list(dataPoints.keys())
    bacteriaNumbers = list(dataPoints.values())
    plt.bar(bacteriaNames, bacteriaNumbers, color ='maroon', width = 0.4)
    plt.xlabel("Bacteria names")
    plt.ylabel("No. of bacteria")
    plt.title("Amount of bacteria in experiment")
    plt.show()   
    #plotting the scatter
    Temperature1=[]
    Growth1=[]
    Temperature2=[]
    Growth2=[]
    Temperature3=[]
    Growth3=[]
    Temperature4=[]
    Growth4=[]
    for i in data:
        if i[2]==1:
           Temperature1.append(i[0])
           Growth1.append(i[1])
        if i[2]==2:
           Temperature2.append(i[0])
           Growth2.append(i[1])
        if i[2]==3:
           Temperature3.append(i[0])
           Growth3.append(i[1])
        if i[2]==4:
           Temperature4.append(i[0])
           Growth4.append(i[1])
    plt.plot(Temperature1,Growth1, 'r-',label='Salmonella')
    plt.plot(Temperature2,Growth2,'b-',label='Bacillus')
    plt.plot(Temperature3,Growth3,'g-',label='Listeria')
    plt.plot(Temperature4,Growth4,'y-',label='Brocothrix')
    plt.xlabel('Temperature')
    plt.ylabel('Growth Rate')
    plt.xlim(10,60)
    plt.ylim(0, 1)
    plt.title('Growth rate vs Temp')
    plt.legend(loc="upper right")
    plt.show()
    #print(np.sort(Temperature1))
    #print(Temperature2)
    #print(Temperature3)
    #print(Temperature4)
   # print(data)
#print(dataPlot(data))
#print(data)
#print(dataStatistics(data,'Mean Temperature'))
def print_menu():
    print(20*"-","Welcome to the action menu!",20*"-")
    print("1. Load Data")
    print("2. Filter Data")
    print("3. Display Statistics")
    print("4. Generate Plots")
    print("5. Quit")
    print (67*"-")

data=[]
dataEmpty=[]
#data and dataEmpty are empty arrays where data will no longer be empty if data is loaded successfully.
loop=True



#
while loop:
    #prints action menut
    print_menu()
    selection = int(input("Please select a number (1-5) from above:"))
    if selection==1:
        print("Load Data has been selected")
        filename=input('Please enter the name of the file you wish to use: ')
        
        #prints error if file can not be found, asks for valid file input
        while not(os.path.isfile(filename)):
            try:
                filename = input('File not found. Please input valid filename:')
                data=dataLoad(filename)
            except ValueError:
                pass        
        data=dataLoad(filename)
        print('Data Loaded successfully!')
                
    elif selection==2:
        if np.array_equal(data,dataEmpty):
#If data = dataEmpty, data has not been loaded and the functon will loop back to original menu.  
            print('Error please load data first!')
        else:
            print('Data Filter has been selected')
            #filter by bacteria type
            x21 = input("Would you like to filter by bacteria type: ")
            while ((x21.lower()!='yes') and (x21.lower()!='no')):
                try: 
                    x21=input('Error, please input yes or no:')
                except ValueError:
                    pass
            #carry out function when yes        
            if x21.lower() == "yes":
                print("Bacteria 1 corresponds to Salmonella enterica.")
                print("Bacteria 2 corresponds to Bacillus cereus.")
                print("Bacteria 3 corresponds to Listeria.")
                print("Bacteria 4 corresponds to Brochothrix thermosphacta.")
                #make bacteria input an integer
                bacteria = int(input("What numerical value of bacteria would you like to filter the data to: "))
                #an empty array with arbitrary values inorder to stack
                data1 = [-1,-1,-1]
                #if a number that is not an integer between 1-4 is entered then we print an error message
                while (bacteria!=1 and bacteria!=2 and bacteria!=3 and bacteria!=4):
                    try:
                        bacteria=int(input('Error! Please input  an integer value from 1-4!:'))
                    except ValueError:
                        pass
                for x in data:
                    if x[2] == bacteria:
                        data1=np.vstack((data1,x))
                print('Bacteria Filter Applied')
                data = data1[1:,:]
            if x21.lower() == "no":
                pass
            
            #filtering by growth rate
            
            
            
            #print(data1)
            #print(data)
    elif selection==3:
        if np.array_equal(data,dataEmpty):
           print('Error please load data first!')
        else:
            print("Display Statistics has been selected")
            #needs another option menu to have an input for statistic
           # print(dataStatistics(data,statistic))
    elif selection==4:
        if np.array_equal(data,dataEmpty):
           print('Error please load data first!')
        else:
            print(dataPlot(data))        
    elif selection==5:
        print("Quit has been selected")
        loop=False 
    else:
        print("Please choose a number from 1-5. Press any key to try again.")
#print(data)