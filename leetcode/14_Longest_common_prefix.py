'''
使用zip函数，把列表中字符串对应的元素打包成一个个元组（元组个数与最短的列表一致），返回这些元组组成的对象
zip(*a)将上述对象解压成列表，但需要用list()来转化
'''
def longestCommonPrefix(strs):
    s = ''
    for i in zip(*strs):#list(zip(*strs)):[('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')],i一共有四个取值
        if len(set(i)) == 1:#i是一个元组，如果它的组成元素只有一种，则其对应集合的长度为1，即原列表中字符串的该位置元素相同
            s += i[0]
        else:
            break           
    return s
list_str =  ["flower","flow","flight"]
y = longestCommonPrefix(list_str)
print(y)
'''
a=[1,2,3]
b=[4,5,6]
c=zip(a,b)#返回一个对象，对应元素压缩在一个元组中
list(c)=[(1,4),(2,5),(3,6)]#转化为列表
a1,a2=zip(*c)#元组解压为列表
list(a1)=[1,2,3]
list(a2)=[4,5,6]
'''