from simple_term_menu import TerminalMenu


def main():
    options = ['1', '2', '3']
    termminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


if __name__ == '__main__':
    main()
