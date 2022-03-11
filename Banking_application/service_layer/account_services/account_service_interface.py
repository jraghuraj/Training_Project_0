from abc import ABC, abstractmethod

from entities.account_class_information import Account


class BankAccountServiceInterface3(ABC):

    @abstractmethod
    def add_new_bank_account(self, bank_account: Account) -> Account:
        pass

    @abstractmethod
    def get_bank_account_info(self, ba_id_number: int) -> Account:
        pass

    @abstractmethod
    def get_all_bank_accounts_by_customer_id(self, cust_id_number: int) -> Account:
        pass

    @abstractmethod
    def update_bank_account(self, ba_id_number: int) -> Account:
        pass

    @abstractmethod
    def withdraw_funds(self, cust_id_number: int, ba_id_number: int, withdraw_amount: float) -> Account:
        pass

    @abstractmethod
    def deposit_funds(self, cust_id_number: int, ba_id_number: int, deposit_amount: float) -> float:
        pass

    @abstractmethod
    def transfer_funds(self, cust_id_number: int, ba_id_number1: int, ba_id_number2: int, transfer_amount: float):
        pass

    @abstractmethod
    def delete_bank_account_by_id(self, ba_id_number: int) -> bool:
        pass
    