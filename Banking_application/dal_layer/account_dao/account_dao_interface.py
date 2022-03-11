from abc import abstractmethod, ABC

from entities.account_class_information import Account


class BankAccountDAOInterface(ABC):

    @abstractmethod
    def create_bank_account(self, bank_account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_info(self, ba_id_number: int) -> Account:
        pass

    @abstractmethod
    def get_all_accounts_by_customer_id(self, cust_id_number: int) -> Account:
        pass

    @abstractmethod
    def update_account(self, ba_id_number: int) -> Account:
        pass
