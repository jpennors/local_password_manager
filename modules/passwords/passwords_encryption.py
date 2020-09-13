import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class PasswordsEncryption:
    iterations = 100000
    backend = default_backend()

    @staticmethod
    def _derive_key(password: bytes, salt: bytes) -> bytes:
        """Derive a secret key from a given password and salt"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=PasswordsEncryption.iterations,
            backend=PasswordsEncryption.backend)
        return b64e(kdf.derive(password))

    @staticmethod
    def encrypt_value(secret: str, value: str):
        salt = secrets.token_bytes(16)
        key = PasswordsEncryption._derive_key(secret.encode(), salt)
        encrypted_value = (b64e(b'%b%b%b' % (salt, PasswordsEncryption.iterations.to_bytes(4, 'big'),
                                b64d(Fernet(key).encrypt(value.encode())))))
        return encrypted_value.decode()

    @staticmethod
    def decrypt_value(secret: str, encrypted_value: str) -> str:
        decoded = b64d(encrypted_value)
        salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
        iterations = int.from_bytes(iter, 'big')
        key = PasswordsEncryption._derive_key(secret.encode(), salt)
        initial_data = Fernet(key).decrypt(token)
        return initial_data.decode()
