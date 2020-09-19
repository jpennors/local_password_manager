class InputValidation:
    DEFAULT_LENGTH_MIN = 0
    DEFAULT_LENGTH_MAX = 100
    only_digit = False

    def __init__(self, length_min=DEFAULT_LENGTH_MIN, length_max=DEFAULT_LENGTH_MAX,
                 only_digit=False):
        self.length_min = length_min
        self.length_max = length_max
        self.only_digit = only_digit

    def process_validation(self, user_input, specific_characters=[]) -> bool:

        if self.length_min is not None and len(user_input) < self.length_min:
            print(f'Minimum length is {self.length_min}.')
            return False

        if self.length_max is not None and len(user_input) > self.length_max:
            print(f'Maximum length is {self.length_max}.')
            return False

        if self.only_digit and not str.isdigit():
            print('Input must be digits.')
            return False

        if len(specific_characters) > 0:
            if len(user_input) == 0 :
                return False
            for char in user_input:
                if char not in specific_characters:
                    possibilities = ', '.join(specific_characters)
                    print(f'Possibilities are {possibilities}')
                    return False

        return True
