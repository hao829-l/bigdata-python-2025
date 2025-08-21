def test1():
    print('hi,执行函数test1')
    return 1,5

result = test1()
print(result)


def test2(x,y):
    x2 = x ** 2
    y2 = y ** 2
    return x2, y2          # return一执行后续代码会中断
    print(126)

result = test2(3,4)
r1,r2 = test2(3,4)
print(result,type(result))