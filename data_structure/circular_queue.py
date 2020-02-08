class CircularQueue:
    """环形队列"""
    def __init__(self):
        """初始化，定义队列容量，定义队列头部指针（front）和尾部指针（rear）"""
        self.max_queue = 5
        self.queue = [None] * self.max_queue
        self.front = self.rear = -1

    def is_empty(self):
        """判断队列是否为空"""
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        """判断队列是否已满"""
        if self.rear - self.front == self.max_queue:  # 用尾部指针和头部指针的距离来判断队列是否已满
            return True
        else:
            return False

    def enter_queue(self, data):
        """向队列中加入数据"""
        if self.is_full():  # 队列已满就不能加入数据
            print("队列已满，无法再加入")
        else:
            self.rear += 1  # 尾部指针向后移动一位
            data_index = (self.rear + 1) % self.max_queue - 1  # 根据尾部指针计算出新加入的数据应该在列表的哪个位置（索引）
            if data_index == -1:  # 如果data_index == -1，说明该新加入的数据应该在列表的最后一个索引位置
                data_index = self.max_queue - 1  # 计算出列表的最后一个索引位置
            self.queue[data_index] = data  # 将数据放入队列（列表）中
            print("加入队列成功")

    def del_queue(self):
        """从队列中取出数据"""
        if self.is_empty():  # 队列已空就不能再取出数据了
            print("队列已空，无法再删除")
        else:
            self.front += 1  # 头部指针向后移动一位
            data_index = self.front % 5  # 计算出需要取出的数据所在列表中的索引位置
            data = self.queue[data_index]  # 拿到该数据
            print("取出数据：", data)
            self.queue[data_index] = None  # 取出后将队列（列表中的该位置重置为None）

    def show(self):
        """展示队列"""
        if self.is_empty():
            print("队列为空，无法显示")
            return
        num = 0  # 该变量用来计数，表示拿到第几个数据了
        while True:
            num += 1
            data_index = (self.front + num) % 5  # 获取当前数据索引
            data = self.queue[data_index]  # 拿到数据
            print(data, end=' ')
            if self.front + num == self.rear:  # 当前情况表示已经拿完了队列中的最后一个数据，所以要跳出循环
                break
        print()


if __name__ == '__main__':
    cir_queue = CircularQueue()
    while True:
        num = input("1.存入队列   2.取出队列   3.查看队列   4.退出\n请输入：")
        if num == '1':
            try:
                data = int(input("输入存入数据："))
            except ValueError:
                print("输入数据错误")
                continue
            cir_queue.enter_queue(data)
        elif num == '2':
            cir_queue.del_queue()
        elif num == '3':
            cir_queue.show()
        elif num == '4':
            print("成功退出")
            break
        else:
            print("输入选项错误，请重新输入")
