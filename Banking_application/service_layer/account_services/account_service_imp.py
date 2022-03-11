from abc import ABC

from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.insufficient_funds_exception import InsufficientFunds
from custom_exceptions.wrong_money_input import BadValueInput
from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.account_class_information import Account
from service_layer.account_services.account_service_interface import BankAccountServiceInterface3


class BankAccountServiceImp(BankAccountServiceInterface3, ABC):
    bank_account_needed_for_id_catch = Account(1, 1, 500)
    bank_account_needed_for_id_catch_2 = Account(1, 2, 500)
    bank_account_needed_for_id_catch_3 = Account(2, 1, 500)
    bank_account_needed_for_id_catch_4 = Account(2, 2, 500)
    bank_account_list = [bank_account_needed_for_id_catch, bank_account_needed_for_id_catch_2,
                         bank_account_needed_for_id_catch_3, bank_account_needed_for_id_catch_4]
    id_generator = 2
    ba_dao_imp = AccountDAOImp
    cust_dao_imp = CustomerDAOImp

    def __init__(self, bank_dao):
        self.bank_dao: AccountDAOImp = bank_dao

    def add_new_bank_account(self, bank_account: Account) -> Account:  # Tie into Customer ID somehow
        return self.bank_dao.create_bank_account(bank_account)

    def get_bank_account_info(self, ba_id_number: int) -> Account:  # Tie into Customer ID somehow
        return self.bank_dao.get_account_info(ba_id_number)

    def get_all_bank_accounts_by_customer_id(self, cust_id_number: int) -> Account:
        return self.bank_dao.get_all_accounts_by_customer_id(cust_id_number)

    def update_bank_account(self, bank_account: Account) -> Account:
        return self.bank_dao.update_account(bank_account)

    def withdraw_funds(self, cust_id_number: int, ba_id_number: int, withdraw_amount: float):
        account = self.bank_dao.get_account_info(ba_id_number)
        if account.custom_id_number != cust_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        if account.bad_id_number != ba_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        elif type(withdraw_amount) != float:
            raise BadValueInput("This transaction could not be processed. Try again")
        elif withdraw_amount < 0:
            raise InsufficientFunds("This transaction could not be processed. Try again")
        else:
            account.balance = account.balance - withdraw_amount
            return self.bank_dao.update_account(account)  # CREATE AN UPDATE

    def deposit_funds(self, cust_id_number: int, ba_id_number: int, deposit_amount: float):
        account = self.bank_dao.get_account_info(ba_id_number)
        if account.custom_id_number != cust_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        if account.bad_id_number != ba_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        if type(deposit_amount) != float:
            raise BadValueInput("This transaction could not be processed. Try again")
        if deposit_amount < 0:
            raise InsufficientFunds("This transaction could not be processed. Try again")
        if account.balance + deposit_amount < 0:
            raise InsufficientFunds("This transaction could not be processed. Try again")
        else:
            account.balance = account.balance + deposit_amount
            return self.bank_dao.update_account(account)  # CREATE AN UPDATE

    def transfer_funds(self, cust_id_number: int, ba_id_number1: int, ba_id_number2: int,
                       transfer_amount: float):
        self.withdraw_funds(cust_id_number, ba_id_number1, transfer_amount)
        self.deposit_funds(cust_id_number, ba_id_number2, transfer_amount)
        return "Transfer complete"

    def delete_bank_account_by_id(self, ba_id_number: int) -> bool:  # Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.bad_id_number == ba_id_number:
                self.bank_account_list.remove(bank_account)
                return True
        raise IdNotFound("No bank account matches this ID number. Try again")

    print(bank_account_list)
