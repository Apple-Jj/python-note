"""
逻辑运算符：与and: 条件1 and 条件2
           或or : 条件1 and 条件2
           非not: not 条件
逻辑运算符 可以把多个条件按照逻辑进行连接，变成更复杂的条件
"""
#  判断年龄0~120 age
age = int(input("请输入120以内的年龄"))
if 0 <= age <= 120:
    print(age)
else:
    print("输入错误")
#  判断成绩 python_score c_score
python_score = int(input("请输入python成绩"))
c_score = int(input("请输入c语言成绩"))
if python_score >= 60 or c_score >= 60:
    print("及格")
else:
    print("不及格")
#  判断公司员工 布尔型 is_employer
is_employer = False
if not is_employer:
    print("非本公司人员禁止入内")

