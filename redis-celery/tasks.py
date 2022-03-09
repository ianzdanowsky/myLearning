# from celery import Celery
import time

# app = Celery('tasks', broker='redis://localhost:6379/0')

# @app.task


def running(runner, vel):
    dist = 0
    while 1:
        time.sleep(2)
        dist += vel
        print("Corredor {0} esta em {1} metros".format(runner, dist))


running('Tiago Assunção', 3)
running('Leonardo Bites', 4)
running('Silvia Mendes', 5)
