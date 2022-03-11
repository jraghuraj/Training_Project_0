class Account:

    def __init__(self, custom_id_number: int, bad_id_number: int, balance: float):
        self.balance = balance
        self.custom_id_number = custom_id_number
        self.bad_id_number = bad_id_number

    def convert_to_dictionary(self):
        return {
            "customIdNumber": self.custom_id_number,
            "badIdNumber": self.bad_id_number,
            "balance": self.balance
            }

