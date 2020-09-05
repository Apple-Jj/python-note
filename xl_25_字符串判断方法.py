# 1、判断空白字符
space_str = "   "
print(space_str.isspace())

# 2、判断数字的三种方法
# 三种方法都不能判断小数

# unicode 字符串
num_str2 = "\u00b2"
print(num_str2)
# 中文数字
num_str3 = "一千零一"

num_str = "1"
print(num_str)
print(num_str3.isdecimal())  # 只能识别整数
print(num_str3.isdigit())  # 识别数字和特殊字符unicode(只是数字)
print(num_str3.isnumeric())  # 识别数字、特殊字符和中文数字

"""
查找和替换
"""
# 1、判断是否已指定字符串开始
hello_str = "hello hello"
print(hello_str.startswith("hello"))
# 判断是否以指定字符串结尾
print(hello_str.endswith("hello"))
# 2、查找指定字符串
# index 同样可以查找指定的字符串位置
# index 如果指定位置没有字符串存在，会报错
# find  如果指定的不存在，会返回 -1
print(hello_str.find("llo"))
print(hello_str)


# 3、替换字符串
# replace 方法执行后会返回一个字符串
# 注意： 不会修改原有的字符串
print(hello_str.replace("hello", "world"))
print(hello_str)

"""
对齐方式
"""
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河如水流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    # print("|%s|" % poem_str.center(20, "　"))
    print("|%s|" % poem_str.strip().center(20, "　"))
# 左对齐 ljust
# 右对齐 rjust
"""
去除空白: strip:两边
         lstrip:左边
         rstrip:右边
"""

"""
切片
"""
num_str = "0123456789"
print(num_str[2:6])  # 截取2-5的字符串
print(num_str[2:])  # 截取2到末尾
print(num_str[:])  # 截取完整的字符串
print(num_str[::2])  # 每隔一个字符
print(num_str[-1::-1])  # 逆序
print(num_str[::-1])
print("1" < "2")

