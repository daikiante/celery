from time import sleep
from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def f():
    print('f関数開始')
    sleep(5)
    print('f関数終了')


def test():
    print('テスト開始')
    f.delay()
    print('テスト終了')


if __name__ == '__main__':
    test()