from modules.error.exeption import ErrorException


class ErrorMessage:
    error_messages = {
        ErrorException.NO_ARGS: 'There is no argument. Please use -h to consult options.'
    }

    @staticmethod
    def display_error_message(exception_type):
        if exception_type in ErrorMessage.error_messages.keys():
            print(ErrorMessage.error_messages[exception_type])
