"""
% 的字符串叫做 格式化字符串
%s 字符串
%d 有符号的十进制整数，%06d 整数显示位数，不足的补零 .06 表示位数
%f 浮点数，%.02f 表示小数点后显示两位 . 02表示小数位数
%% 输出%

print(end=""）表示不会换行
"""
name = input("请输入名字")
student_no = int(input("请输入学号"))
price = float(input("请输入苹果价格"))
weight = float(input("请输入购买苹果数量"))
money = price * weight
scale = float(input("请输入比例"))
print("我的名字叫 %s ，请多多关照" % name)
print("我的学号是 %03d" % student_no)
print("苹果单价是 %0.2f , 苹果购买的数量是 %0.3f , 支付金额是 %0.4f" % (price, weight, money))
print("输出比例是 %.02f%%" % (scale * 100))
