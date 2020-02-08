class Player:
    """节点类"""
    def __init__(self):
        """初始化姓名，分数，指针"""
        self.name = ''
        self.score = 0
        self.rlink = None
        self.llink = None


def ergodic(head, num=None, is_print=False, left=False):
    """遍历函数，num是遍历到哪一个位置序号，is_print是否触发打印方法，left表示是否由head开始往左遍历"""
    ptr = head
    count = 0
    while True:
        if num == count:
            break

        if not left:
            if ptr.rlink != head:
                ptr = ptr.rlink
            else:
                break
        else:
            if ptr.llink != head:
                ptr = ptr.llink
            else:
                break
        count += 1
        if is_print:
            print('No.'+str(count), ptr.llink.name if ptr.llink != head else 'head', '<---',
                  ptr.name, ptr.score, '--->', ptr.rlink.name if ptr.rlink != head else 'head')
    return ptr  # 返回遍历完成后的最后一个节点


head = Player()  # 初始化一个链表头指针，不用来存放任何数据
head.rlink = head  # 初始化右指针
head.llink = head  # 初始化左指针


while True:
    select = input("(1).新增   (2).查看   (3).插入   (4).删除   (5).离开\n输入：")
    if select == "1":  # 新增节点，分为右新增和左新增
        direction = input("(1).右新增   (2).左新增\n输入：")
        if direction not in ("1", "2"):
            print("输入错误")
            continue
        new_data = Player()
        new_data.name = input("姓名：")
        new_data.score = input("分数：")
        if direction == "1":  # 右新增
            ptr = ergodic(head)  # 从head开始向右遍历获取最后一个节点
            ptr.rlink = new_data
            new_data.llink = ptr
            new_data.rlink = head
            head.llink = new_data
        else:  # 左新增
            ptr = ergodic(head, left=True)  # 从head开始向左遍历获取最后一个节点
            ptr.llink = new_data
            new_data.rlink = ptr
            new_data.llink = head
            head.rlink = new_data

    elif select == "2":  # 遍历查看所有节点，分为右遍历和左遍历
        direction = input("(1).右遍历   (2).左遍历\n输入：")
        if direction == "1":  # 右遍历
            ergodic(head, is_print=True)
        elif direction == "2":  # 左遍历
            ergodic(head, is_print=True, left=True)
        else:
            print("输入错误")

    elif select == '3':  # 插入节点，分为右插入和左插入
        direction = input("(1).右插入   (2).左插入\n输入：")
        if direction not in ("1", "2"):
            print("输入错误")
            continue
        try:
            num = int(input("请输入需要插入的节点位置序号："))
            if num < 1:
                print("输入必须为大于0的正整数")
                continue
        except ValueError:
            print("输入有误")
            continue
        insert_data = Player()
        insert_data.name = input("姓名：")
        insert_data.score = input("分数：")
        if direction == "1":  # 右插入
            ptr = ergodic(head, num - 1)  # 获取需要插入位置的前一个节点，新插入的节点就在这个节点的后面
            insert_data.llink = ptr
            insert_data.rlink = ptr.rlink
            ptr.rlink = insert_data
            insert_data.rlink.llink = insert_data
        else:  # 左插入
            ptr = ergodic(head, num - 1, left=True)
            insert_data.rlink = ptr
            insert_data.llink = ptr.llink
            ptr.llink = insert_data
            insert_data.llink.rlink = insert_data

    elif select == '4':  # 删除节点，分为右删除和左删除
        direction = input("(1).右删除   (2).左删除\n输入：")
        if direction not in ("1", "2"):
            print("输入错误")
            continue
        try:
            num = int(input("请输入需要删除的节点位置序号："))
            if num < 1:
                print("输入必须为大于0的正整数")
                continue
        except ValueError:
            print("输入有误")
            continue
        if direction == "1":  # 右删除
            ptr = ergodic(head, num)  # 获取需要删除的节点
        else:  # 左删除
            ptr = ergodic(head, num, left=True)
        ptr.llink.rlink = ptr.rlink
        ptr.rlink.llink = ptr.llink

    elif select == '5':
        print("成功离开")
        break
    else:
        print("输入错误，请重试")
