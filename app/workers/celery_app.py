from time import sleep
from celery import Celery

celery_app = Celery('celery_app',broker="amqp://guest:guest@localhost:5672")
celery_app.autodiscover_tasks()


@celery_app.task
def process_order(order_id: int):
    print("order processing started.....")
    sleep(3)
    print("Order Processed")

