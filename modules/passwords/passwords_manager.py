from modules.passwords.password_object import PasswordObject
from modules.passwords.passwords_storage import PasswordsStorage
from modules.login.login import Login
import pyperclip
from modules.utils.input.input import Input
from modules.utils.input.input_type import InputType


class PasswordsManager:

    def __init__(self):
        login = Login()
        self.secret_key = login.secret_key
        self.password_storage = PasswordsStorage(self.secret_key)

    def list_passwords(self):
        print('--- PASSWORD LIST ---\n')
        password_names = self.password_storage.get_passwords_list()
        self.display_password_list(password_names)

    def add_new_password(self, password_name=None, identifier=None, password=None):
        print('--- PASSWORD CREATION ---\n')
        if not password_name:
            password_name = Input.get_user_input('What is the name of your password?\n', InputType.PASSWORD_NAME)
        # ToDO Check if it exists
        if not identifier:
            identifier = Input.get_user_input(f'What is the identifier of {password_name}?\n', InputType.IDENTIFIER)
        if not password:
            password = Input.get_user_input(f'What is the password of {password_name}?\n', InputType.PASSWORD)

        new_password_object = PasswordObject(secret_key=self.secret_key)
        new_password_object.encrypt(name=password_name, identifier=identifier, password=password)

        self.password_storage.add_password(new_password_object)
        print('Password added')

    def view_password(self, password_name=None):
        print('--- PASSWORD INFO ---\n')
        if not password_name:
            password_name = self._get_specific_password(action='consult')
        password_object = self.password_storage.get_password(password_name)
        self.display_password_info(password_object)

    def update_pasword(self, old_password_name=None, identifier=None, password=None):
        print('--- PASSWORD UPDATE ---\n')
        if not old_password_name:
            old_password_name = self._get_specific_password(action='update')
        new_name_needed = Input.get_user_input(f'Do you want to edit the name of '
                                f'the password {old_password_name}? (y/N)\n', InputType.CONFIRM)
        if new_name_needed == 'y':
            password_name = Input.get_user_input('What is the new name of your password?\n', InputType.PASSWORD_NAME)
        else:
            password_name = old_password_name
            # ToDO Check if it exists

        if not identifier:
            identifier = Input.get_user_input(f'What is the new identifier of {password_name}?\n', InputType.IDENTIFIER)
        if not password:
            password = Input.get_user_input(f'What is the new password of {password_name}?\n', InputType.PASSWORD)

        new_password_object = PasswordObject(secret_key=self.secret_key)
        new_password_object.encrypt(name=password_name, identifier=identifier, password=password)
        self.password_storage.update_password(old_name=old_password_name, name=password_name, password_object=new_password_object)
        print('Password updated')

    def delete_password(self, password_name=None):
        print('--- PASSWORD DELETION ---\n')
        if not password_name:
            password_name = self._get_specific_password(action='delete')
        self.password_storage.remove_password(password_name)
        print('Password removed')

    def _get_specific_password(self, action: str):
        password_names = self.password_storage.get_passwords_list()
        self.display_password_list(password_names)
        password_id = Input.get_user_input(f'Which password do you want to {action} ?\n',
                                           InputType.PASSWORD_OPTION,
                                           [str(index) for index in range(len(password_names))])
        return password_names[int(password_id)]

    @staticmethod
    def display_password_list(password_names):
        for index, password_name in enumerate(password_names):
            print(f'{index} - {password_name}')

    @staticmethod
    def display_password_info(password_object: PasswordObject):
        print(f'Password {password_object.name}\n'
              f'Identifier: {password_object.identifier}\n'
              f'Password: {password_object.password}\n')
        pyperclip.copy(password_object.password)
        print('Your password has been copied to clipboard !')

