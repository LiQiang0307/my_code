import time
import random

def quick_sort(array,low,high):
    if low<high:
        key_index=sub_sort(array,low,high)
        quick_sort(array,low,key_index) #递归前半部分
        quick_sort(array,key_index+1,high) #递归后半部分
    return array
 
 
 
def sub_sort(array,low,high):
    key=array[low]
    while low<high:
        while low<high and array[high]>=key:
            high-=1
        if low<high:
            array[low],array[high]=array[high],array[low]
        else:
            break
        while low<high and array[low]<key:
            low+=1
        if low<high:
            array[high], array[low] = array[low], array[high]
        else:
            break
    return low
 
if __name__=="__main__":

    """
    1. 简单测试
    """
    start=time.time()
    # print(start)
    array=[9,5,7,6,1,3,4,8,2]
    print("未排序前",array)
    array_result=quick_sort(array,0,len(array)-1)
    end=time.time()
    print("排序后",array_result)
    print("运行时间：",end-start)

    """
    2. 对100个数进行排序
    """
    # 随机生成100个整数
    list100=random.sample(range(1,200),100)
    print("未排序前",list100)
    start100=time.time()
    array_100=quick_sort(list100,0,len(list100)-1)
    end100=time.time()
    print("排序后",array_100)
    print("运行时间：",end100-start100)

    """
    2. 对5000个数进行排序
    """
    # 随机生成100个整数
    list5000=random.sample(range(1,10000),5000)
    print("未排序前",list5000)
    start5000=time.time()
    array_5000=quick_sort(list5000,0,len(list5000)-1)
    end5000=time.time()
    print("排序后",array_5000)
    print("运行时间：",end5000-start5000)



 