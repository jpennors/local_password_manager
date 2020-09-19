import configparser
import pyperclip
import hashlib
from modules.utils.input.input import Input
from modules.utils.input.input_type import InputType


class Login:
    secret_key: str

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Login, cls).__new__(cls)
            cls.instance.__initialized = False

        return cls.instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self._read_config()
        self._login()

    def _read_config(self):
        config = configparser.ConfigParser()
        config.read('config\\env.ini')
        self.hashed_secret_key = config['SETTINGS']['HASHED_SECRET_KEY']

    def _login(self):
        if not self.hashed_secret_key:
            return self._create_secret_key()
        secret_key = Input.get_user_input('Enter your secret key\n', InputType.APP_KEY_LOGIN)
        secret_key_try = 1

        while hashlib.sha3_384(secret_key.encode()).hexdigest() != self.hashed_secret_key:
            print('Wrong password')
            secret_key = Input.get_user_input('Enter your secret key\n', InputType.APP_KEY_LOGIN)
            secret_key_try += 1
            if secret_key_try > 5 :
                print('You missed too much, bye !')
                quit()
        self.secret_key = secret_key


    @staticmethod
    def _create_secret_key():
        print('We did not find any existing configuration, let\'s start !')
        password = Input.get_user_input(
            'First of all, write a password. This one is extremely important:\n',
            InputType.APP_KEY_CREATION)

        confirm_password = ''
        while password != confirm_password:
            confirm_password = Input.get_user_input('Please confirm it\n', InputType.APP_KEY_CREATION)

        hashed_secret_key = hashlib.sha3_384(password.encode()).hexdigest()
        print(f'Your secret key is \n{hashed_secret_key}')
        pyperclip.copy(hashed_secret_key)
        print('It has been copied to the clipboard.\nPlease paste it in config/env.ini in HASHED_SECRET_KEY=')
        quit()
