'''
希尔排序：递减增量排序，是对插入排序的改进
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
时间复杂度O(n)~O(n^2)之间，不同的序列的复杂度不同。
与插入排序相比，在代码上只是多了个gap，用来划分子序列，当gap为1时，即为最后一步的插入排序。
'''
def shellSort(list): 
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap,len(list)): 
            j = i 
            while  j >= gap and list[j-gap] >list[j]: 
                list[j - gap], list[j] = list[j], list[j-gap]
                j = j - gap
        gap = gap // 2
    return list
  
list = [ 12, 34, 54, 2, 3] 
  
shellSort(list) 
print(list)
