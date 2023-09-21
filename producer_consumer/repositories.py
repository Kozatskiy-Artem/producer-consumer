from datetime import datetime

from .models import Order
from .interfaces import RepositoryInterface


class Repository(RepositoryInterface):
    """
    The Repository class handles the retrieval of order data from the data storage.
    """

    def get_orders(self, user_id: int) -> list[Order]:
        """
        Retrieve all orders by user ID.

        :param user_id: (int)
        :return: orders: (list(Order)) List of user orders
        """
        orders = Order.objects.filter(employee=user_id)
        return list(orders)

    def delete_order(self, order_id) -> str:
        """
        Delete order by order id and return message

        :param order_id:
        :return: message (str)
        """
        order = Order.objects.get(pk=order_id)

        message = f"Задача №{order.pk}-{order.task_id} пiд назвою {order.name}" \
                  f" була опрацьована {order.employee.first_name + ' ' + order.employee.position} у {datetime.now()}"

        order.delete()

        return message
