from modules.login.login import Login
from modules.menu.menu_launcher import MenuLauncher


if __name__ == '__main__':

    login = Login()
    login.set_secret_key()

    menu = MenuLauncher()
    menu.launch_menu()

