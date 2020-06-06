'''
方法一：把列表代表的数字按十进制算出来，加1后转换为str再转换为list
'''
def plusOne1(digits):
    num = 0
    len_num = len(digits)
    for i in range(len_num):
        num += digits[i] * 10**(len_num - 1 - i)
    num_plus = num + 1
    str_num = str(num_plus)
    num_plus = list(str_num)

    return num_plus

'''
方法二：str与int之间互相转换，用join方法来连接字符串元素
'''
def plusOne2(digits):
    return [int(x) for x in str(int(''.join([str(i) for i in digits])) + 1)]

'''
方法三：不进行计算，孤僻算法，慎用
    遍历digits，判断最后位是否为9，若不是则+1并返回，否则将此位置0；
    对于digits里全为9的情况，需要扩展list，并将首位置为1。
'''
def plusOne3(digits):
    for i in range(len(digits) - 1,-1,-1):#倒叙遍历
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits[0] = 1
    digits.append(0)
    return digits
            


a = [2,8,9]
b = plusOne3(a)
print(b)
