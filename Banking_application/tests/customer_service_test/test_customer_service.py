from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer import customer_dao
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
non_string_first_name = Customer(9, "Molly", 3)
non_string_last_name = Customer("Patrick", 29, 3)
first_name_too_long = Customer("Optimus Prime Omega the large", "Autobot", 3)
last_name_too_long = Customer("Patrick", "Adventures of the mighty man", 3)


def test_check_no_duplicate_id_numbers():
    test_customer = Customer("Jester", "Washington", 1)
    result = customer_dao.create_customer(test_customer)
    assert result.custom_id_number != 1


def test_check_non_string_first_name_create_customer():
    try:
        customer_service.service_create_customer(non_string_first_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid first name"


def test_check_non_string_last_name_create_customer():
    try:
        customer_service.service_create_customer(non_string_last_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid last name"


def test_check_first_name_length_too_long():
    try:
        customer_service.service_create_customer(first_name_too_long)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid first name"


def test_check_last_name_length_too_long():
    try:
        customer_service.service_create_customer(last_name_too_long)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid last name"


def test_cant_typecast_to_int():
    try:
        customer_service.service_get_customer_by_id("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "No Customer matches the id given: please try again"


def test_get_customer_successfully_typecast_string():
    result = customer_service.service_get_customer_by_id("1")
    assert result.custom_id_number == 1


def test_catch_non_string_first_name_update():
    try:
        customer_service.service_update_customer_by_id(non_string_first_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid first name"


def test_catch_non_string_last_name_update():
    try:
        customer_service.service_update_customer_by_id(non_string_last_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid last name"


def test_catch_non_numeric_id_delete_customer():
    try:
        customer_service.delete_customer_by_id("one")
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"


def test_delete_customer_with_nonexistent_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"
