from abc import ABCMeta, abstractmethod


class RepositoryInterface(metaclass=ABCMeta):
    """
    Interface for repository.

    This interface defines methods that must be implemented by any class
    acting as a repository for order data. By adhering to this interface,
    classes ensure consistent behavior for accessing order information
    regardless of their specific implementations.

    By using this interface, you can easily swap out different repository
    implementations without affecting other parts of the application that
    depend on orders.
    """

    @abstractmethod
    def get_orders(self, user_id: int):
        """
        Retrieve all orders by user ID.

        :param user_id: (int)
        :return: orders: (list(Order)) List of user orders
        """
        pass

    @abstractmethod
    def delete_order(self, order_id) -> str:
        """
        Delete order by order id and return message

        :param order_id:
        :return: message (str)
        """
        pass
