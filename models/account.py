from models.client import Client
from utils.helper import float_to_str_currency


class Account:

    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self._number: int = Account.code
        self._client: Client = client
        self._partial_balance: float = 0.0
        self._overdraft: float = 100.0
        self._total_balance: float = self._total_balance_calculator
        Account.code += 1

    def __str__(self: object) -> str:
        return f'\nAccount Number: {self._number} \nClient: {self._client.name} ' \
               f'\nTotal Balance: {float_to_str_currency(self._total_balance)}'

    @property
    def number(self: object) -> int:
        return self._number

    @property
    def client(self: object) -> Client:
        return self._client

    @property
    def partial_balance(self: object) -> float:
        return self._partial_balance

    @partial_balance.setter
    def partial_balance(self: object, value: float) -> None:
        self._partial_balance = value

    @property
    def overdraft(self: object) -> float:
        return self._overdraft

    @overdraft.setter
    def overdraft(self: object, value: float) -> None:
        self._overdraft = value

    @property
    def total_balance(self: object) -> float:
        return self._total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self._total_balance = value

    @property
    def _total_balance_calculator(self: object) -> float:
        return self._partial_balance + self._overdraft

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.partial_balance = self.partial_balance + value
            self.total_balance = self._total_balance_calculator
            print('Deposit made successfully.')
        else:
            print('Error when depositing. Try again.')

    def withdraw(self: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.partial_balance >= value:
                self.partial_balance = self.partial_balance - value
                self.total_balance = self._total_balance_calculator
            else:
                remaining_balance: float = self.partial_balance - value
                self.overdraft = self.overdraft + remaining_balance
                self.partial_balance = 0
                self.total_balance = self._total_balance_calculator
            print('Withdraw made successfully.')
        else:
            print('Error when withdrawing. Try again.')

    def transfer(self: object, destination_account: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.partial_balance >= value:
                self.partial_balance = self.partial_balance - value
                self.total_balance = self._total_balance_calculator
                destination_account.partial_balance += value
                destination_account.total_balance = destination_account._total_balance_calculator
            else:
                remaining_balance: float = self.partial_balance - value
                self.overdraft = self.overdraft + remaining_balance
                self.partial_balance = 0
                self.total_balance = self._total_balance_calculator
                destination_account.partial_balance += value
                destination_account.total_balance = destination_account._total_balance_calculator
            print('Transfer made successfully.')
        else:
            print('Transfer error. Try again.')
