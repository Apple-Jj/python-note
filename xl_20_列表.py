"""
1、 列表
     list（列表）是 python 中使用 最频繁 的数据类型，在其他语言中通常叫做 数组
     专门用于存储 一串信息
     列表用 [] 定义，数据 之间有 ， 分离
     列表的 索引 从 0 开始
        索引 就是数据在 列表 中的位置编号， 索引 又可以被称为下标
            注意：从列表中取值时，如果 超出索引范围，程序会报错


         1、取值：使用方法： list[索引值]
            取索引：知道列表中的内容，想知道内容在列表中的位置 ：name_list.index
            使用index方法需要注意，如果传递的数据不在列表中，程序会报错

         2、修改： name_list[要修改的索引值] = "想要修改后的内容"
                要修改的索引超出索引值的话，程序会报错

         3、增加：name_list.append("要增加的数据") : 可以向列表的末尾增加数据
                 name_list.inset(要插入位置的索引值(int),"插入的数据"))：指定的位置插入数据
                 name_list.extend("要插入的列表名"):把另外一个列表中的完整内容插入到 当前列表的末尾

         4、删除：1、
                     name_list.remove("要删除的数据"):可以从列表中 删除指定的数据，多个重复的数据。默认删除第一个
                     name_list.pop(""): 括号内 ：没有参数 删除末尾的数据
                                           ： 有参数  要删除指定位置的索引内容
                     name_list.clear(): 清空列表
                 2、
                     del 列表[索引] ：删除指定索引的数据
                               注意 ： del 删除的数据 是从内存中删除的 后续是不可以使用的
                 提示 ：在日常开发中，要从列表中删除数据，建议使用列表中提供的方法

         5、统计： len("列表名") ： len_list = len(name_list) : 统计列表在元素的总数
                   count        : 统计列表中某一数据出现的次数
                注意： 如果 在 统计完之后 ，出现了 remove 删除，这是默认删除第一个 出现的数据
         6、排序：
                1、 升序：sort：列表名.sort()：英文字母是按照 字母表排序，数字按照从小到大排序
                2、 降序：      列表名.sort(reverse = True)：reverse = False 表示升序 ，True 表示升序
                3、 逆序（反转）：列表名.reverse: 列表中的数据全部反转
         7、循环遍历
                遍历：从头到尾依次 列表 中获取数据
                     在 循环体内部 针对每一个元素 ，执行相同的操作
                在 python 中为了提高列表达到遍历效率，专门提供 迭代 iteration 遍历
                for 就能够实现迭代 : for 变量（随便定义） in 列表名：
                                        ... 要循环的操作内容
                 顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在 变量 当中

"""

name_list = ["张三", "李四", "王五"]

print(name_list[0])  # 索引使用

print(name_list.index("张三"))
#  修改
name_list[0] = "赵六"
print(name_list)
#  增加
name_list.append("王小二")
name_list.insert(1, "小美眉")
print(name_list)

temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)
#  删除
name_list.remove("赵六")
print(name_list)

name_list.pop()
print(name_list)
name_list.pop(3)
print(name_list)

del name_list[1]
print(name_list)

name_list.clear()
print(name_list)

#  统计
name_list = ["张三", "赵四", "王五", "张三"]
list_len = len(name_list)
print("列表中包含的元素：%d" % list_len)

count = name_list.count("张三")
print("张三出现了：%d 次" % count)

#  排序
name_list = ["张三", "赵四", "王五", "王小二"]
num_list = [6, 8, 5, 1, 10, 20, 11]
# 升序
name_list.sort()
num_list.sort()
print(num_list)
print(name_list)
#  降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)
#  逆序（反转）
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)

#  迭代遍历

name_list = ["张三", "李四", "王五"]
for my_name in name_list:
    print("我的名字叫：%s" % my_name)
