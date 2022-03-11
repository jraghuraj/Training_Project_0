from custom_exceptions.id_not_found import IdNotFound


class Customer:
    def __init__(self, first_name: str, last_name: str, custom_id_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.custom_id_number = custom_id_number

    def convert_to_dictionary(self):
        return {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "customIDnumber": self.custom_id_number
        }

    class BankAccount:

        def __init__(self, custom_id_number: int, bad_id_number: int, money_amount: float):
            self.bad_id_number = bad_id_number
            self.custom_id_number = custom_id_number
            self.money_amount = money_amount

    class BankAccountID:

        def __init__(self, id_number):
            self.id_number = id_number
            self.balance = 0

        def deposit_funds(self, id_number):
            if self.id_number == id_number:
                amount = float
                self.balance += amount
                return self.balance
            else:
                raise IdNotFound("No bank account matches this ID number. Try again")

        def withdraw_funds(self, id_number):
            if self.id_number == id_number:
                amount = float
                self.balance += amount
                return self.balance
            else:
                raise IdNotFound("No bank account matches this ID number. Try again")
