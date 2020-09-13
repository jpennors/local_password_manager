from modules.error.message import ErrorMessage
from modules.error.exeption import ErrorException
from modules.utils.screen_manager import ScreenManager
from modules.menu.menu_option import MenuOption
from modules.menu.menu_actions import MenuAction


class MenuLauncher:
    menu_options = {
        "0": MenuOption("Look for a password", MenuAction.view_password),
        "1": MenuOption("List passwords", MenuAction.list_passwords),
        "2": MenuOption("Update a password", MenuAction.update_pasword),
        "3": MenuOption("Add a new password", MenuAction.add_new_password),
        "4": MenuOption("Delete a password", MenuAction.delete_password),
        "5": MenuOption("Start over", None)
    }

    def launch_menu(self):
        ScreenManager.clear_screen()
        self.display_option()

    def display_option(self):
        for (menu_option_id, menu_option) in self.menu_options.items():
            print(f'{menu_option_id} - {menu_option.description}')
        self.select_option()

    def select_option(self):
        menu_option_id = input('Which option ?\n')
        if menu_option_id not in self.menu_options.keys():
            ErrorMessage.display_error_message(ErrorException.WRONG_MENU_OPTION)
            self.launch_menu()
        else:
            self.display_selection(menu_option_id)
            self.menu_options[menu_option_id].action()

    def display_selection(self, menu_option_id):
        print(f'Tu as sélectionné "{self.menu_options[menu_option_id].description}"')
