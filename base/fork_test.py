import os
from time import sleep

print('***********************')
a = 1

pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print('这是新的进程')
    print("a =",a)
    a = 10000
else:
    sleep(1)
    print("这是原有进程")
    print("psarent a =",a)

print("演示完毕")
