class ListStack:
    """列表结构堆栈类"""
    def __init__(self):
        """初始化堆栈的属性"""
        self.max_stack = 10  # 定义堆栈的容量
        self.stack = [None] * self.max_stack  # 声明堆栈列表
        self.top = -1  # 堆栈的顶端，-1表示堆栈为空

    def is_empty(self):
        """判断堆栈是否为空"""
        if self.top == -1:
            return True
        else:
            return False

    def push(self, data):
        """向堆栈中存入数据"""
        if self.top >= self.max_stack - 1:
            print("堆栈已满，不能再存数据")
        else:
            self.top += 1
            self.stack[self.top] = data
            print("数据已存入堆栈")

    def pop(self):
        """从堆栈中取出数据"""
        if self.is_empty():
            print("堆栈已空，不能再取数据")
        else:
            print("取出：%s" % self.stack[self.top])
            self.stack[self.top] = None
            self.top -= 1

    def show(self):
        """展示堆栈"""
        width = 10
        for data in self.stack[::-1]:
            if data is None:
                show_str = '|' + width * ' ' + '|'
            else:
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
        print('-' * (width+2))


if __name__ == '__main__':
    list_stack = ListStack()
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
