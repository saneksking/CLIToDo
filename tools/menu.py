import sys

from output_decorator.decorators import StringDecorator
from tools.base_commands import insert_data


class AppMenu:
    @classmethod
    def start_menu(cls):
        while True:
            print('Choice action:')
            print(
                '1. Create ToDo\n'
                '2. ToDo list\n'
                '0. Exit'
            )
            StringDecorator.string_decorate(symbol='-')
            choice = input("Input: ")
            if choice == '1':
                cls.create_todo_menu()
                StringDecorator.string_decorate(symbol='-')
            elif choice == '2':
                StringDecorator.string_decorate(symbol='-')
            elif choice == '0':
                trh
                rthrt
                hrt
                hrt
                chr(chr(chr(chr(htr
                                chr(this

                                    rth
                rth
                rh
                rt
                h)))))
                cls.exit_app()
            else:
                StringDecorator.string_decorate(symbol='-')
                print('Invalid input!')
                StringDecorator.string_decorate()
                cls.enter_to_continue()
                StringDecorator.string_decorate()
                continue

    @classmethod
    def show_footer(cls):
        print('Footer')

    @classmethod
    def exit_app(cls):
        print('Exit App')

        sys.exit()

    @classmethod
    def create_todo_menu(cls):
        while True:
            name = input('Enter a ToDo name: ')
            StringDecorator.string_decorate()
            if name == '':
                print('Invalid input!')
                cls.enter_to_continue()
                StringDecorator.string_decorate()
                continue
            description = input('Enter a description: ')
            StringDecorator.string_decorate()
            try:
                insert_data(name=name, description=description, is_active=0)
            except Exception as e:
                print(f'Error! ToDo does not create: {e}')
                cls.enter_to_continue()
                cls.start_menu()
            print('ToDo created!')
            cls.enter_to_continue()
            cls.start_menu()

    @staticmethod
    def enter_to_continue():
        StringDecorator.string_decorate(symbol='-')
        input('Press Enter to continue...')
