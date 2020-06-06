'''
本题的思路就是先判断给定整数x的正负情况，把符号首先给提取出来,然后将abs(x)变成字符串，接着将字符串反转，最后恢复成整数
还有一些思路是用整数去除以10，取整来做，但还是转换为字符串更简单一些。
'''
class Solution:
    def reverse(self, x):
        x_flag = -1 if x <= 0 else 1#记录x的正负
        abs_x = abs(x)
        str_x = str(abs_x)#变成字符串
        reverse_str_x = str_x[::-1]#字符串反序
        reverse_int_x = int(reverse_str_x)#反序后的字符串变成整数
        reverse_int_x = reverse_int_x * x_flag#恢复正负号
        if -2 ** 31 <= reverse_int_x <= 2** 31 - 1:#范围判断
            return reverse_int_x
        else:
            return 0
