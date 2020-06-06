'''
建立哈希表；
根据规则，左边的比右边的大则加上左边的数，左边的比右边的小则减去左边的（循环范围在开始到倒数第二个数）；
最后一位没有右边的数要比，直接加上
'''
def romantoint(s):
    roma_hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}#建立哈希表
    num = 0
    for i in range(len(s)-1):#循环范围到倒数第二个数为止
        if roma_hash[s[i]] >= roma_hash[s[i + 1]]:
            num += roma_hash[s[i]]
        else:
            num -= roma_hash[s[i]]
    last_num = s[len(s) - 1]#对最后一位的处理
    num = num + roma_hash[last_num]
    return num

s = 'MMCMLXIV'
y = romantoint(s)
print(y)


    
