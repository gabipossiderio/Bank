from time import sleep
from typing import List, Optional

from models.account import Account
from models.client import Client
from utils.helper import str_to_date

accounts: List[Account] = []


def menu() -> None:
    print(" WELCOME TO THE BEST CLI BANK YOU'VE EVER SEEN ".center(100, '#'))
    print(" POSSIDERIO'S ATM ".center(100, '='))

    options = {
        '1': {
            'msg': 'Create account', 'action': create_account
        },
        '2': {
            'msg': 'Make a withdrawal', 'action': make_withdraw
        },
        '3': {
            'msg': 'Make a deposit', 'action': make_deposit
        },
        '4': {
            'msg': 'Make a transfer', 'action': make_transfer
        },
        '5': {
            'msg': 'Show accounts', 'action': show_accounts
        },
        '6': {
            'msg': 'Exit', 'action': exit
        },
    }

    while True:
        print('\nPlease, choose a number:')
        for i in range(1, len(options.keys()) + 1):
            print(str(i) + ' - ' + options[str(i)]['msg'])
        choice: str = input('\n>>>>>> ')
        try:
            options[str(choice)]['action']()
        except KeyError:
            print('\nYou entered an invalid option. Try again.')
        sleep(2)


def create_account() -> None:
    print('\nInform client data:')

    name: str = input('Name: ')
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    birth_date: str = input('Birth Date (DD/MM/YYYY): ')

    try:
        str_to_date(birth_date)
    except ValueError:
        print('\nPlease, enter a valid date (DD/MM/YYYY).\n')
        sleep(2)
        menu()

    client: Client = Client(name, email, cpf, birth_date)

    account: Account = Account(client)

    accounts.append(account)

    print('\nYour account has been created successfully.\n')
    print('ACCOUNT DATA'.center(100, '='))
    print(account)
    sleep(2)


def make_withdraw() -> None:
    if len(accounts) == 0:
        print('There are no registered accounts.')
        sleep(2)
        menu()
    account_number: int = int(input('Please, enter the account number to which the money will be withdrawn: '))

    account: Account = get_account_by_number(account_number)

    if account:
        value: float = float(input('\nEnter the withdrawal amount: '))
        account.withdraw(value)
    else:
        print(f'\nThe account with the number {account_number} was not found.')


def make_deposit() -> None:
    if len(accounts) == 0:
        print('\nThere are no registered accounts.')
        sleep(2)
        menu()
    account_number: int = int(input('\nPlease, enter the account number to which the money will be deposited: '))

    account: Account = get_account_by_number(account_number)

    if account:
        value: float = float(input('Enter the deposit amount: '))
        account.deposit(value)
    else:
        print(f'\nThe account with the number {account_number} was not found.')


def make_transfer() -> None:
    if len(accounts) == 0:
        print('\nThere are no registered accounts.')
        sleep(2)
        menu()

    sender_account_number: int = int(input('\nPlease, enter the account number to which the money will be withdrawn: '))

    sender_account: Account = get_account_by_number(sender_account_number)

    if sender_account:
        receiver_account_number: int = int(
            input('\nPlease, enter the account number to which the money will be deposited: ')
        )
        receiver_account: Account = get_account_by_number(receiver_account_number)
        if receiver_account:
            value: float = float(input('\nEnter the transfer amount: '))
            sender_account.transfer(receiver_account, value)
        else:
            print(f'\nThe account with the number {receiver_account_number} was not found.')
    else:
        print(f'\nThe account with the number {sender_account_number} was not found.')


def show_accounts() -> None:
    if len(accounts) == 0:
        print('There are no registered accounts.')
        sleep(2)
        menu()
    print('ACCOUNTS LIST'.center(100, '='))
    for account in accounts:
        print(account)
        print('-------------------------------------')
        sleep(1)


def get_account_by_number(number: int) -> Account:
    c: Optional[Account] = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number:
                c = account
    return c


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
