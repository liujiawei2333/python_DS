'''
方法一：两个数组合并后排序，没有利用两个数组本身就是有序的特点，导致时间复杂度较高
时间复杂度O((n+m)log(n+m))
空间复杂度O(1)，注：实际上应该是O(m)，因为切片操作导致列表拷贝（拷贝的是地址，不是对象本身）
'''
def merge1(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m] + nums2)
    '''
    等号左边的nums1必须加上[:]才能是改变了原nums1的值
    sorted方法返回的是原列表的副本，如果只用nums1只是将其指向副本，而nums1在内存中的原地址的值没有变化
    用nums1[:]就能将内存中的地址的值改变
    '''

    
'''
方法二：双指针，从前往后
时间复杂度O(n+m)
空间复杂度O(m),重新开辟了nums_copy的空间
'''
def merge2(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1[:] = []#用来保存最终结果的列表,等号左边的nums1必须加上[:]才能是改变了原nums1的值

    p1 = 0
    p2 = 0
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:#在两个列表中选择最小的那个保存
            nums1.append(nums1_copy[p1])
            p1 += 1#自增是很重要的
        else:
            nums1.append(nums2[p2])
            p2 += 1#自增是很重要的
    #循环完成后，依然有某个数组中有元素剩下，需要保存
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]

'''
方法三：三指针，从尾部开始改nums1的值，不需要重新创建一个列表，降低了空间复杂度
时间复杂度O(n+m)
空间复杂度O(1)
'''
def merge3(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1#nums1的指针
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]#剩余的元素