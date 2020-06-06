'''
方法一：动态规划。斐波那契数列
f(i)=f(i-1)+f(i-2)
到达i的方法=到达i-1的方法+到达i-2的方法
'''
def climbStairs1(n):
    f = [1, 2]#在第一阶和第二阶的方法数
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])#用列表保存每一阶的方法数
    return f[n-1]

n = 3
print(climbStairs(n))