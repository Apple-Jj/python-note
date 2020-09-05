row = 1
while row <= 9:
    col = 1
    while col <= row:
        # print("*", end="")
        result = row * col
        print("%d * %d = %d" % (col, row, result), end="\t")
        col += 1
    # print("%d" % row)
    print("")
    row += 1
"""
转义字符:
     \t :   在控制台输出一个 制表符，协助在输出文本时 垂直方向 保持对齐
     \n :   在控制台输出一个 换行符
     \\	反斜杠符号
     \'	单引号
     \"	双引号
     \a	响铃
     \b	退格(Backspace)
     \000	空
     \n	换行
     \v	纵向制表符
     \t	横向制表符
     \r	回车
     \f	换页
"""
# print("1\t 2\t 3")
# print("10\t 20\t 30")
# print("\"hello\"hello")
