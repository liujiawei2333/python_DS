'''
方法一：转化为字符串，判断是否与反序的时候相等（最简单）
'''
def isPalindrome(x):
    if str(x) == str(x)[::-1]:
            return True
        else:
            return False

'''
方法二：不转化为字符串，用数字关系来获得反序的数
'''
def isPalindrome(x):
     if x < 0 :#负数不可能是回文数
            return False
        
        '''n得到的是与x反序的整数'''
        m,n = x,0
        
        while m:
            n = n * 10 + m % 10
            m = m // 10
            
        if x == n:
            return True
        else:
            return False

X = 1212
Y = isPalindrome(X)
print(Y)