'''
栈：先入后出
遇到左括号入栈，遇到右括号将对应栈顶的左括号出栈，遍历完所有括号后栈为空
建立哈希表，键为左括号，值为右括号，查询括号是否对应只需要O(1)的复杂度
'''
def isValid(s):
    '''&是按位与，将两者转化为二进制数，对应位置都为1的结果对应位置才为1，否则都为0'''
    if len(s) & 1 == 1:  # 位运算判断s的个数的奇偶（常用，记住！），如果len(s)为奇数，则其二进制最后一位必然为1
        return False

    stack = []
    hash_map = {'(': ')', '[': ']', '{': '}'}#建立哈希表
    for c in s:
        if c in hash_map:#所有的左括号入栈
            stack.append(c)
            continue
        elif stack and hash_map[stack[-1]] == c:#栈顶的元素对应哈希表的值正好为接下来的元素，则该左括号被删除
            stack.pop()#删除最后一个元素（栈顶弹出）
        else:
            return False
    return not stack

s="{()[]}"
y = isValid(s)
print(y)