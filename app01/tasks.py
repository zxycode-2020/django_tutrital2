import datetime


from app01.models import Class, Student
from django_tutrital2.celery import app

import logging
from celery import shared_task

logger = logging.getLogger(__name__)

today = datetime.date.today()


@app.task()
def say_hello():
    print("hello celery")
    return "hello celery 定时任务"
