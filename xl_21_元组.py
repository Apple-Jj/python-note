"""
元组: Tuple
        Tuple(元组)使用方法基本与列表类似，不同之处在于 元组的 元素不能修改
        元组： 由多个元素组成的序列
        元组 用于存储一串信息，数据之间用 ， 隔开
        元组用（）定义
        元组的索引从 0 开始
创建空元组 ： empty_tuple = ()
元组中 只包含一个元素 时，需要在 元素后面 添加一个逗号 ，
注意： 定义完成后 不能 修改数据 ！！！！

    函数的 参数和返回值，一个函数可以接收 任意多个参数，或者一次返回多个数据
    格式化字符串，格式化字符串后面的（）本质上就是一个元组
    让列表不可以被修改，以保护数据的安全
"""
#  定义
info_tuple = ("张三", "张三", "18", 1.75)
print(info_tuple)
print(type(info_tuple))

#  索引
print(info_tuple[0])

#  创建空元组
empty_tuple = ()

#  只包含一个元素的元组
single_tuple = (5,)
print(type(single_tuple))

#  元组常规用法
#  取索引值
print(info_tuple.index("张三"))
#  取值
print(info_tuple[0])
#  统计
print(info_tuple.count("张三"))
#  统计元组中包含元素的个数
print(len(info_tuple))


#  循环遍历

#  1、迭代遍历
for my_info in info_tuple:
    #  使用格式化字符串拼接 my_info 这个变量不方便！！！
    #  因为元组中通常保存的数据类型是不同的
    print(my_info)
