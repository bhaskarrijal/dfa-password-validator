import string


def validate_password(password):
    states = {
        0: {'lower': 1, 'upper': 2, 'digit': 3},
        1: {'lower': 1, 'upper': 2, 'digit': 3},
        2: {'lower': 1, 'upper': 2, 'digit': 3},
        3: {'lower': 3, 'upper': 3, 'digit': 3}
    }
    current_state = 0
    for c in password:
        if c in string.ascii_lowercase:
            input_symbol = 'lower'
        elif c in string.ascii_uppercase:
            input_symbol = 'upper'
        elif c in string.digits:
            input_symbol = 'digit'
        else:
            return False
        current_state = states[current_state].get(input_symbol)
        if current_state is None:
            return False
    return current_state == 3 and len(password) >= 8


print(validate_password('Abc12345'))
print(validate_password('abc12345'))
print(validate_password('ABC12345'))
print(validate_password('Abcdefg'))
print(validate_password('Abcdefgh'))
print(validate_password('Abcdefgh!'))
