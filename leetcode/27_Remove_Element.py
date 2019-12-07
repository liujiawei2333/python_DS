'''
方法一：给列表重新赋值，只留下了不等于val的值，复杂度低
'''
def removeElement1(nums,val):
    i = 0
    for j in range(len(nums)):
        # 如果nums[j]不等于val, 则将nums[j]赋值给nums[i]即可, i自增
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

'''
方法二：pop的复杂度比较高，不是很快
'''
def removeElement2(nums,val):
    p=0
    while(p<len(nums)):
        if nums[p]！=val:
            p+=1
        else:
            nums.pop(p)

nums = [3,2,2,3]
y = removeElement(nums,3)
print(y)