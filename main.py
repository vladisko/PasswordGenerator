from alphabet import alphabet
from random import shuffle

special_symbols = [
                    '!', ''', '#', '$', '%', '&', ''', '(', ')',
                    '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                    '>', '?', '@', '[', ']', '^', '_', '`', '{', '|',
                    '}', '~', '\\'
                    ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

uppercase_chars = alphabet("en", True)
lowercase_chars = alphabet("en", False)

def generate_password(password_len:int) -> str: 
    if password_len <= (len(special_symbols) + len(numbers) + len(uppercase_chars) + len(lowercase_chars)):
        password = ""

        mix = special_symbols + numbers + uppercase_chars + lowercase_chars
        shuffle(mix)

        for i in mix[0:password_len]:
            password += i
            
        return password
    return print("Недопустимая длина пароля")