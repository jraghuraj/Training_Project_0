from abc import ABC, abstractmethod

from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_information import Customer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    @abstractmethod
    def service_create_customer(self, customer_name: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, cust_id_number: int) -> Customer:
        pass

    @abstractmethod
    def service_update_customer_by_id(self, customer_name: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self, cust_id_number: int) -> bool:
        pass
