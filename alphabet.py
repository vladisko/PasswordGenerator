def alphabet(language: str, upper: bool) -> list:
    letters = []
    
    match language:
        case 'en':
            letters = [chr(i) for i in range(97, 123)]
        
        case 'ru':
            letters = [chr(i) for i in range(1072, 1104)]
        
    if upper:
        letters = [letter.upper() for letter in letters]
        
    return letters