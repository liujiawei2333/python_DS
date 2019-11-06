输出变量的数据类型：`type(a)`

` print(isinstance(a, float)) `：判断是否是对应的类型，返回布尔值

`a / b `:除法，返回浮点数

`a // b`:除法，返回整数

`a % b`:取余数

`a**b`:乘方

# 列表

列表是可以变的数据结构，元素可以相同，支持各种数据结构和包含列表（嵌套）

1. 解包：    `list=[1,2,3,4]`

​			`a,b,c,d=list`

2. 反序：

` elems = list(range(10)) `  = ` [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] `

` elems[::-1] =[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`

3. `[x:y:z]`：从索引x到索引y，每z个元素取一个

如果z是负数，就是反向取了。

如果x不特别指定，就默认是在遍历列表的方向上，遇到的第一个元素。

如果y不特别指定，就默认是列表最后一个元素。

` elems[::2] =[0, 2, 4, 6, 8]`

` elems[-2::-2] = [8, 6, 4, 2, 0]`

删掉列表中的偶数:`elems[::2]=[1, 3, 5, 7, 9] `

4. 列表中的每个元素也是列表，拉平：

` list_of_lists = [[1], [2, 3], [4, 5, 6]] `

` sum(list_of_lists, []) =[1, 2, 3, 4, 5, 6]`

5. 某个元素:

`a=[1,2,True,4.5]`

`a[1]=2`，`a[1:3]=[2,True]`

6. 列表的长度`len(a)=4`，与索引无关，就是元素的数量

7. 列表相加`b=[2,4]`

`a+b=[1,2,True,4.5,2,4]`是有顺序的，相同的不会合并

8. 列表相乘`b*3=[2,4,2,4,2,4]`
9. 列表推导式：` new_list = [2*x for x in original_list] `，每个元素都乘2，与第8条是不同的
10. 判断元素是否在列表中`2 in b   True`
11. `list.append(item)`尾部加item元素
12. `list.insert(i,item)`:第i个索引处插入元素item
13. `list.pop()`:删除最后一项并返回该项

​	`list.pop(i)`:删除索引为i的项并返回该项

13. `list.sort()`:元素从小到大排序
14. `list.sort(reverse = True)`：元素从大到小排序
15. `list.reverse()`:元素反序排列
16. `list.count(item)`:item元素出现的次数
17. `list.index(item)`:第一个item出现的索引位置
18. `list.remove(item)`:移除第一个出现的item
19. `del list[i]`:删除索引为i的元素
20. `list.search(item)`:寻找item是否存在，返回布尔值
21. `range(5,10)`

​	`list(range(5,10))=[5,6,7,8,9,10]`

​	`list(range(5,10,2)=[5,7,9]`

21. `max(list)`:返回列表最大值

22. `min(list)`：返回列表最小值

23. `list(str)`：将字符串转化为列表

24. ` filter(bool, list) `：将 False，None，0，“”） 等值去掉

25. ` max(set(list), key = list.count)`:取列表中出现频率最高的元素

26. 将两个列表转换为字典

    ```python
    dict(zip(list1,list2))
    #list1作为键，list2作为值
    ```

    

27. 解包，将成对列表解开成两组不同的元组

    ```python
    array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    transposed = zip(*array)
    print(transposed)
    # [('a', 'c', 'e'), ('b', 'd', 'f')]
    ```

    





# 字符串

字符串是不可变的数据结构

1. `astring.center(w)`:位于尺寸为w的中心的串，如果w小于串的长度，则返回串本身

2. `astring.count(item)`:串中item出现的次数

3. `astring.ljust(w)`:位于尺寸为w的左侧的串

4. `astring.rjust(w)`:位于尺寸为w的右侧的串

5. `astring.lower()`:所有元素小写

6. `astring.upper()`:所有元素大写

7. `astring.title()`:首字母大写

8. `astring.find(item)`:item出现第一次的下标

9. `astring.split(schar)`:用分割字符作为分割点返回字符串列表，如果没有schar，则以空格为分割点

10. 把字符串列表拼接乘一个字符串：`‘char’.join(astring)`:用char连接字符串，char一般为，、或者没有

    ```python
    list_of_strings = ['My', 'name', 'is', 'Chaitanya', 'Baweja']
    # Using join with the comma separator
    print(','.join(list_of_strings))
    # Output
    # My,name,is,Chaitanya,Baweja
    ```

    

11. 反转：`astring[::-1]`与列表的做法相同

12. 回文检测

    ```python
    my_string = "abcba"
    if my_string == my_string[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
    ```

    

13. `astring+"!!!"`：+表示连接两个字符串

14. `astring*2`:  \* 表示复制当前字符串，紧跟的数字为复制的次数 

15. `“a \nbook”`:  \ 转义特殊字符 

16. `r"a \nbook`: 若不想让反斜杠发生转义，可以在字符串前面添加一个 r 

17. 字符串占用字节数：` len(string.encode('utf-8')) `

