# 插入排序

from random import randint

li = [randint(1, 100) for n in range(10)]

print("初始列表：", li)

for i in range(1, len(li)):  # 因为开始就需要拿第2个元素来和第一个元素比较，所以从索引为1的元素（即列表的第二个元素）开始
    tmp = li[i]  # 将要插入的值保存起来
    no = i - 1
    while no >= 0 and tmp < li[no]:  # 将要插入的值依次和该值前面的所有值进行比较
        li[no+1] = li[no]
        no -= 1
    li[no+1] = tmp

    print("第%s次排序后：" % i, li)

print("完成排序后：", li)
