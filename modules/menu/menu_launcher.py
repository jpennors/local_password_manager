from modules.utils.screen_manager import ScreenManager
from modules.menu.menu_option import MenuOption
from modules.menu.menu_actions import MenuAction
from modules.utils.input.input import Input
from modules.utils.input.input_type import InputType


class MenuLauncher:

    menu_options = {
        "0": MenuOption("Display a password", MenuAction.view_password),
        "1": MenuOption("List passwords", MenuAction.list_passwords),
        "2": MenuOption("Update a password", MenuAction.update_pasword),
        "3": MenuOption("Add a new password", MenuAction.add_new_password),
        "4": MenuOption("Delete a password", MenuAction.delete_password),
        "5": MenuOption("Quit", MenuAction.quit)
    }

    def __init__(self):
        self.launch_menu()

    def launch_menu(self):
        while True:
            ScreenManager.clear_screen()
            self.display_option()
            ScreenManager.keyboard_action_before_clearing()

    def display_option(self):
        print('--- MAIN MENU ---')
        for (menu_option_id, menu_option) in self.menu_options.items():
            print(f'{menu_option_id} - {menu_option.description}')
        self.select_option()

    def select_option(self):
        menu_option_id = Input.get_user_input('Select an option ?\n', InputType.MENU_OPTION,
                                              list(self.menu_options.keys()))
        ScreenManager.clear_screen()
        self.display_selection(menu_option_id)
        self.menu_options[menu_option_id].action()

    def display_selection(self, menu_option_id):
        print(f'You select option "{self.menu_options[menu_option_id].description}"\n')
