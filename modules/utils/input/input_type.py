from enum import Enum


class InputType(Enum):
    PASSWORD = 1,
    IDENTIFIER = 2,
    APP_KEY_CREATION = 3,
    APP_KEY_LOGIN = 4,
    MENU_OPTION = 5,
    PASSWORD_NAME = 6,
    CONFIRM = 7,
    PASSWORD_OPTION = 8