class Node:
    """链表节点类"""
    def __init__(self):
        self.data = 0
        self.next = None


class LinkedListStack:
    """链表结构堆栈类"""
    def __init__(self):
        """初始化堆栈的属性"""
        self.head = Node()
        self.top = self.head  # 堆栈的顶端，当前表示堆栈为空

    def is_empty(self):
        """判断堆栈是否为空"""
        if self.top == self.head:
            return True
        else:
            return False

    def push(self, data):
        """向堆栈中存入数据"""
        new_node = Node()
        new_node.data = data
        self.top.next = new_node
        self.top = new_node
        print("成功存入数据")

    def pop(self):
        """从堆栈中取出数据"""
        if self.is_empty():
            print("堆栈已空，不能再取数据")
        else:
            print("取出：%s" % self.top.data)
            ptr = self.head
            while True:
                if ptr.next == self.top:
                    ptr.next = None
                    self.top = ptr
                    break
                ptr = ptr.next

    def show(self):
        """堆栈展示"""
        if self.top == self.head:
            print('堆栈为空')
        else:
            ptr = self.head.next
            li = []
            while True:
                li.append(ptr.data)
                if ptr.next is None:
                    break
                ptr = ptr.next
            width = 10
            for data in li[::-1]:
                str_data = str(data)
                if len(str_data) >= width:
                    show_str = '|' + str_data + '|'
                else:
                    space_num = width - len(str_data)
                    if space_num % 2 == 1:
                        left_space_num = space_num // 2 + 1
                        right_space_num = space_num // 2
                    else:
                        left_space_num = right_space_num = space_num // 2
                    show_str = '|' + ' ' * left_space_num + str_data + ' ' * right_space_num + '|'
                print(show_str)
            print('-' * (width + 2))


if __name__ == '__main__':
    list_stack = LinkedListStack()
    while True:
        num = input("1.存入数据   2.取出数据   3.查看数据   4.退出\n请输入：")
        if num == '1':
            try:
                data = int(input("输入存入数据："))
            except ValueError:
                print("输入数据错误")
                continue
            list_stack.push(data)
        elif num == '2':
            list_stack.pop()
        elif num == '3':
            list_stack.show()
        elif num == '4':
            print("成功退出")
            break
        else:
            print("输入选项错误，请重新输入")
