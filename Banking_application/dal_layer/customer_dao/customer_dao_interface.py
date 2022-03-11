from abc import ABC, abstractmethod

from entities.customer_class_information import Customer


class CustomerDAOInterface(ABC):

    # create
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # read
    @abstractmethod
    def get_customer_info_by_id(self, cust_id_number: int) -> Customer:
        pass

    # update
    @abstractmethod
    def update_customer_by_id(self, customer_name: Customer) -> Customer:
        pass

    # delete
    @abstractmethod
    def delete_customer_by_id(self, cust_id_number: int) -> bool:
        pass
