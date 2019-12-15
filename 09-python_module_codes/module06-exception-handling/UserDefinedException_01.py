class InvalidTransactionException(Exception):
    def __init__(self,message):
        self._message = message

    def print_message(self):
        print(self._message)


class BankTransaction:

    def __init__(self):
        self.balance = 2000

    def amount_to_with_draw(self, withdraw_amount):
        remaining_balance = self.balance - int(withdraw_amount)
        if remaining_balance <= 1000:
            raise InvalidTransactionException("Not allowed to withdraw ")
        else:
            return remaining_balance


if __name__ == '__main__':

    try:
        obj1 = BankTransaction()
        amount = int(input("Enter amount to deposit"))
        print(obj1.amount_to_with_draw(amount))
    except InvalidTransactionException as ex:
        ex.print_message()