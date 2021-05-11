'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-04-26 22:06:03
LastEditTime: 2021-04-26 22:10:16
'''
import time
import random

def insertion_sort(array):
    for i in range(len(array)):
        cur_index = i
        while array[cur_index-1] > array[cur_index] and cur_index-1 >= 0:
            array[cur_index], array[cur_index-1] = array[cur_index-1], array[cur_index]
            cur_index -= 1
    return array
 
 
if __name__ == '__main__':
    """
    1. 简单测试
    """
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    print('排序前',array)
    start=time.time()
    print('排序后',insertion_sort(array))
    end=time.time()
    print("运行时间：",end-start)

    """
    2. 对100个数进行排序
    """
    # 随机生成100个整数
    list100=random.sample(range(1,200),100)
    print("未排序前",list100)
    start100=time.time()
    array_100=insertion_sort(list100)
    end100=time.time()
    print("排序后",array_100)
    print("运行时间：",end100-start100)

    """
    2. 对5000个数进行排序
    """
    # 随机生成100个整数
    list5000=random.sample(range(1,20000),5000)
    print("未排序前",list5000)
    start5000=time.time()
    array_5000=insertion_sort(list5000)
    end5000=time.time()
    print("排序后",array_5000)
    print("运行时间：",end5000-start5000)

    