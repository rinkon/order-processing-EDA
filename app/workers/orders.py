from app.workers.celery_app import celery_app
from time import sleep
from app.database.db import session
from app.models.order import Order, OrderStatus


@celery_app.task(name="order_process")
def process_order(order_id: int):
    print(f"order processing started.....{order_id}")
    sleep(3)
    db = session()
    try:
        db_order = db.query(Order).filter(Order.id == order_id).first()
        db_order.order_status = OrderStatus.COMPLETED
        db.commit()
    finally:
        db.close()
    print(f"Order Processed..{order_id}")
