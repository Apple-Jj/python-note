"""
判断语句也成为：分支语句
if 要判断的条件：（冒号很重要）
    条件成立时：首行缩进（四个空格或者 Tab键） 建议使用空格
    Tab 和 空格 不要混用！！！
    https:zh.wikipedia.org/wiki/数字符号表
"""
age = int(input("请输入年龄"))
if age >= 18:
    print("可以进入网吧happy")
    print("")
else:
    print("禁止入内")
print("什么时候执行")
"""
if 语句进阶 ：elif
如果希望再增加一些条件，条件不同，需要执行的代码也不同时，就可以使用:elif
if 条件1:
   ...
elif 条件2:
   ...
elif 条件3:
   ...
elif 条件4:
   ...
else：  所以条件都不成立时
   ...
   
   elif 和  else 必须和 if 联合使用，而不能单独使用
   elif 判断条件之间都是评级的
"""
#  女友的生日 holiday_name
holiday_name = str(input("其请输入节日名称(平安夜，情人节，生日)"))
if holiday_name == "平安夜":
    print("买玫瑰")
    print("看电影")
elif holiday_name == "情人节":
    print("开房")
    print("吃火锅")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("每天都是节日啊~~~~~")

"""
if 的嵌套
if 条件1：
   ...
   if 条件2：
      ...
   else: 条件2 不满足的处理
      ...
else: 条件1 不满足的处理
   ...
"""
# 火车安检
# 布尔型 has_ticket(车票)
# 整型 knife_length(刀的长度) 大于20cm 不让进 小于让进
name = str(input("请输入姓名"))
has_ticket = False
has_knife = False
if name == "谢斌龙":
    if not has_ticket:
        print("可以进站")
        if not has_knife:
            print("不能通过安检")
            knife_length = int(input("输入刀的长度"))
            if knife_length >= 20:
                print("不允许上车，您的刀的长度为：%.02d cm" % knife_length)
            else:
                print("允许上车")
        else:
            print("通过安检")
    else:
        print("不可以进站")
else:
    print("没有票")

