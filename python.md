

# 函数

 \# 默认参数：在函数声明时，指定形参的默认值，调用时可不传入参数（使用默认值）。

```python
def my_func2(x, y=1):
   print(x+y)

my_func2(2)
```

 ## 可变参数(一颗星)

变参数就是传入的参数个数是可变的，可以是1个、2个到任意个。
\#在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，并且是双精度浮点型变量

``` python
def my_func3(*numbers):
	sum = 0
  	for n in numbers:
    	sum = sum + n * n
  	return sum
```

\# 函数调用
`my_func3() `  #返回结果0
`my_func3(1,2) `#返回结果5 

## 关键字参数（两颗星）

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个字典。

``` python
def my_func4(x, **kw):
	print ('x:', x, 'other:', kw) 
```

 \#除了必选参数x外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数。 

` my_func4(8) `

 \#也可以传入任意个数的关键字参数 

` my_func4(8, z="66") `

# 三元表达式

```python
>>> y = 5
>>> x = -1 if y < 0 else 1
>>> x
1
```



## 无名参数

 如果是进行一些简单的处理的函数，可以使用关键字“lambda”来记述。

字符串变成小写：`a=lambda s: s.lower()`调用：`a(‘HEELO’)`

# with-as：上下文管理协议

```python
>>> with open(r"D:\CSDN\Column\temp\mpmap.py", 'r') as fp:
    contents = fp.readlines()
```



## 回调函数

 函数可以将别的函数作为参数使用，被作为参数使用的函数被称为回调函数，一般使用无名函数来简化过程。

`calcdisp(a,b,lambda a,b : a+b)`

## 变量使用范围的改变

在函数内部要改变外部的变量，需要在函数内部使用global或者nonlocal。

## 生成器

 生成器是函数的一种。通常，函数只会返回固定的数值，但是如果使用了生成器，便会随着调用次数的不同，返回不同的数值。 目的是避免使用list,节省内存开销

 1.需要定义生成器函数；2.需要调用生成器函 数并且初始化；3.将生成器对象作为参数调用next()函数。 

```python
def gen(maxnum):
    for i in range(maxnum):
        yield i#返回返回值的同时回到起始点，下次处理从这里执行

g=gen(5)#生成器初始化
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))#出错
```

```python
>>> def get_square(n):
    for i in range(n):
        yield(pow(i,2))

>>> a = get_square(5)
>>> a
<generator object get_square at 0x000001B2DE5CACF0>
>>> for i in a:
    print(i, end=', ')

0, 1, 4, 9, 16, 
```



## 迭代器iter

```python
>>> a = [1,2,3]
>>> a_iter = iter(a)
>>> a_iter
<list_iterator object at 0x000001B2DE434BA8>
>>> for i in a_iter:
    print(i, end=', ')

1, 2, 3, 
```



### 生成器推导式

`g=(x for x in range(5))`

注意，下面的格式t成为了[0,1,2,3,4]这样的列表(列表退导式)

`t=[x for x in range(5)]`

# 装饰器

```python
>>> import time
>>> def timer(func):
    def wrapper(*args,**kwds):
        t0 = time.time()
        func(*args,**kwds)
        t1 = time.time()
        print('耗时%0.3f'%(t1-t0,))
    return wrapper

>>> @timer
def do_something(delay):
    print('函数do_something开始')
    time.sleep(delay)
    print('函数do_something结束')


>>> do_something(3)
函数do_something开始
函数do_something结束
耗时3.077
```

 timer() 是我们定义的装饰器函数，使用@把它附加在任何一个函数（比如do_something）定义之前，就等于把新定义的函数，当成了装饰器函数的输入参数。运行 do_something() 函数，可以理解为执行了timer(do_something) 。 

# 断言assert

 断言，就是声明表达式的布尔值必须为真的判定，否则将触发 AssertionError 异常。严格来讲，assert是调试手段，不宜使用在生产环境中 

