def alphabet(language: str, upper=False) -> list:
    match language:
        case 'en':
            letters = [chr(i) for i in range(97, 123)]

        case 'ru':
            letters = [chr(i) for i in range(1072, 1104)]

    if upper:
        letters = [letter.upper() for letter in letters]

    return letters


special_symbols = [
    '!', '#', '$', '%', '&', '(', ')',
    '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
    '>', '?', '@', '[', ']', '^', '_', '`', '{', '|',
    '}', '~', '\\', "'", '"'
]

numbers = []
for num in range(0, 10):
    numbers.append(str(num))

uppercase_chars = alphabet("en", True)
lowercase_chars = alphabet("en")
