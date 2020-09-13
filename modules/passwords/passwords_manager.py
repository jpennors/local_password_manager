from modules.passwords.password_object import PasswordObject
from modules.passwords.passwords_storage import PasswordsStorage
from modules.login.login import Login


class PasswordsManager:

    def __init__(self):
        login = Login()
        print(login)
        self.secret_key = login.secret_key
        self.password_storage = PasswordsStorage(self.secret_key)

    def list_passwords(self):
        password_names = self.password_storage.get_passwords_list()
        self.display_password_list(password_names)

    def add_new_password(self):
        name = input('What is the name of your password?\n')
        # ToDO Check if it exists
        password = input(f'What is the password of {name}?\n')

        new_password_object = PasswordObject(secret_key=self.secret_key)
        new_password_object.encrypt(name=name, password=password)

        self.password_storage.add_password(new_password_object)

    def view_password(self):
        password_names = self.password_storage.get_passwords_list()
        self.display_password_list(password_names)
        password_id = input('Which password do you want to consult ?')
        # TODo Check for password_id value
        password_object = self.password_storage.get_password(password_names[int(password_id)])
        self.display_password_info(password_object)


    def display_password_list(self, password_names):
        print('--- PASSWORD LIST ---')
        for index, password_name in enumerate(password_names):
            print(f'{index} - {password_name}')

    def display_password_info(self, password_object: PasswordObject):
        print(f'Password {password_object.name} : {password_object.password}')

