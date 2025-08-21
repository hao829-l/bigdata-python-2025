# map函数
print(map(lambda n: n ** 2, [1, 2, 3, 4, 5, 6]))
print(list(map(lambda n: n ** 2, [1, 2, 3, 4, 5, 6])))      # 将可迭代器转化为list（列表）类型


# reduce函数

from functools import *

print(reduce(lambda x , y : x + y , [2,4,6,8,10],(1)))


# 案例：统计每个单词出现的次数

str1 = 'hello python hello world java list hi python hello hi'
# 第一步：把单词切割开
lst = str1.split(' ')

# 第二步：每个单词只要出现了就代表有一次
new_lst = list(map(lambda item: {item:1}, lst))
print(new_lst)

# 第三步：调用reduce实现相同单词的叠加
def func(dict1, dict2):
    # 把dict1作为叠加的返回字典
    key = list(dict2.items())[0][0]         #items获取所有项
    value = list(dict2.items())[0][1]       #得到dict2中的value

    dict1[key] = dict1.get(key,0) + value
    return dict1

print(reduce(func, new_lst))


# filter函数

lst1 = [1,2,3,4,5,6,7,8,9,10]

# 偶数留下
print(list(filter(lambda x: x % 2 == 0, lst1)))


# sorted函数

# 需要给某个复杂的列表排序
lst = [
    {'name':'张三','age':31},
    {'name':'李四','age':17},
    {'name':'王五','age':20}
]

print(sorted(lst , key = lambda item : item['age'],reverse = True))


# 排列字符串
str_lst = ['hello','python','Java','hi','world']

print(sorted(str_lst,key = str.lower))      #upper










