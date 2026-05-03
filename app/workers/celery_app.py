from time import sleep
from celery import Celery

celery_app = Celery('celery_app',broker="amqp://guest:guest@localhost:5672", include=["app.workers.orders"])




