from os import system, name


class ScreenManager:

    @staticmethod
    def clear_screen():
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
