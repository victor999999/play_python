class Player:
    """节点类"""
    def __init__(self):
        """初始化姓名，分数，指针"""
        self.name = ''
        self.score = 0
        self.next = None


def ergodic(head, num=None, is_print=False):
    """遍历函数，num是遍历到哪一个位置序号，is_print是否触发打印方法"""
    ptr = head
    count = 0
    while True:
        if num == count:
            break
        if ptr.next:
            count += 1
            ptr = ptr.next
            if is_print:
                print('No.'+str(count), ptr.name, ptr.score, '--->', ptr.next.name if ptr.next else None)
        else:
            break
    return ptr  # 返回遍历完成后的最后一个节点


def invert(x):  # x是链表的第一个节点(即head的指针的指向)
    """反转链表"""
    y = x.next  # y是x原来的next
    if y is None:
        return x
    x.next = None  # 将第一个节点的next指向None(因为反转了)
    while True:  # 循环反转后面的所有节点
        r = y.next
        y.next = x
        if r is None:  # r是None说明y已经是原本链表的最后一个节点了
            return y  # 返回y，这个y是反转后的链表的第一个节点
        x = y
        y = r


head = Player()


while True:
    select = input("(1).新增   (2).查看   (3).插入   (4).删除   (5).反转   (6).离开\n输入：")
    if select == "1":  # 新增节点
        ptr = ergodic(head)  # 获取当前链表最后一个节点
        next_data = Player()  # 创建一个新节点
        next_data.name = input("姓名：")
        next_data.score = input("分数：")
        next_data.next = None
        ptr.next = next_data  # 连接节点

    elif select == "2":  # 遍历查看链表所有节点
        print("所有数据显示如下：")
        ergodic(head, is_print=True)  # 遍历链表，将打印参数设为True

    elif select == '3':  # 向链表中任意位置插入节点，位置以序号表示，即第一个节点序号为1，第二个节点序号为2，以此类推
        try:
            num = int(input("请输入需要插入的节点位置序号："))  # 输入序号必须是大于0的正整数，如果输入大于最后一个节点的序号则插入到最后一个节点之后
            if num < 1:
                print("输入必须为大于0的正整数")
                continue
        except ValueError:
            print("输入有误")
            continue
        ptr = ergodic(head, num-1)  # 获取需要插入位置的前一个节点
        insert_data = Player()
        insert_data.name = input("姓名：")
        insert_data.score = input("分数：")
        insert_data.next = ptr.next
        ptr.next = insert_data

    elif select == '4':  # 删除链表中任意位置的节点
        try:
            num = int(input("请输入需要删除的节点位置序号："))  # 输入序号必须是大于0的正整数，如果输入大于最后一个节点的序号则删除最后一个节点
            if num < 1:
                print("输入必须为大于0的正整数")
                continue
        except ValueError:
            print("输入有误")
            continue
        ptr = ergodic(head, num - 1)  # 获取需要删除位置的前一个节点
        ptr.next = ptr.next.next

    elif select == '5':  # 反转链表
        new_first = invert(head.next)  # 获取新的第一个节点
        head.next = new_first  # head指向新的第一个节点
        print('成功反转')

    elif select == '6':
        print("成功离开")
        break
    else:
        print("输入错误，请重试")
