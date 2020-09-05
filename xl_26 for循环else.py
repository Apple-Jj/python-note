for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    print("会执行么？")

print("循环结束")

student = [
    {"name": "阿土"},
    {"name": "小美"}
]
find_name = "小美"
#  在学院列表中搜索指定的姓名
for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 :%s" % find_name)
        break

print("循环结束")
