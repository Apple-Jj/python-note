"""
函数的嵌套调用：

"""


# def test1():
#     print("*" * 50)
#
#
# def test2():
#     print("-" * 50)
#     test1()
#     print("+" * 50)
#
#
# test2()

"""
打印 分隔线
"""
# 需求1、 定义函数 print_line 函数能够打印 * 组成的一条 分割线


# def print_line():
#     print("*" * 50)
#
#
# print_line()

# 需求2、 定义一个函数能够打印 由任意字符串组成 的分隔线

# def print_line(char):
#
#     print(char * 50)
#
#
# print_line("-")

# 需求3、 定义一个函数能够打印 任意重复次数 的分隔线
# def print_line(char, times):
#     print(char * times)
#
#
# print_line("-", 5)

# 需求3、 定义一个函数能够打印 5行的分隔线，分隔线要求符合需求3
def print_line(char, times):

    print(char * times)


def print_lines(char, times):
    """
    打印多行分隔线

    :param char:分隔线使用的分割字符
    :param times:分隔线重复的次数
    """
    row = 0
    while row <= 4:
        print_line(char, times)
        row += 1


name = "模块练习"
