from modules.error.exeption import ErrorException


class ErrorMessage:
    error_messages = {
        ErrorException.WRONG_MENU_OPTION: 'L\'option choisit n\'existe pas.'
    }

    @staticmethod
    def display_error_message(exception_type):
        if exception_type in ErrorMessage.error_messages.keys():
            print(ErrorMessage.error_messages[exception_type])
