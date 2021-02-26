import os

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    #获取当前进程的PID
    print("Child get pid:",os.getpid())
    #获取父进程的PID
    print('Child get parent pid:',os.getppid())
else:
    print("Parent get child pid:",pid)
    print("Parent get pid:",os.getpid())