```python
>>> def i_want_to_sleep(delay):
    assert(isinstance(delay, (int,float))), '函数参数必须为整数或浮点数'
    print('开始睡觉')
    time.sleep(delay)
    print('睡醒了')


>>> i_want_to_sleep(1.1)
开始睡觉
睡醒了
>>> i_want_to_sleep(2)
开始睡觉
睡醒了
>>> i_want_to_sleep('2')
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    i_want_to_sleep('2')
  File "<pyshell#244>", line 2, in i_want_to_sleep
    assert(isinstance(delay, (int,float))), '函数参数必须为整数或浮点数'
AssertionError: 函数参数必须为整数或浮点数
```



# 类

类(Class):用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。

数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。

```python
#创建类Student
class Student(object):
   "学生成绩"
   def __init__(self, name, score):
       self.name = name
       self.score = score

   def print_score(self):
       print('%s: %s' % (self.name, self.score))

#创建Student类的对象bart
jack = Student('Bart Simpson', 59)
#创建Student类的对象lisa
bob = Student('Lisa Simpson', 87)
#访问类的属性
jack.print_score()
bob.print_score()
# 添加一个 'age' 属性
jack.age = 7  
print("添加一个 'age' 属性：",hasattr(jack, 'age'))
# 修改 'age' 属性
jack.age = 8 
print("修改 'age' 属性：",getattr(jack, 'age'))
# 删除 'age' 属性
del jack.age  
print("删除 'age' 属性：",hasattr(jack, 'age'))
```

##  **类的继承** 

面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。

通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。

```python
#编写一个名为Fruit的class，执行run()方法可以直接打印
#编写Apple和Orange类时，就可以直接从Fruit类继承
class Fruit(object):
   '父类Animal'
   def run_father(self):
       print('调用父类方法...')

class Apple(Fruit):
   '子类1 Apple'
   def run_son(self):
       print('调用子类方法...')

class Orange(Fruit):
   '子类2 Orange'
   def run_son(self):
       print('调用子类方法...')
#实例化子类
apple = Apple()
orange = Orange()
#调用父类方法
apple.run_father()
orange.run_father()
#调用子类方法
apple.run_son()
orange.run_son()
```

### **方法重写**

如果父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法

```python
class Fruit(object):
   '父类Animal'
   def run(self):
       print('调用父类方法...')

class Apple(Fruit):
   '子类1 Apple'
   def run(self):
       print('子类1 Apple 重写父类方法...')

class Orange(Fruit):
   '子类2 Orange'
   def run(self):
       print('子类2 Orange 重写父类方法...')
#实例化子类
apple = Apple()
orange = Orange()
#调用父类方法
apple.run()
orange.run()
```

# 模块

```python
# 导入模块
import math
# 现在可以调用模块里包含的函数了
print("求e的n次幂：",math.exp(1))

# from…import 语句：从模块中导入一个指定的部分到当前命名空间中
# 导入模块中的特定函数
from math import exp
# 现在可以直接使用该函数了
print("求e的n次幂：",exp(1))

# from…import* 语句：导入一个模块中的所有项目。然而这种声明不该被过多地使用
from math import *
```

## 交换两个变量的值：

` a, b = b, a `不需要中间变量

## 元素重复次数

`Counter`会计算每一个元素出现的次数，`Counter()`会返回一个字典，元素作为key，出现的次数作为 value。

我们也可以使用 `most_common()` 这个方法来获取出现字数最多的元素。

```python
from collections import Counter
my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # defining a counter object
print(count) # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})
print(count['b']) # of individual element
# 3
print(count.most_common(1)) # most frequent element
# [('d', 5)]
```

## 寻找变位词

使用`Counter`的一个很有意思的用法是找变位词：

变位词一种把某个词或句子的字母的位置（顺序）加以改换所形成的新词。

使用 `Counter` 得到的两个对象如果相等，则他们是变位词：即两个字符串的组成元素是否是一样的

```python
from collections import Counter
str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3  = Counter(str_1), Counter(str_2), Counter(str_3)
if cnt_1 == cnt_2:
   print('1 and 2 anagram')
if cnt_1 == cnt_3:
   print('1 and 3 anagram')
```

