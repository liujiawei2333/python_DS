'''
插入排序：构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入(背下，比较难理解，画图示)
时间复杂度O(n^2)，但都是移位的操作而没有交换（一般移位操作只需要交换大约三分之一的处理工作），所以性能还不错
'''
def insertionSort(list): #从小到大
    for i in range(1, len(list)):
        j = i
        while j >=1 and list[j-1] > list[j]: #对已经构建的序列从后往前扫描
                list[j - 1], list[j] = list[j], list[j-1]
                j -= 1

list = [12, 11, 13, 5, 6,7,100] 
insertionSort(list) 
print (list)

