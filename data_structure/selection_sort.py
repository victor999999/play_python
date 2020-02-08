# 选择排序

from random import randint

li = [randint(1, 100) for n in range(10)]  # 生成一个由10个1到100内的随机整数组成的列表

print("初始列表：", li)

for i in range(len(li)-1):  # 总共需要进行多少轮的排序，因为最后一轮是从两个元素取出最小的，所以轮数是列表的长度减1，i表示现在在选择一个数放在i位置
    for j in range(i+1, len(li)):  # 用当前i位置的数依次和它后面的所有数进行比较选出最小的
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]

    print("第%s次排序后：" % (i + 1), li)

print("完成排序后：", li)
