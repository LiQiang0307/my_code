'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-04-26 22:11:21
LastEditTime: 2021-04-26 22:13:27
'''
import random
import time

def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

if __name__ == '__main__':
    """
    1. 简单测试
    """
    a = [30,50,57,77,62,78,94,80,84]
    print ('排序前',a)
    x=HeapSort(a)
    print('排序后',x)

    """
    2. 对100个数进行排序
    """
    # 随机生成100个整数
    list100=random.sample(range(1,200),100)
    print("未排序前",list100)
    start100=time.time()
    array_100=HeapSort(list100)
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
    array_5000=HeapSort(list5000)
    end5000=time.time()
    print("排序后",array_5000)
    print("运行时间：",end5000-start5000)

    