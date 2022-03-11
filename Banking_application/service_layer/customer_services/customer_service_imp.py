from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from entities.customer_class_information import Customer
from service_layer.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def service_create_customer(self, customer_name: Customer) -> Customer:
        if type(customer_name.first_name) != str:
            raise BadCustomerInfo("Please pass in a valid first name")
        elif len(customer_name.first_name) >= 20:
            raise BadCustomerInfo("Please pass in a valid first name")
        elif type(customer_name.last_name) != str:
            raise BadCustomerInfo("Please pass in a valid last name")
        elif len(customer_name.last_name) >= 20:
            raise BadCustomerInfo("Please pass in a valid last name")
        return self.customer_dao.create_customer(customer_name)

    def service_get_customer_by_id(self, cust_id_number: int) -> Customer:
        try:
            return self.customer_dao.get_customer_info_by_id(int(cust_id_number))
        except ValueError:
            raise BadCustomerInfo("No Customer matches the id given: please try again")

    def service_update_customer_by_id(self, customer_name: Customer) -> Customer:
        if type(customer_name.first_name) != str:
            raise BadCustomerInfo("Please pass in a valid first name")
        elif type(customer_name.last_name) != str:
            raise BadCustomerInfo("Please pass in a valid last name")
        return self.customer_dao.update_customer_by_id(customer_name)

    def delete_customer_by_id(self, cust_id_number: int) -> bool:
        if type(cust_id_number) == int:
            return self.customer_dao.delete_customer_by_id(cust_id_number)
        else:
            raise IdNotFound("No Customer matches the id given: please try again")
