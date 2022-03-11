from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_success():
    test_customer = Customer("Joe", "Rag", 0)
    result = customer_dao.create_customer(test_customer)
    assert result.custom_id_number != 0


def test_catch_non_unique_id():
    test_customer = Customer("Abe", "Lincoln", 1)
    result = customer_dao.create_customer(test_customer)
    assert result.custom_id_number != 1


"""Get Customer Info Section"""


def test_get_customer_info_by_id_success():
    result = customer_dao.get_customer_info_by_id(1)
    assert result.custom_id_number == 1


def test_get_customer_using_nonexistent_id():
    try:
        customer_dao.get_customer_info_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"

    """update team test"""


def test_update_cust_using_nonexistent_id():
    try:
        new_cust_name = Customer("Charlie", "Williams", 0)
        customer_dao.update_customer_by_id(new_cust_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"


"""delete customer tests"""


def test_delete_cust_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result


def test_delete_cust_with_nonexistent_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"
