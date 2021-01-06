# -*- coding: utf-8 -*-
"""
auther : Mina emad
Id     : 20170309
"""
import pandas as pd
import math 


def load_file(filename):
    dataSet=pd.read_csv(filename)
    dataSetLen=len(dataSet)
    carsdata=[]
    for i in range(0,dataSetLen):
        carsdata.append([dataSet.values[i,j] for j in range(0,7)])
    #price feature
    for i in range (0,dataSetLen):
        if carsdata[i][0]=='low':
            carsdata[i][0]=1
        if carsdata[i][0]=='med':
            carsdata[i][0]=2
        if carsdata[i][0]=='high':
            carsdata[i][0]=3
        if carsdata[i][0]=='vhigh':
            carsdata[i][0]=4
      #maintance price feature
    for i in range (0,dataSetLen):
        if carsdata[i][1]=='low':
            carsdata[i][1]=1
        if carsdata[i][1]=='med':
            carsdata[i][1]=2
        if carsdata[i][1]=='high':
            carsdata[i][1]=3
        if carsdata[i][1]=='vhigh':
            carsdata[i][1]=4
      # no. of doors feature
    for i in range (0,dataSetLen):
        if carsdata[i][2]=='2':
            carsdata[i][2]=2
        if carsdata[i][2]=='3':
            carsdata[i][2]=3
        if carsdata[i][2]=='4':
            carsdata[i][2]=4
        if carsdata[i][2]=='5more':
            carsdata[i][2]=5
     # capacity feature
    for i in range (0,dataSetLen):
        if carsdata[i][3]=='2':
            carsdata[i][3]=2
        if carsdata[i][3]=='4':
            carsdata[i][3]=4
        if carsdata[i][3]=='more':
            carsdata[i][3]=5
    # lug feature
    for i in range (0,dataSetLen):
        if carsdata[i][4]=='small':
            carsdata[i][4]=1
        if carsdata[i][4]=='med':
            carsdata[i][4]=2
        if carsdata[i][4]=='big':
            carsdata[i][4]=3
    #safty
    for i in range (0,dataSetLen):
        if carsdata[i][5]=='low':
            carsdata[i][5]=1
        if carsdata[i][5]=='med':
            carsdata[i][5]=2
        if carsdata[i][5]=='high':
            carsdata[i][5]=3  
    return(carsdata)

def clculate_distance(traindata,test):
    diff_list=[]
    sumtion=0.0
    distance=0.0
    dis_list=[]
    for i in range(0,len(traindata)):
        for j in range (0,len(test)):
            x1=float(traindata[i][j])
            x2=float(test[j])
            diff=x2-x1
            sqr_diff=diff**2
            diff_list.append(sqr_diff)
        sumtion=sum(diff_list)
        distance=math.sqrt(sumtion)
       # print(distance)
        dis_list.append((distance,traindata[i][6]))
        diff_list.clear()
    return dis_list


def find_nearest(dis):
    nearest=[]
    for i in range(0,5):
        nearest.append(dis[i])
    return nearest

            
def voting(classes):
    clsFreq=[]
    cls=set()
    for c in classes:
        cls.add(c)
    my_cls=list(cls)
    count=0
    for i in range(0,len(my_cls)):
        for j in range(0,len(classes)):
            if my_cls[i]==classes[j]:
                count=count+1
        clsFreq.append((my_cls[i],count))
        count=0
    clsFreq.sort()
    sortCls=[]
    for x,y in clsFreq:
        sortCls.append(x)
    resCls=sortCls[-1]
    return (resCls)


def calculate_accurcy(test,orgTest):
    count=0
    for i in range (0,len(test)):
        if test[i][6]==orgTest[i][6]:
            count=count+1
    return (count/len(orgTest))*100

def main():
    cars_data= load_file("car.data.csv")
    data_Set_Length=len(cars_data)

    print(cars_data)

    test_Data=[]
    train_Data=[]
    training_Data_Size=int(.75 * data_Set_Length)
    for i in range(0, training_Data_Size):
        train_Data.append([cars_data[i][j] for j in range(0, 7)])
    for i in range (training_Data_Size, data_Set_Length):
        test_Data.append([cars_data[i][j] for j in range(0, 6)])
    for row in test_Data:
        disstance= clculate_distance(train_Data, row)

        disstance.sort()

        nearest= find_nearest(disstance)
       #print(nearest)
        classes=[]
        for x,y in nearest:
            classes.append(y)
        expCls= voting(classes)
       # print(expCls)
        row.append(expCls)
    originalTest=[]
    #print(disstance)
    for i in range (training_Data_Size, data_Set_Length):
        originalTest.append([cars_data[i][j] for j in range(0, 7)])
    accurcy= calculate_accurcy(test_Data, originalTest)
    print(test_Data)
   # print(originalTest)
    print("accurcy:",round(accurcy,4),"%")
if __name__ =='__main__':
    main()
