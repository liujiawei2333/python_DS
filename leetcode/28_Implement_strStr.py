'''
方法一：使用find内置函数，寻找item第一次出现的索引。
'''
def strStr1(haystack,needle):
    return haystack.find(needle)
'''
方法二：使用切片寻找
'''
def strStr2(haystack,needle):
    for i in range(0, len(haystack) - len(needle) + 1):#当needle正好在haystack最后的位置，则需要循环的长度为len(haystack) - len(needle) + 1
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

x = "hellohehe"
y = "lo"
a = strStr2(x,y)
print(a)