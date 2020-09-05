"""
字典 是 除了列表之外 python中最灵活的数据类型
字典同样可以存储数据
    通常用于存储 描述一个 物体 的相关信息
和列表的区别：
        列表 是 有序的集合
        字典 是 无序的集合

字典的定义：
            字典名：{}
            字典使用 键值对 存储数据，键值之间用 ， 分隔
            键 key 是索引
            值 value 是数据
            键 和 值 之间用 ： 分隔
            键 必须是唯一的
            值可以是任何数据类型，但 键 只能是 字符串、数字或元组



"""

xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75,
    "weight": 75

}
print(xiaoming)

#  取值
print(xiaoming["name"])

#  增加
xiaoming["Grade"] = 60
print(xiaoming)
#  修改
xiaoming["name"] = "王五"
print(xiaoming)
#  删除
xiaoming.pop("name")
print(xiaoming)

#  统计键值对数量
print(len(xiaoming))
#  合并字典  如果 要合并的字典中的内容重复后，数据会被覆盖
cloth_color = {
    "color": "yellow"
}
xiaoming.update(cloth_color)
print(xiaoming)
#  清空
# xiaoming.clear()
# print(xiaoming)

#  循环遍历
for k in xiaoming:
    print("%s：%s" % (k, xiaoming[k]))


str1 = "123456"
print(str1.isalnum())
