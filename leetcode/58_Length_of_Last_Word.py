'''
方法一：rstrip()去掉字符串最后面（右边）的空格；split()用空格把字符串分割成列表；[-1]取最后一个
'''
def lengthOfLastWord(s):
    return len(s.rstrip().split(" ")[-1])

s = "we are friends"
s1 = " "
print(lengthOfLastWord2(s1))