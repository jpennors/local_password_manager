import os
from modules.passwords.password_object import PasswordObject


class PasswordsStorage:
    file_name = 'files.txt'

    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.passwords_object = dict()
        # ToDO Add FileModeOpening Enum
        if self.file_name not in os.listdir():
            print('Initializing ...')
            self._get_or_create_password_storage('w')
        else:
            self._get_or_create_password_storage('r')
            self.load_passwords()

    def __del__(self):
        if self.file:
            self.file.close()

    def _get_or_create_password_storage(self, mode):
        self.file = open(self.file_name, mode)

    def load_passwords(self):
        print("reading ...")
        for line in self.file.read().split('\n'):
            if not line:
                return
            encrypted_name, encrypted_password = line.split(':')
            password_object = PasswordObject(secret_key=self.secret_key)
            password_object.decrypt(encrypted_name=encrypted_name, encrypted_password=encrypted_password)
            self.passwords_object[password_object.name] = password_object

    def get_passwords_list(self):
        return list(self.passwords_object.keys())

    def add_password(self, password_object: PasswordObject):
        if password_object.name in self.passwords_object:
            # ToDO Add Error message
            return
        self.passwords_object[password_object.name] = password_object
        self._save_new_file()

    def get_password(self, name):
        if name not in self.passwords_object.keys():
            return
            # ToDO Error message when key not found
        return self.passwords_object[name]

    def remove_password(self, name):
        if name in self.passwords_object.keys():
            del self.passwords_object[name]
        # ToDO Error message when key not found
        self._save_new_file()

    def update_password(self, old_name, name, password_object: PasswordObject):
        if old_name in self.passwords_object.keys():
            if old_name != name:
                del self.passwords_object[old_name]
            self.passwords_object[name] = password_object
        # ToDO Error message when key not found
        self._save_new_file()

    def _save_new_file(self):
        self._get_or_create_password_storage('w')
        for password_object in self.passwords_object.values():
            self.file.write(self._get_password_format_for_file(password_object))
        self.file.close()

    def _get_password_format_for_file(self, password_object: PasswordObject) -> str:
        return f'{password_object.encrypted_name}:{password_object.encrypted_password}\n'
