from modules.utils.input.input_type import InputType
from modules.utils.input.input_validation import InputValidation


class Input:
    validation_rules = {
        InputType.PASSWORD: InputValidation(length_min=1),
        InputType.IDENTIFIER: InputValidation(),
        InputType.APP_KEY_CREATION: InputValidation(length_min=4),
        InputType.APP_KEY_LOGIN: InputValidation(),
        InputType.MENU_OPTION: InputValidation(),
        InputType.PASSWORD_NAME: InputValidation(length_min=2),
        InputType.CONFIRM: InputValidation(),
        InputType.PASSWORD_OPTION: InputValidation(length_min=1)
    }

    @classmethod
    def get_user_input(cls, description: str, input_type: InputType, specific_characters=[]):
        user_input = Input._user_input(description)
        if input_type in cls.validation_rules:
            while not cls.validation_rules[input_type].process_validation(user_input, specific_characters):
                print('There was an issue with your input ...')
                user_input = Input._user_input(description)

        return user_input

    @staticmethod
    def _user_input(description: str):
        return input(description)