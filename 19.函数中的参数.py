# # 形参
def test1(x,y):
    return x+y

r1 = test1(1, 2)
print(r1)


print(test1(y=10, x=20))


# 默认值传参

def test2(x,y,init_sum=10):
    init_sum += x + y
    return init_sum

print(test2(10, 20))
print(test2(10, 20, 50))


# 不定长传参

# 不定长普通参数

def test3(*args,init_sum=10):
    print(type(args))
    if args:
        # for i in args:
        #     init_sum += i
        return init_sum + sum(args)
    return init_sum

print(test3())

print(test3(1,2,init_sum=100))

#不定长关键字参数

def test4(init_sum=10,**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f'参数的名字{k}，参数的值{v}')

    return init_sum + sum(kwargs.values())


print(test4(x=10, y=20, z=30))


# 位置参数 -->默认传参 -->不定长普通参数 -->不定长关键字参数
# def tset5( a , b , c=100 , *args , **kwargs ):