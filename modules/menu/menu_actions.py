from modules.passwords.passwords_manager import PasswordsManager


class MenuAction:

    @staticmethod
    def list_passwords():
        password_manager = PasswordsManager()
        password_manager.list_passwords()

    @staticmethod
    def add_new_password():
        password_manager = PasswordsManager()
        password_manager.add_new_password()

    @staticmethod
    def view_password():
        password_manager = PasswordsManager()
        password_manager.view_password()

    @staticmethod
    def update_pasword():
        password_manager = PasswordsManager()
        password_manager.update_pasword()

    @staticmethod
    def delete_password():
        password_manager = PasswordsManager()
        password_manager.delete_password()

    @staticmethod
    def quit():
        quit()

