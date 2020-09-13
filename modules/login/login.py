from getpass import getpass


class Login:

    secret_key: str

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Login, cls).__new__(cls)

        return cls.instance

    def set_secret_key(self):
        self.secret_key = input("Enter your password : \n")