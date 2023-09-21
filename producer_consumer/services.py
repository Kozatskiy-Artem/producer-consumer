from .interfaces import RepositoryInterface
from .models import Order


class Service:
    """
    The Service class is responsible for interacting with the data storage layer and encapsulated
    the application`s core business logic.
    """

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def get_orders(self, user_id: int) -> list[Order]:
        """
        Retrieve all orders by user ID.

        :param user_id: (int)
        :return: orders: (list(Order)) List of user orders
        """

        return self.repository.get_orders(user_id)

    def delete_order(self, order_id: int) -> str:
        """
        Delete order by order id and return message

        :param order_id:
        :return: message (str)
        """
        return self.repository.delete_order(order_id)
