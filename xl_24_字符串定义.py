"""
定义：
     如果字符串内部需要 "" ，可以使用 '' 来定义
     如果字符串内部需要 '' , 可以使用 "" 来定义


"""
str1 = "Hello python"
str2 = '我的外号是："大西瓜" '
print(str2)
print(str1[2])

for char in str2:
    print(char)

# 统计字符串长度
print(len(str1))
# 统计某一字符串出现的次数
print(str1.count("llo"))
# 统计某一字符串出现的位置
print(str1.index("p"))