## 异常捕获

`try-except`

```python
a, b = 1,0
try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
   print("Run this always")
```

## 枚举遍历

```python
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))
# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
```

## 对象使用内存的大小

getsizeof()获取对象的字节大小，只计算直接占用的内存，而不是对象内所引用对象的内存

```python
import sys#sys模块提供给解释器交互的函数
num = 21
print(sys.getsizeof(num))#24,不完全准确，包含了其他信息，单位为byte
```

 一个静态创建的列表，如果只包含两个元素，那它自身占用的内存就是 80 字节，不管其元素所指向的对象是什么。 

```python
a = [1, 2]
b = [a, a]  # 即 [[1, 2], [1, 2]]

# a、b 都只有两个元素，所以直接占用的大小相等
sys.getsizeof(a) # 结果：80
sys.getsizeof(b) # 结果：80
```

 空对象，但是这些对象在内存分配上并不为“空”，而且分配得还挺大 

```python
sys.getsizeof("")      # 49
sys.getsizeof([])      # 64
sys.getsizeof(())      # 48
sys.getsizeof(set())   # 224
sys.getsizeof(dict())  # 240

# 作为参照：
sys.getsizeof(1)       # 28
sys.getsizeof(True)    # 28
```

 **基础数字<空元组 < 空字符串 < 空列表 < 空集合 < 空字典** 

 这些空对象都是容器，我们可以抽象地理解：它们的一部分内存用于创建容器的骨架、记录容器的信息（如引用计数、使用量信息等等）、还有一部分内存则是预分配的 

```python
import sys
sys.getsizeof("")      # 49
sys.getsizeof([])      # 64
sys.getsizeof(())      # 48
sys.getsizeof(set())   # 224
sys.getsizeof(dict())  # 240

# 作为参照：
sys.getsizeof(1)       # 28
sys.getsizeof(True)    # 28
```

 空对象并不为空，一部分原因是 Python 解释器为它们预分配了一些初始空间。在不超出初始内存的情况下，每次新增元素，就使用已有内存，因而避免了再去申请新的内存 。

内存扩充是不均匀的：

 **超额分配机制：**申请新内存时并不是按需分配的，而是多分配一些，因此当再添加少量元素时，不需要马上去申请新内存 

 **非均匀分配机制：**三类对象申请新内存的频率是不同的，而同一类对象每次超额分配的内存并不是均匀的，而是逐渐扩大的 

 **在元素个数相等时，静态创建的列表所占的内存有可能小于动态扩容时的内存！** 

消减元素并不会释放内存

## 代码执行时间

```python
import time
start_time = time.time()#单位为秒
# Code to check follows
a, b = 1,2
c = a+ b
# Code to check ends
end_time = time.time()
time_taken_in_micro = (end_time- start_time)*(10**6)

print(" Time taken in micro_seconds: {0} ms").format(time_taken_in_micro)
```

## 随机取样

```python
import random
my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = random.sample(my_list,num_samples)#从列表中随机取num_samples个数
print(samples)
```

更安全的随机取样库secrets

```python
import secrets                              # imports secure module.
secure_random = secrets.SystemRandom()      # creates a secure random object.
my_list = ['a','b','c','d','e']
num_samples = 2
samples = secure_random.sample(my_list, num_samples)
print(samples)
```

## 数字化

```python
um = 123456
list_of_digits = list(map(int, str(num)))
print(list_of_digits)
# [1, 2, 3, 4, 5, 6]
```

## 唯一性检查

检查列表中的元素是否是不重复的，用列表的长度和其对应的集合的长度做对比

```python
def unique(l):
    if len(l)==len(set(l)):
       print("All elements are unique")
    else:
        print("List has duplicates")

unique([1,2,3,4])
# All elements are unique

unique([1,1,2,3])
# List has duplicates
```

# for-else模块

```python
>>> for i in [1,2,3,4]:
    print(i)
else:
    print(i, '我是else')

1
2
3
4
4 我是elsepy
```

