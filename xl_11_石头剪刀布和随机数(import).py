"""
import 导入模块（工具包） 的使用

需求：
    1、由控制台输入要出的拳：石头（1）、剪刀（2）、布（3）
    2、电脑随机出拳--先假定电脑只会出石头
    3、比较胜负
"""
# 导入数据包
# 注意，再导入数据包的时候用改将导入的语句放在文件的顶部
import random

player = int(input("请输入您要出的拳：(石头（1）、剪刀（2）、布（3）)"))
computer = random.randint(1, 3)       # 增加随机数
print("玩家选择的拳头是: %d ,电脑选择的拳头是: %d " % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("恭喜您 赢了！！")
elif player == computer:
    print("平局")
else:
    print("不服气，我们决战到天亮!!")

"""
随机数 的处理
import random 中
               1、randint 函数：随机整数 random.randint(a, b),返回a，b之间的整数，包含a，b
                  random.randint(10, 20):生成的随机数n：10 <= n <= 20
                  random.randint(20, 20):随机数永远都是20
                  random.randint(20, 10):该语句错误，下限要小于上限
               2、random.random():随机的浮点数 没有限制
               3、random.uniform(a, b):生成上线为b，上限为a的浮点数   a <= n <= b
                  如果a > b，则生成的随机数n: b <= n <= a。如果 a <b， 则 a <= n <= b
                  random.uniform(10, 20):生成的随机数n: 10 <= n <= 20 结果：18.7356606526
                  random.uniform(20, 10):生成的随机数n: 20 <= n <= 10 结果：13.5798298022   
               4、random.randrange的函数原型为：random.randrange([start], stop[, step])，
                                               从指定范围内，按指定基数递增的集合中 获取一个随机数。
                  random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
                  random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效
               5、　random.choice从序列中获取一个随机元素。
                   其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
                   这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
                   print random.choice("学习Python")   
                   print random.choice(["JGood", "is", "a", "handsome", "boy"])  
                   print random.choice(("Tuple", "List", "Dict"))  
               6、　random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱
                   p = ["Python", "is", "powerful", "simple", "and so on..."]  
                   random.shuffle(p)  
                   print p    
                   ['powerful', 'simple', 'is', 'Python', 'and so on...']  
               7、　random.sample的函数原型为：random.sample(sequence, k)，
                   从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
                   list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
                   slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
                   print slice  
                   print list #原有序列并没有改变。  
   
               
"""
