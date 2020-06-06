'''
方法一：内置函数法，转换为十进制计算完之后再转换为二进制
'''
def addBinary1(a,b):
    return bin(int(a, 2) + int(b, 2))[2:]

'''
方法二：进位加法原理，比较重要
先转换到相同长度，summ存储进位值（0进位，1不进位），从后向前计算。
'''
def addBinary2(a,b):
    if len(a) < len(b):#保证a是最长的
        a, b = b, a
    n = len(a)
    b = '0'*(n - len(b)) + b#补齐 b不足的位为 0
    result = ''
    summ = 0#进位值
    for i in range(n):
        a_1 = int(a[-i-1])#从后往前计算，也就是在位数上从右往左
        b_1 = int(b[-i-1])
        result = str((a_1 + b_1 + summ) % 2) + result#当前位数相加模 2 ，链接更小位数的值
        summ = (a_1 + b_1 + summ) // 2    #当前位数之和整除二，得到下一位运算的进位值

    if summ == 1:#判断最高位是否需要进位
        result = '1' + result
    return result
