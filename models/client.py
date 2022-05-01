from datetime import date

from utils.helper import date_to_str, str_to_date


class Client:
    counter: int = 1

    def __init__(self: object, name: str, email: str, cpf: str, birth_date: str) -> None:
        self._code: int = Client.counter
        self._name: str = name
        self._email: str = email
        self._cpf: str = cpf
        self._birth_date: date = str_to_date(birth_date)
        self._registration_date: date = date.today()
        Client.counter += 1

    @property
    def code(self: object) -> int:
        return self._code

    @property
    def name(self: object) -> str:
        return self._name

    @property
    def email(self: object) -> str:
        return self._email

    @property
    def cpf(self: object) -> str:
        return self._cpf

    @property
    def birth_date(self: object) -> str:
        return date_to_str(self._birth_date)

    @property
    def registration_date(self: object) -> str:
        return date_to_str(self._registration_date)

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nName: {self.name} \nBirth Date: {self.birth_date} ' \
               f'\nRegistration Date: {self.registration_date}'
