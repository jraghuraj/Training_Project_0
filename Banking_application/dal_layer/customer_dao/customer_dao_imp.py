from abc import ABC

from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_information import Customer


class CustomerDAOImp(CustomerDAOInterface, ABC):
    customer_list = []

    # id_generator = 2

    def __init__(self):
        cust_needed_for_id_catch = Customer("Alfred", "Wayne", 1)

        self.customer_list = []
        self.id_generator = 2
        self.customer_list.append(cust_needed_for_id_catch)

    def create_customer(self, customer_name: Customer) -> Customer:
        customer_name.custom_id_number = self.id_generator
        self.id_generator += 1
        self.customer_list.append(customer_name)
        return customer_name

    def get_customer_info_by_id(self, cust_id_number: int) -> Customer:
        for customer_name in self.customer_list:
            if customer_name.custom_id_number == cust_id_number:
                return customer_name
        raise IdNotFound("No Customer matches the id given: please try again")

    def update_customer_by_id(self, customer_name: Customer) -> Customer:
        for old_customer in self.customer_list:
            if customer_name.custom_id_number == old_customer.custom_id_number:
                old_customer = customer_name
                return old_customer
        raise IdNotFound("No Customer matches the id given: please try again")

    def delete_customer_by_id(self, cust_id_number: int) -> bool:
        for customer_name in self.customer_list:
            if customer_name.custom_id_number == cust_id_number:
                self.customer_list.remove(customer_name)
                return True
        raise IdNotFound("No Customer matches the id given: please try again")
