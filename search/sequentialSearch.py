'''
顺序查找：按从前到后的顺序查找，不要求列表具有一定的顺序，时间复杂度为O(n)
'''
def sequentialSearch(alist, item):
        pos = 0
        while pos < len(alist):
            if alist[pos] == item:
                return pos
            else:
                pos = pos+1
        return None

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

'''
升序列表的顺序查找：超过被查找项依然没有找到，则不必继续，可以停止，时间复杂度虽然理论上依然为O(n)，但实际上能减少一些多余操作
'''
def orderedSequentialSearch(alist, item):
        pos = 0
        while pos < len(alist):
            if alist[pos] == item:
                return pos
            else:
                if alist[pos] > item:
                    break#跳出循环
                else:
                    pos = pos+1
        return None

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))