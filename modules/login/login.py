import configparser
import pyperclip
import hashlib

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
        secret_key = input('Enter your secret key\n')
        secret_key_try = 1

        while hashlib.sha3_384(secret_key.encode()).hexdigest() != self.hashed_secret_key:
            print('Wrong password')
            secret_key = input('Enter your secret key\n')
            secret_key_try += 1
            if secret_key_try > 5 :
                print('You missed too much, bye !')
                quit()
        self.secret_key = secret_key


    @staticmethod
    def _create_secret_key():
        print('We did not find any existing configuration, let\'s start !')
        password = input('First of all, write a password. This one is extremely important:\n')

        confirm_password = ''
        while password != confirm_password:
            confirm_password = input('Please confirm it\n')

        hashed_secret_key = hashlib.sha3_384(password.encode()).hexdigest()
        print(f'Your secret key is \n{hashed_secret_key}')
        pyperclip.copy(hashed_secret_key)
        print('It has been copied to the clipboard.\nPlease paste it in config/env.ini in HASHED_SECRET_KEY=')
        quit()
