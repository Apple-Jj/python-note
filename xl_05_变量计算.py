"""
1）数字型之间可以直接进行算术运算
bool True = 1 false = 0
"""
i = 5
f = 10.5
b = True
A = i * f + b
print(A)
b = False
A = i * f * b
print(A)

""""
2）字符串型之间可通过 + 号 组成一个新的字符串
字符串之间 可通过 * 号重复拼接一个新的字符串
"""
first_name = "张"
last_name = "三"
name = first_name + last_name
print(name)
name = last_name + first_name
print(name)

i = "*" * 50
print(i)
name = (last_name + first_name) * 50
print(name)
"""
3) 数字型和字符型之间不能进行其他计算
"""
i = first_name + "10"
print(i)
