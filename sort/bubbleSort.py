'''
冒泡排序： 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
1.比较相邻的两个数据，如果反序则交换两个数
2.对每一个相邻的数做1的工作，这样从开始到结尾一队在最后的数就是最大的数。相当于最大的数一个个在最后面浮出
3.对所有元素进行上面的操作，除了最后一个
时间复杂度为O(n^2)
但交换的次数太多，效率低下
'''

def bubbleSort(arr):#从小到大排序
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i])
