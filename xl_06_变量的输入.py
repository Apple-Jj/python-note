"""
input 函数是接受用户从键盘出入的信息
input 输入的数据都是字符串类型 (str)
 字符串 = input("提示信息")
"""

password = input("请输入密码")
print(password, type(password))

"""
类型转换函数
int(x) 将x转换成整型
float(x) 将x转换成浮点型
"""
A = 123.0
print(A)
A = int(A)
print(A)
A = float(A)
print(A)

"""
超市买苹果

收银员输入苹果价格，单位：元/斤
收银员输入用户购买重量，单位：斤
计算并输出付款金额
"""

# 两个字符串之间不能进行乘法操作
price = float(input("请输入苹果价格"))
weight = float(input("请输入购买苹果重量"))
money = price * weight
money = int(money)
print(money)

print()


