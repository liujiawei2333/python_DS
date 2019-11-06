'''
二分查找：要求输入必须是有序的元素列表，如果要查找的元素在列表中，返回其位置，否则返回null
每次都猜最中间，根据大小来不断缩小范围，分而治之
时间复杂度是O(logn)
'''
def binarySearch(list,item):
    low = 0
    high = len(list)-1
    while low < high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

'''
二分查找：递归方式。使用了列表的切片操作，切片操作的时间复杂度为O(n),，所以该类二分查找不会严格按照O(logn)执行，不如第一个方式好。
'''
def binarySearchRecursive(list, item):
    if len(list) == 0:
        return None
    else:
        mid = len(list) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            return binarySearchRecursive(list[mid+1:],item)
        else:
            return binarySearchRecursive(list[:mid],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRecursive(testlist, 3))
print(binarySearchRecursive(testlist, 13))

'''
不一定二分查找一定比顺序查找要好。列表元素较少时，排序的成本不值得。
应该经常考虑采取额外的分类工作是否使搜索获得好处。如果我们可以排序一次，然后查找多次，排序的成本就不那么重要。
然而，对于大型列表，一次排序可能是非常昂贵，从一开始就执行顺序查找可能是最好的选择。
'''