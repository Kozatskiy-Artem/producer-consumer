import random

from celery import shared_task, current_task

from .models import CustomUser, Order


@shared_task
def create_order():
    users = list(CustomUser.objects.all())
    employee = random.choice(users)
    order = Order.objects.create(
        task_id=current_task.request.id,
        name="Some name",
        description="Some description",
        employee=employee
    )
    print(order)