18. 取出一个字符串中所有组成他的元素，使用集合set

    ```python
    my_string = "aavvccccddddeee"
    temp_set = set(my_string)  #{'d', 'e', 'a', 'v', 'c'}
    new_string = ''.join(temp_set)  #deavc
    ```

    

    # 元组

    元组是不可以变的数据结构

    `Tuple=(2,True,4.96)`

     元组中只包含一个元素时，需要在元素后面添加逗号,否则括号会被当作运算符使用  `Tuple=(50,)`

    1. `Tuple[0]`: 使用下标索引来访问元组中的值 
    2. `tuple1+tuple2`: 对元组进行连接组合 
    3. `tuple*2`:  \* 表示复制当前元组，紧跟的数字为复制的次数 
    4. ` del tuple`:删除整个元组，但不能删除其中的某个元素
    5. `len(tuple)`：元组中元素个数
    6. `max(tuple)`:返回元组最大值
    7. `min(tuple)`：返回元组最小值
    8. ` tuple(list) `:列表转换为元组

# 集合

集合是不可改变且不可重复的无序数据结构

`set={3,6,“cat”,“4.5,False”}`

 注意：创建一个空集合必须用 set() 而不是 {}，因为 {} 是用来创建一个空字典。 

1. `xxx in set`:某元素是否属于set，返回布尔值

2. `len(set)`:集合中元素的个数，是从下标为1开始的，是几个元素就是几

3. `set1 | set2`:求并集=`set1.union(set2)`

4. `set1 & set2`求交集=`set1.intersection(set2)`

5. `set1-set2`:set1中的元素去掉与set2相同的元素=`set1.difference(set2)`,3,4,5条都是会创建新的集合

6. `set1<=set2`：set1是否属于set2=`set1.issubset(set2)`返回布尔值

7. `set.add(item)`：添加元素item

8. `set.remove(item)`:移除元素item

9. `set.pop()`：随意移除一个元素

10. `set.clear()`：元素清空，得到set()

11. `set.update('p')`:添加一个元素

12. `set.update(['a','b','c'])`：添加多个元素

13. `set.update(['a','b'],{'a','b'})`:添加列表和集合

    # 字典

    无序的可变类型，键值对`k={'A':'a','B':'b'}`，键必须是唯一的

    创建字典,用{}创建：`dict1={'A':'a','B':'b'}`

    ​    或用内置函数`dict2=dict(A='a',B='b')`

    1. 取值`k['A']='a'`:如果没有会报错

    2. 增加新的键值对：`k['C']='c'`

    3. `key in dict`:键是否在字典中，返回布尔值

    4. `del dict[key]`:删除key及其对应的值

    5. `dict.keys()`:获取所有键

    6. `dict.values()`:获取所有值

    7. `dict.item()`：获取所有键值对

    8. `list(dict.keys())等三种`：将4,5,6的结果转换为列表

    9. `dict.get(key)`：获取k对应的值，如果没有则为None

    10. `dict.get(key,alt)`：获取k对应的值，如果没有则为alt

    11. `dict.clear()`：清空字典

    12. `dir(dict)`：查看dict的所有方法

    13. 合并两个字典：

        ```python
    dict_1 = {'apple': 9, 'banana': 6}
        dict_2 = {'banana': 4, 'orange': 8}
    combined_dict = {**dict_1, **dict_2}#两个字典存在交集的时候，后一个覆盖前一个
        
        ```
    
    print(combined_dict)
        # Output
# {'apple': 9, 'banana': 4, 'orange': 8}
        ```

    
​    
    
    # 栈
        
    后入先出（顶） 
        
    `from pythonds.basic.stack import Stack`
        
    `s = Stack()`
        
        1. `s.isEmpty()`:判断栈是否为空，返回布尔值
        
        2. `s.push(item)`:元素item加到顶部
        
        3. `s.size()`:计算栈中元素的数量，是从下标为1开始的，是几个元素就是几
        
        4. `s.pop()`：删除顶部的项
        
           # 队列
        
           先进先出
        
           `from pythonds.basic.queue import Queue`
        
           `q = Queue()`
        
           1. `q.isEmpty()`:判断队列是否为空，返回布尔值
        
           2.  `q.enqueue(item)`：元素item添加到队尾
        
           3. `q.dequeue()`：移除队首的项，返回该项
        
           4. `q.size()`：元素数量，是从下标为1开始的，是几个元素就是几
    
    
    ​          
    
        # 双端队列

有队列和栈的所有能力

`from pythonds.basic.deque import Deque`

`d = Deque()`

1. `d.isEmpty()`:判断双端队列是否为空
2. `d.addRear(item)`:item元素添加到尾部
3. `d.addFront(item)`：item元素添加到首部
4. `d.removeRear()`:删除尾部，返回该项
5. `d.removeFront()`:删除首部，返回该项
6. `d.size()`：元素数量，是从下标为1开始的，是几个元素就是几

