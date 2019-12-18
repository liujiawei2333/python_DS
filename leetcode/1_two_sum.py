'''
用两层循环的暴力破解方式不可取，时间复杂度太高
'''
'''方法一：
遍历列表的同时查字典
'''
def two_sum1(nums, target):
    dct = {}
    for i, n in enumerate(nums):
        if target - n in dct:
            return [dct[target - n], i]
        dct[n] = i

'''方法二：
找到 num2 = target - num1，是否也在 list 中，用以下两个方法：
num2 in nums，返回 True 说明有戏
nums.index(num2)，查找 num2 的索引
'''
def two_sum2(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue#继续循环
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从i+1后的序列后找num2
                break
    if j>0:
        return [i,j]
    else:
        return []

'''
方法三：
对方法二的改进，每次只查找num1位置的之前,时间缩短了一半以上
'''
def two_sum3(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]

'''
方法四：用字典来建立哈希表求解（关键方法）
'''
def two_sum4(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind#以数组的值为哈希表的键，以数组的索引为哈希表的值
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:#判断索引是否重复
            return [i,j]

'''
方法五:改进方法四
'''
def two_sum5(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

list = [11,15,2,2,7]
target = 9
output = two_sum4(list,target)
print(output)