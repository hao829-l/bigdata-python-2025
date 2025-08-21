# 使用匿名函数计算两个数字的和
fn = lambda x , y : x + y
print(fn(8,10))


# 需要给某个复杂的列表排序
lst = [
    {'name':'张三','age':31},
    {'name':'李四','age':17},
    {'name':'王五','age':20}
]

lst.sort(key = lambda x : x['age'], reverse = True)
print(lst)
