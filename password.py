from modules.login.login import Login
from modules.menu.menu_launcher import MenuLauncher
from modules.passwords.passwords_manager import PasswordsManager
from modules.error.message import ErrorMessage
from modules.error.exeption import ErrorException
import argparse


def get_password_args(args):
    password_name: str
    identifier: str
    password: str

    if 'n' in args:
        password_name = args['n']
    if 'i' in args:
        identifier = args['i']
    if 'p' in args:
        password = args['p']

    return password_name, identifier, password


def main():

    # Args processing
    parser = argparse.ArgumentParser(description='Password Manager')
    parser.add_argument('-interactive', action='store_true',
                        help='Use the interactive command line to manage passwords')
    parser.add_argument('-add', action='store_true', help='Add a new password')
    parser.add_argument('-get', action='store_true', help='Get credentials of a password')
    parser.add_argument('-update', action='store_true', help='Update a password')
    parser.add_argument('-remove', action='store_true', help='Remove a password')
    parser.add_argument('-list', action='store_true', help='List all password names')
    parser.add_argument('-n', help='Name the password for get/add/update/remove argument')
    parser.add_argument('-i', help='Identifier for update and add argument')
    parser.add_argument('-p', help='Password for update and add argument')
    args = vars(parser.parse_args())

    login = Login()

    if args['interactive']:
        return MenuLauncher()

    if args['list']:
        # List Password
        password_manager = PasswordsManager()
        return password_manager.list_passwords()

    if args['get']:
        password_name = get_password_args(args)[0]
        password_manager = PasswordsManager()
        return password_manager.view_password(password_name)

    if args['add']:
        password_name, identifier, password = get_password_args(args)
        password_manager = PasswordsManager()
        return password_manager.add_new_password(password_name, identifier, password)

    if args['update']:
        # Update Password
        password_name, identifier, password = get_password_args(args)
        print(password_name)
        password_manager = PasswordsManager()
        return password_manager.update_pasword(password_name, identifier, password)

    if args['remove']:
        # Remove Password
        password_name, identifier, password = get_password_args(args)
        password_manager = PasswordsManager()
        return password_manager.delete_password(password_name, identifier, password)

    return MenuLauncher()


if __name__ == '__main__':
    main()
