name = '王2'
age = 20
city = '湖北'

print('我的名字是%s，我的年龄是%d,我所在的城市是%s' % (name,age,city))    #使用占位符进行格式化输出

money = 1234
num = 1.78
num02 = 58.437

print('我的存款是:%5d' % money)
print('我的存款是:%d' % money)
print('我的身高是:%.1f' % num)   #精确到小数点后一位（四舍五入）
print('我的体重是:%.2f' % num02)   #精确到小数点后二位（四舍五入）


# 第二种格式化输出
print(f'我的名字是{name},我的年龄是{age+1},我所在的城市是{city}')



