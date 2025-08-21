def test(n:int) ->int:
    """
    计算一个数字n的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return 1    # 递归函数退出的出口
    return n * test(n-1)

print(test(1))
print(test(2))
print(test(3))
print(test(4))
print(test(5))
print(test(6))
print(test(7))
print(test(8))
print(test(9))
print(test(10))