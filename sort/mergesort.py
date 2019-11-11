'''
归并排序：分而治之，递归
不断将列表拆分为一半，为空或一个项（递归停止条件）时进行排序，递归调用两半部分的合并排序，完成后进行合并。
分割：递归地把当前序列平均分割为两半
集成：在保持元素顺序的同时将上一步得到的子序列集合到一起。
时间复杂度：O(nlogn):合并操作有n个，列表划分操作有logn个。
但需要额外的空间来保存两半部分，空间复杂度需要考虑，不是很适合大型数据集。
'''
def mergeSort(list):
    if len(list) > 1:#不断调用自己直到拆分为单个元素的时候返回这个元素，不再拆分
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0#左侧的列表的索引
        j=0#右侧的列表的索引
        k=0#归并子列表的索引
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1
        #上述while循环出来后，说明i，j的其中一个数组没有数据了，接下来需要分别进行两个循环把那个没循环完的序列循环完

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1

list = [54,26,93,17,77,31,44,55,20]
mergeSort(list)
print(list)