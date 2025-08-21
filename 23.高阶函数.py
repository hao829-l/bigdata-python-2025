# 对任意两个数字，整理之后再求和

def sum_num(a,b):
    return abs(a) + abs(b)      # abs:绝对值函数

# 高阶函数的实现

def sum_num2(a,b,f):
    """

    :param a:
    :param b:
    :param f: 就是对两个数字进行整理的函数
    :return:
    """
    return f(a) + f(b)

print(sum_num2(2,-8,abs))

# 通过平方整理后求和

print(sum_num2(-2,-6,lambda n: n ** 2))

# 第二种高阶函数

def test3(*args):
    def sum_nums():
        sum = 0
        for n in args:
            sum += n
        return sum
    return sum_nums

print(test3(2,4,6,8,10))
print(test3(2,4,6,8,10)())



