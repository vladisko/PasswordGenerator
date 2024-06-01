from random import shuffle
from symbols import *


def generate_password(password_len=10) -> str | None:
    if password_len <= (len(special_symbols) + len(numbers) + len(uppercase_chars) + len(lowercase_chars)):
        password = ""

        mix = special_symbols + numbers + uppercase_chars + lowercase_chars
        shuffle(mix)

        for i in mix[0:password_len]:
            password += i

        return password
    print("Недопустимая длина пароля")
