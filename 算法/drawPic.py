'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-05-11 08:20:45
LastEditTime: 2021-05-11 10:23:29
'''
import HeapSort
import InsertSort
import QuickSort
import matplotlib.pyplot as plt
import time
import random

import sys   
sys.setrecursionlimit(10000) #设置递归值

Qtime_ms=[0]  # 列表用于存储快速排序所需要时间
Itime_ms=[0]  # 插入排序所用时间
Htime_ms=[0]  # 堆排序所用时间

N=[0,1000,2000,3000,4000]


for i in N[1:]:
    # random_list=random.sample(range(1,6000),i)
    random_list = [random.uniform(1.0, i) for i in range(i)]
    # print(random_list)
    # 插入排序 
    start_time=time.time()
    Iarray=InsertSort.insertion_sort(random_list)  # 插入排序
    end_time=time.time()
    cost=end_time-start_time
    Itime_ms.append(cost*1000)  # 以ms毫秒为单位，所以乘1000

    # 堆排序
    start_time=time.time()
    Harray=HeapSort.HeapSort(random_list)  # 堆排序
    end_time=time.time()
    cost=end_time-start_time
    Htime_ms.append(cost*1000)
    
    # 快速排序
    start_time=time.time()
    Qarray=QuickSort.quick_sort(random_list,0,len(random_list)-1)
    end_time=time.time()
    cost=end_time-start_time
    Qtime_ms.append(cost*1000)


print(Itime_ms)


plt.plot(N,Qtime_ms,"b-",linewidth=2,markersize=12,label="quick sort")
plt.plot(N,Htime_ms,"g-",linewidth=2,markersize=12,label="heap sort")
plt.plot(N,Itime_ms,"y-",linewidth=2,markersize=12,label="insert sort")


plt.xlabel("size of n")
plt.xlabel("time(ms)")
plt.legend(loc="upper left")
plt.show()




    

    




