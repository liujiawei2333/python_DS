'''
方法一：暴力匹配
枚举所有长度大于等于2的子串，依次判断是否为回文
只对于“大于当前最长子串长度”的子串进行验证
时间复杂度：0(n^3):左边界、右边界和继续验证子串都与n有关
空间复杂度：0(1),只用了常数个临时变量
'''
'''重要的程序，要背下'''
def valid(s,left ,right):#验证子串是否为回文串，与“判断串是否为子串”是相同的
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def longestPalindrome(s):
    size = len(s)
    if size < 2:#小于2的特例的处理，长度小于2的串一定是回文串
        return s
    
    max_len = 1
    res = s[0]

    #枚举所有长度大于等于2的字串
    for i in range(size - 1):
        for j in range(i + 1,size):
            if j - i + 1 > max_len and valid(s,i,j):
                max_len = j - i + 1
                res = s[i:j+1]
    return res

X = "cbbd"
Y = longestPalindrome(X)
print(Y)


