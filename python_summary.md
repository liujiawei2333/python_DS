# 列表

可变数据结构，元素可以相同，`list=[1,2,True,0.2]`

|                             函数                             |                             解释                             | 复杂度 |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----: |
|                          `list[i]`                           |                        访问索引i的值                         |        |
|                         `list[::-1]`                         |                             反序                             |        |
|                       `list(range(10)`                       |                        创建自然数列表                        |        |
|            `list=[1,2,3,4]`  <br> ` a,b,c,d=list`            |                           列表解包                           |        |
|                        `list[x:y:z]`                         | 从索引x到y，每z个元素取一个<br>如果z<0,反向取值<br>x不指定，默认为第一个元素<br>y不指定，默认为最后一个元素 |        |
| ` list_of_lists = [[1], [2, 3], [4, 5, 6]] `<br>` sum(list_of_lists, []) =[1, 2, 3, 4, 5, 6]` |                    列表中的元素拉平成一维                    |        |
|      `a=[1,2,True,4.5]`<br>`a[1]=2`，`a[1:3]=[2,True]`       |                           列表取值                           |        |
|                         `len(list)`                          |                    列表的长度（元素数量）                    |  O(1)  |
|                        `list1+list2`                         |             列表相加，按顺序拼接，相同元素不合并             |        |
|                           `list*n`                           |                        n个该列表拼接                         |        |
|                 `list2=[2*x for x in list]`                  |                   列表推导式，每个元素乘2                    |        |
|                        `item in list`                        |                   元素是否在列表中，布尔值                   |        |
|                     `list.append(item)`                      |                      列表尾部加item元素                      |        |
|                    `list.insert(i,item)`                     |                   第i个索引处插入item元素                    |        |
|                `list.pop()`<br>`list.pop(i)`                 | 删除最后一项元素，返回该项;<br>删除索引为i的元素项并返回该项 |  O(n)  |
|          `list.sort()`<br>`list.sort(reverse=True)`          |                从小到大排序;<br>从大到小排序                 |        |
|                       `list.reverse()`                       |                         元素反序排列                         |        |
|         `list.index(item)`<br>`list.index(item,a,b)`         | 第一个item元素出现的索引;<br>在索引a~b的范围内，第一个item出现的索引位置 |        |
|                      `list.count(item)`                      |                      item元素出现的次数                      |        |
|                     `list.remove(item)`                      |                   移除第一个出现的item元素                   |        |
|                        `del list[i]`                         |                      删除索引为i的元素                       |        |
|                     `list.search(item)`                      |                 寻找item元素是否存在，布尔值                 |        |
|                         `max(list)`                          |                           最大元素                           |        |
|                         `min(list)`                          |                           最小元素                           |        |
|                         `list(str)`                          |                       字符串转化为列表                       |        |
|                     `filter(bool,list)`                      |                将False，None，0，“” 等值去掉                 |        |
|             ` max(set(list), key = list.count)`              |                  取列表中出现频率最高的元素                  |        |
|                   `dict(zip(list1,list2))`                   |          将两个列表转化为字典，list1为键，list2为值          |        |
| `zip(*[['a', 'b'], ['c', 'd'], ['e', 'f']])`<br>`[('a', 'c', 'e'), ('b', 'd', 'f')]` |                  解包，成对列表解为两个元组                  |        |

# 字符串

不可变的数据结构,`string="124sdaf"`

|              函数              |                             解释                             | 复杂度 |
| :----------------------------: | :----------------------------------------------------------: | ------ |
|          `string[i]`           |                        访问索引i的值                         |        |
|       `string.center(w)`       |    位于尺寸为w的中心的串，如果w小于串的长度，则返回串本身    |        |
|       `string.ljust(w)`        |                    位于尺寸为w的左侧的串                     |        |
|        `string.just(w)`        |                    位于尺寸为w的右侧的串                     |        |
|      `string.count(item)`      |                      item元素出现的次数                      |        |
|        `string.upper()`        |                         所有元素大写                         |        |
|        `string.lower()`        |                         所有元素小写                         |        |
|        `string.title()`        |                          首字母大写                          |        |
|     `string.find('item')`      |                   item字符第一次出现的索引                   |        |
|     `string.split(schar)`      | 用schar字符作为分割点返回**字符串列表**，如果没有schar，则以**空格**为分割点 |        |
|      `string.join(schar)`      | 将序列中的元素以schar字符连接生成一个新的字符串，这个序列可以是元组、列表、字典和字符串，但其元素必须是字符串 |        |
|     `string.strip(schar)`      |          删除首尾的schar字符,如果不指定，默认为空格          |        |
|     `string.lstrip(schar)`     |        删除首（左）的schar字符,如果不指定，默认为空格        |        |
|     `string.rstrip(schar)`     |        删除尾（右）的schar字符,如果不指定，默认为空格        |        |
|         `string[::-1]`         |                             反转                             |        |
|            `str(x)`            |                   其他数据类型转换为字符串                   |        |
|       `string1+string2`        |                     按顺序拼接两个字符串                     |        |
|           `string*n`           |                       n个该字符串拼接                        |        |
| `len(string.encode('utf-8')) ` |                      字符串占用的字节数                      |        |

# 元组

不可变数据结构，`Tuple=(2,True,4.96)`

|      函数       |                        解释                        | 复杂度 |
| :-------------: | :------------------------------------------------: | :----: |
|   `Tuple[i]`    |                   访问索引i的值                    |        |
|  `Tuple=(50,)`  | 只包含一个元素时，需要加逗号，不然括号就当做运算符 |        |
| `Tuple1+Tuple2` |                 按顺序拼接两个元组                 |        |
|    `Tuple*n`    |                   n个该元组拼接                    |        |
|   `del tuple`   |          删除整个元组，但无法删除某个元素          |        |
|  `len(Tuple)`   |                      元素个数                      |        |
|  `max(Tuple)`   |                     元素最大值                     |        |
|  `min(Tuple)`   |                     元素最小值                     |        |
|   `tuple(x)`    |      其他数据类型转换为元组，包括列表和字符串      |        |

