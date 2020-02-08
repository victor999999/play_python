# 冒泡排序

from random import randint

li = [randint(1, 100) for n in range(10)]  # 生成一个由10个1到100内的随机整数组成的列表

print("初始列表：", li)

for i in range(len(li)-1):  # 总共需要进行多少轮的排序，因为最后一轮是由两个元素进行比较，所以轮数是列表的长度减1
    for j in range(len(li)-1-i):  # 比较相邻的两个元素
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]  # 相邻元素交换顺序
    print("第%s次排序后：" % (i + 1), li)

print("完成排序后：", li)
