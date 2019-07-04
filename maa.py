# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:32:18 2019

@author: lenovo
"""

##每30秒调用task.add
#from datetime import timedelta
# 
#CELERYBEAT_SCHEDULE = {
#  'add-every-30-seconds': {
#    'task': 'tasks.add',
#    'schedule': timedelta(seconds=30),
#    'args': (16, 16)
#  },
#}
#
##crontab任务
##每周一7:30调用task.add
#from celery.schedules import crontab
# 
#CELERYBEAT_SCHEDULE = {
#  # Executes every Monday morning at 7:30 A.M
#  'add-every-monday-morning': {
#    'task': 'tasks.add',
#    'schedule': crontab(hour=3, minute=35, day_of_week=1),
#    'args': (16, 16),
#  },
#}

from celery import Celery
app = Celery()
app.config_from_object("celeryconfig")
@app.task
def taskA(x, y):
    return x * y
@app.task
def taskB(x, y, z):
    return x + y + z
@app.task
def add(x, y):
    return x + y














