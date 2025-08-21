#  获取数据
s = float(input('请输入你的身高（单位：米）：\t'))            #转义字符\t：制表符（一个tab键的距离）
t = float(input('请输入你的体重（单位：千克）：\t'))

#  开始计算
bmi = t / s ** 2    #bim=身高除以体重的平方          结果得到一个float
print(f'你的身高是：{s}米，',end ='')
print(f'你的体重是：{t}千克，',end ='')
print(f'你的bmi的计算结果是：%.2f' % bmi)



