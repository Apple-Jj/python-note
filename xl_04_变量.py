"""
变量名 只有在 第一次出现时 才算定义变量
"""

qq_number = 123
qq_password = 456
print(qq_number)
print(qq_password)

"""
  eg ：超市买苹果
  价格 8.5 元
  买了 7.5 斤 苹果
  计算付款金额
  只要买苹果 就反5元
"""
price = 8.5
weight = 7.5
money = price * weight
money = money - 5
print(money)

"""
变量的数据类型
在python定义变量类型时 是不需要指定变量类型的；
在运行的时候python解释器会根据等号右边的内容来准确推导出变量的类型

数字型：
      int(整型)
      float(浮点型)
      bool(布尔型) -- 非零即真
        True 真 (非零数) 
        false 假 （0）
      complex(复数型)

非数字型：
      字符串（引号内容）str
      列表
      元组
      字典      










eg:保存信息
姓名：小明     str 字符串
年龄：18       int 整型
性别：是男生   bool 布尔类型，真 True或者假 False 
身高：1.75     float 浮点数,小数类型
体重：75.0公斤 75 int 75.0 float
"""
name = "小明"
print(name)
age = "18岁"
print(age)
gender = True
height = "1.75m"
print(height)
weight = "75.0kg"
print(weight)






