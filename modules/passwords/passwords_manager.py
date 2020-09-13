from modules.passwords.password_object import PasswordObject
from modules.passwords.passwords_storage import PasswordsStorage
from modules.login.login import Login
import pyperclip


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
        password_id = input('Which password do you want to consult ?\n')
        # TODo Check for password_id value
        password_object = self.password_storage.get_password(password_names[int(password_id)])
        self.display_password_info(password_object)

    def update_pasword(self):
        password_names = self.password_storage.get_passwords_list()
        self.display_password_list(password_names)
        password_id = input('Which password do you want to update ?\n')
        # TODo Check for password_id value
        old_name = password_names[int(password_id)]
        new_name_needed = input(f'Do you want to edit the name of '
                                f'the password {old_name}? (y/N)\n')
        if new_name_needed == 'y':
            name = input('What is the new name of your password?\n')
        else:
            name = old_name
            # ToDO Check if it exists
        password = input(f'What is the new password of {name}?\n')

        new_password_object = PasswordObject(secret_key=self.secret_key)
        new_password_object.encrypt(name=name, password=password)
        self.password_storage.update_password(old_name=old_name, name=name, password_object=new_password_object)
        print('Password updated')

    def delete_password(self):
        password_names = self.password_storage.get_passwords_list()
        self.display_password_list(password_names)
        password_id = input('Which password do you want to delete ?\n')
        self.password_storage.remove_password(password_names[int(password_id)])

    def display_password_list(self, password_names):
        print('--- PASSWORD LIST ---\n')
        for index, password_name in enumerate(password_names):
            print(f'{index} - {password_name}')

    def display_password_info(self, password_object: PasswordObject):
        print(f'Password {password_object.name} : {password_object.password}\n')
        pyperclip.copy(password_object.password)
        print('Your password has been copied to clipboard !')

