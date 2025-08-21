def my_abs(num):
    """
    该函数用来返回一个数字的绝对值。
    :param num: 传入的数字，必须是个数字，而且必传。
    :return: 返回传入的数字的绝对值。
    """
    if num < 0:
        return -num
    else:
        return num

def new_abs(num:int) -> int:
    """
    该函数用来返回一个数字的绝对值。
    :param num: 传入的数字，必须是个数字，而且必传。
    :return: 返回传入的数字的绝对值。
    """
    if num < 0:
        return -num
    else:
        return num

print(my_abs(-5))
print(new_abs(-8))