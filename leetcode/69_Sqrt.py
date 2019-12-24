'''
方法一：我自己的。二分法
'''
def mySqrt1(x):
    if x == 0:#取值为0的边界情况
        return 0
    else:#二分法
        low = 1
        high = (x+1)//2+1#由于要求的数不可能在原数的一半以上，一定在(x+1)//2+1左边
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 > x:
                high = mid -1
            elif (mid ** 2 < x) & ((mid + 1)** 2 <= x):
                low = mid + 1
            elif (mid ** 2 < x) & ((mid + 1)** 2 > x):#不能完全平方的情况
                return mid
            elif mid ** 2 == x:#完全平方的情况
                return mid

'''
方法二：二分法，无需特别考虑边界情况，但要注意特值对搜索边界的影响
时间复杂度：O(logn)
空间复杂度：O(1)
'''
def mySqrt2(x):
    left = 0#照顾到0
    right = x // 2 + 1#照顾到1
    while left < right:
        mid = (left + right + 1) >> 1#右移1位，除以2向下取整;同时加一选择右中位数
        square = mid * mid
        if square > x:
            right = mid - 1
        else:
            left = mid
    return left

'''
方法三：牛顿法
直线代替曲线，一阶泰勒展开，求交点，反复
'''
def mySqrt3(x):
    if x == 0:
        return 0
    else:
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2#推导的公式
            if abs(cur - pre) < 1e-6:#抵消浮点运算中因为误差造成的相等无法判断的情况
                return int(cur)

x=100000023
y = mySqrt(x)
print(y)