from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.insufficient_funds_exception import InsufficientFunds
from custom_exceptions.wrong_money_input import BadValueInput
from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from entities.account_class_information import Account
from service_layer.account_services.account_service_imp import BankAccountServiceImp

bank_account_dao = AccountDAOImp()
bank_account_service = BankAccountServiceImp(bank_account_dao)
test_bank_account_person = Account(1, 1, 100.00)


def test_add_new_bank_account():
    test_bank_account = Account(1, 0, 100)
    result = bank_account_dao.create_bank_account(test_bank_account)
    assert result.bad_id_number != 0


def test_get_bank_account_info_by_bank_account_id_success():
    result = bank_account_dao.get_account_info(1)
    assert result.bad_id_number == 1


def test_get_bank_account_info_by_bank_account_id_nonexistent():
    try:
        bank_account_dao.get_account_info(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"


def test_get_all_bank_account_info_by_cust_id_success():
    result = bank_account_dao.get_all_accounts_by_customer_id(1)
    assert result.custom_id_number == 1


def test_get_all_bank_account_info_by_cust_id_nonexistent():
    try:
        bank_account_dao.get_all_accounts_by_customer_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer account matches this ID number. Try again"


def test_deposit_funds_by_bank_account_id_success():
    result = bank_account_service.deposit_funds(1, 1, 50.00)
    assert result


def test_deposit_funds_by_bank_account_id_failure():
    try:
        bank_account_service.deposit_funds(1, 3, 50.00)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"


def test_deposit_funds_with_negative_amount():
    try:
        bank_account_service.deposit_funds(1, 1, -50.00)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_withdraw_funds_with_string():
    try:
        bank_account_service.deposit_funds(1, 1, "string")
        assert False
    except BadValueInput as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_withdraw_funds_by_bank_account_id_success():
    result = bank_account_service.withdraw_funds(1, 1, 50.00)
    assert result


def test_withdraw_funds_by_bank_account_id_failure():
    try:
        bank_account_service.withdraw_funds(1, 3, 50.00)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"


def test_withdraw_funds_with_negative_amount():
    try:
        bank_account_service.withdraw_funds(1, 1, -50.00)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_deposit_funds_with_string():
    try:
        bank_account_service.deposit_funds(1, 1, "string")
        assert False
    except BadValueInput as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_transfer_funds_success():
    result = bank_account_service.transfer_funds(1, 1, 2, 50.00)
    return result


def test_transfer_funds_with_bad_cust_id():
    try:
        bank_account_service.transfer_funds(0, 1, 2, 50.0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"


def test_transfer_funds_with_negative():
    try:
        bank_account_service.transfer_funds(1, 1, 2, -50.0)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_transfer_funds_with_string():
    try:
        bank_account_service.transfer_funds(1, 1, 90, "STRING")
        assert False
    except BadValueInput as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_delete_bank_account_by_id_success():
    result = bank_account_dao.delete_bank_account_by_id(1)
    assert result


def test_delete_bank_account_by_id_failure():
    try:
        bank_account_dao.delete_bank_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"
