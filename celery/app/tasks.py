from celery import Celery
from kombu import serialization

app = Celery('tasks', broker='redis://:123456@127.0.0.1:6379/0')




@app.task
def add(x, y):
    return x + y

# 启动worker: celery -A tasks worker --loglevel=info
