class Player:
    """节点类"""
    def __init__(self):
        """初始化姓名，分数，指针"""
        self.name = ''
        self.score = 0
        self.next = None


def ergodic(head, num=None, is_print=False):
    """遍历函数，num是遍历到哪一个位置序号，is_print是否触发打印方法"""
    if head.next is None:
        return None
    ptr = head
    count = 0
    while True:
        count += 1
        if is_print:
            print('No.'+str(count), ptr.name, ptr.score, '--->', ptr.next.name)
        if count == num:
            break
        if ptr.next == head:
            break
        ptr = ptr.next
    return ptr  # 返回遍历完成后的最后一个节点


def invert(x):  # x是链表的第一个节点
    """反转环形链表"""
    y = x.next  # y是x原来的next
    x.next = ergodic(x)  # 将第一个节点的next指向最后一个节点(因为反转了)
    while True:  # 循环反转后面的所有节点
        r = y.next
        y.next = x
        if r == head:  # r是head说明y已经是原本链表的最后一个节点了
            return y  # 返回y，这个y是反转后的链表的第一个节点
        x = y
        y = r


head = Player()
ptr = head


while True:
    select = input("(1).新增   (2).查看   (3).插入   (4).删除   (5).反转   (6).离开\n输入：")
    if select == "1":  # 新增节点
        ptr = ergodic(head)  # 获取当前链表最后一个节点
        if ptr is None:  # ptr为None说明当前在添加第一个节点head
            head.name = input("姓名：")
            head.score = input("分数：")
            head.next = head
        else:  # 添加第一个节点之后的节点
            next_data = Player()
            next_data.name = input("姓名：")
            next_data.score = input("分数：")
            next_data.next = head
            ptr.next = next_data

    elif select == "2":  # 遍历查看链表所有节点
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
        if num == 1:  # 如果插入位置是1的话，那么head将发生变化
            head = insert_data

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
        if ptr == ergodic(head, num):  # 输入序号过大时需要做特殊处理，因为输入序号过大也代表删除最后一个节点，那么这时我需要获取这最后一个节点的前一个节点
            ptr = ergodic(ptr)
        ptr.next = ptr.next.next
        if num == 1:  # 如果删除位置是1的话，那么head将发生变化
            head = ptr.next

    elif select == '5':  # 反转链表
        new_first = invert(head)  # 获取新的第一个节点
        head = new_first  # head指向新的第一个节点
        print('成功反转')

    elif select == '6':
        print("成功离开")
        break
    else:
        print("输入错误，请重试")
