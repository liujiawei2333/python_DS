#题目默认给定的数组是从小到大排列的
def searchInsert1(nums, target):
    if not target in nums:
        for i in range(len(nums)):
            if nums[i] > target:
                nums.insert(i,target)
                return i
            elif nums[len(nums) - 1] < target:#目标数比数组中所有数都大时，返回数组长度，即最后一个索引后面的索引
                return len(nums)
    else:
        return nums.index(target)#自带函数实现查找

def searchInsert2(nums, target):
    if not target in nums:
        for i in range(len(nums)):
            if nums[i] > target:
                nums.insert(i,target)
                return i
            elif nums[len(nums) - 1] < target:
                return len(nums)
    else:#用二分查找寻找
        low = 0
        high = len(nums) - 1
        while low <= high:#这里添加了"="是防止出现数组只有一个数的情况
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

a = [1,3,5,6]
b = 2
c = searchInsert2(a,b)
print(c)
