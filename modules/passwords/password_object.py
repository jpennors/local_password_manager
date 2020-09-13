from modules.passwords.passwords_encryption import PasswordsEncryption


class PasswordObject:

    secret_key: str
    name: str
    password: str
    encrypted_name: str
    encrypted_password: str

    def __init__(self, secret_key: str):
        # ToDO Add name & password + credentials mode like Encrypted / Default
        self.secret_key = secret_key

    def encrypt(self, name, password):
        self.name = name
        self.password = password

        self.encrypted_name = PasswordsEncryption.encrypt_value(self.secret_key, name)
        self.encrypted_password = PasswordsEncryption.encrypt_value(self.secret_key, password)

    def decrypt(self, encrypted_name: str, encrypted_password: str):
        self.encrypted_name = encrypted_name
        self.encrypted_password = encrypted_password

        self.name = PasswordsEncryption.decrypt_value(self.secret_key, encrypted_name)
        self.password = PasswordsEncryption.decrypt_value(self.secret_key, encrypted_password)