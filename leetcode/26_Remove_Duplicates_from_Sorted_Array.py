'''
方法一：逆序遍历，遇到相同的元素则删掉重复的元素
逆序是为了防止删除元素后影响下一位索引的定位
pop操作的复杂度是O(n)，故总复杂度为O(n^2)
'''
def removeDuplicates1(nums):
    for i in range(len(nums)-1, 0, -1):#逆序排列，从后往第一个，-1代表步长为反向
        if nums[i] == nums[i-1]: 
            nums.pop(i)
    return len(nums)

'''
方法二：双指针法
i为慢指针，j为快指针，满足条件时增加j以跳过重复项(比较难懂)
时间复杂度O(n)
'''
def removeDuplicates2(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1 if nums else 0

'''
方法三：另一种容易理解的双指针法
两个指针分别指向第一、第二个元素，如果相等就删除第二个元素，不等的话两个指针位置都加一
pop操作的复杂度为O(n),所以总复杂度为O(n^2)
'''
def removeDuplicates3(nums):
    pre,cur = 0,1
    while cur < len(nums):
        if nums[pre] == nums[cur]:
            nums.pop(cur)
        else:
            pre,cur = pre + 1,cur + 1
    return len(nums)
list = [1,1,2,2,3,4]
y = removeDuplicates2(list)
print(y)