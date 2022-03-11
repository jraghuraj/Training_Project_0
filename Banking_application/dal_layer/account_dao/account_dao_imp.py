from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_interface import BankAccountDAOInterface
from entities.account_class_information import Account


class AccountDAOImp(BankAccountDAOInterface):
    account_needed_for_id_catch = Account(1, 1, 500.00)
    account_needed_for_id_catch_2 = Account(1, 2, 400.00)
    account_needed_for_id_catch_3 = Account(2, 1, 400.00)
    account_needed_for_id_catch_4 = Account(2, 2, 400.00)
    bank_account_list = [account_needed_for_id_catch, account_needed_for_id_catch_2,
                         account_needed_for_id_catch_3, account_needed_for_id_catch_4]

    def __init__(self):
        self.id_generator = 2

    def create_bank_account(self, bank_account: Account) -> Account:
        bank_account.bad_id_number = self.id_generator
        self.id_generator += 1
        self.bank_account_list.append(bank_account)
        return bank_account

    def get_account_info(self, bank_id_number: int) -> Account:
        for bank_account in self.bank_account_list:
            if bank_account.bad_id_number == bank_id_number:
                return bank_account
        raise IdNotFound("No bank account matches this ID number. Try again")

    def get_all_accounts_by_customer_id(self, customer_id_number):
        for bank_account in self.bank_account_list:
            if bank_account.custom_id_number == customer_id_number:
                return AccountDAOImp.bank_account_list[customer_id_number]
            else:
                raise IdNotFound("No customer account matches this ID number. Try again")

    def update_account(self, bank_account: Account) -> Account:
        for old_info in self.bank_account_list:
            if bank_account.custom_id_number != old_info.custom_id_number:
                raise IdNotFound("No Customer matches the id given: please try again")
            else:
                old_info = bank_account
                return old_info

    def delete_bank_account_by_id(self, ba_id_number: int) -> bool:  # Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.bad_id_number == ba_id_number:
                self.bank_account_list.remove(bank_account)
                return True
        raise IdNotFound("No bank account matches this ID number. Try again")

    print(bank_account_list[0])
