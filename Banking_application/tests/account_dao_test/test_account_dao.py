from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from entities.account_class_information import Account

account_dao: AccountDAOImp = AccountDAOImp()
test_bank_account_person = Account(1, 1, 100.00)


# create


def test_create_bank_account_success():  # Figure out how to tie the BA with specific customers
    test_bank_account = Account(1, 0, 100.00)
    result = account_dao.create_bank_account(test_bank_account)
    assert result.bad_id_number != 0


def test_catch_non_unique_bank_account_id():
    test_bank_account = Account(1, 1, 200.00)
    result = account_dao.create_bank_account(test_bank_account)
    assert result.bad_id_number != 1


# receive


def test_get_bank_account_info_by_bank_account_id_success():
    result = account_dao.get_account_info(1)
    assert result.bad_id_number == 1


def test_get_bank_account_info_by_bank_account_id_nonexistent():
    try:
        account_dao.get_account_info(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"


def test_get_all_bank_account_info_by_customer_id_success():
    result = account_dao.get_all_accounts_by_customer_id(1)
    return result


def test_get_all_bank_account_info_by_customer_id_nonexistent():
    try:
        account_dao.get_all_accounts_by_customer_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer account matches this ID number. Try again"


# use


def test_update_account_success():
    new_bank_info = Account(1, 1, 300.00)
    result = account_dao.update_account(new_bank_info)
    assert result.balance == 300.00


def test_update_account_custom_id_failure():
    new_bank_info = Account(0, 1, 300.00)
    try:
        account_dao.update_account(new_bank_info)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"


# delete

def test_delete_bank_account_by_id_success():
    result = account_dao.delete_bank_account_by_id(1)
    assert result


def test_delete_bank_account_by_id_failure():
    try:
        account_dao.delete_bank_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"
