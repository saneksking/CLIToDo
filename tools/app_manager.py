import sys

from output_decorator import StringDecorator

from tools.base_commands import insert_data, get_all_data, get_object_by_id
from tools.config import Config


class AppManager:
    def __init__(self):
        self.config = Config()

    def show_head(self):
        StringDecorator().string_decorate(text=self.config.title)

    def show_description(self):
        StringDecorator().string_decorate()
        StringDecorator().string_decorate(text=self.config.description, symbol="|")
        StringDecorator().string_decorate()

    def show_footer(self):
        StringDecorator().string_decorate()
        StringDecorator().string_decorate(text=self.config.copr, symbol='|')
        StringDecorator().string_decorate()

    def start_menu(self):
        while True:
            print('Choice action:')
            print(
                '1. Create ToDo\n'
                '2. ToDo list\n'
                '0. Exit'
            )
            StringDecorator.string_decorate(symbol='-')
            choice = input("Input: ")
            if choice == '0':
                self.show_footer()
                sys.exit()
            elif choice == '1':
                self.create_todo_menu()
                StringDecorator.string_decorate(symbol='-')
                continue
            elif choice == '2':
                self.todo_list_menu()
                StringDecorator.string_decorate(symbol='-')
            else:
                StringDecorator.string_decorate(symbol='-')
                print('Invalid input!')
                StringDecorator.string_decorate()
                self.enter_to_continue()
                StringDecorator.string_decorate()
                continue

    def create_todo_menu(self):
        while True:
            name = input('Enter a ToDo name: ')
            StringDecorator.string_decorate()
            if name == '':
                print('Invalid input!')
                self.enter_to_continue()
                StringDecorator.string_decorate()
                continue
            description = input('Enter a description: ')
            StringDecorator.string_decorate()
            try:
                insert_data(name=name, description=description, is_active=0)
                print('ToDo created!')
                StringDecorator.string_decorate(symbol='-')
            except Exception as e:
                print(f'Error! ToDo does not create: {e}')
            self.enter_to_continue()
            self.start_menu()
            break

    def todo_list_menu(self):
        while True:
            StringDecorator().string_decorate(text='ToDo list')
            StringDecorator().string_decorate()
            to_do_list = get_all_data()
            for n, todo in enumerate(to_do_list, 1):
                if todo['is_active']:
                    status = 'Complete'
                else:
                    status = 'Uncompleted'
                print(f'{n}. Name: {todo["name"]} | Status: {status} | ID: {todo['id']}')
            print('0. Back')
            StringDecorator().string_decorate(symbol='-')
            todo_choice = input("Choice ToDo ID: ")
            if todo_choice == '0':
                break
            elif todo_choice == '':
                StringDecorator().string_decorate(symbol='-')
                print('Invalid input!')
                self.enter_to_continue()
                continue
            else:
                self.to_do_menu(todo_choice)
        StringDecorator().string_decorate(symbol='-')
        self.start_menu()

    def to_do_menu(self, todo_id):
        todo = {}
        try:
            todo = get_object_by_id(int(todo_id))
        except Exception as e:
            StringDecorator().string_decorate(symbol='-')
            print(f'Error! ToDo does not exist: {e}')
            self.enter_to_continue()
            self.todo_list_menu()

        while True:
            StringDecorator().string_decorate()
            StringDecorator().string_decorate(text=f'ToDo {todo['name']}')
            StringDecorator().string_decorate()
            StringDecorator().string_decorate(text=f'ToDo name: {todo["name"]}'
                                                   f' | Description: {todo["description"]}'
                                                   f' | Status: {todo["is_active"]}',
                                              symbol='=')
            StringDecorator().string_decorate(symbol='-')
            print('Choice action:\n'
                  '1. Update ToDo\n'
                  '2. Complete it\n'
                  '3. Delete it\n'
                  '0. Back')
            StringDecorator().string_decorate(symbol='-')
            choice = input("Input: ")
            if choice == '0':
                break
            elif choice == '1':
                self.update_todo(todo)
                self.enter_to_continue()
                continue
            elif choice == '2':
                self.complete_todo(todo)
                self.enter_to_continue()
                continue
            elif choice == '3':
                self.delete_todo(todo)
                self.enter_to_continue()
                continue
            else:
                StringDecorator().string_decorate(symbol='-')
                print('Invalid input!')
                self.enter_to_continue()
                continue
        self.todo_list_menu()

    def update_todo(self, todo_id):
        print('Updating ToDo')

    def complete_todo(self, todo_id):
        print('Completing ToDo')

    def delete_todo(self, todo_id):
        print('Deleting ToDo')

    @staticmethod
    def enter_to_continue():
        StringDecorator.string_decorate(symbol='-')
        input('Press Enter to continue...')
        StringDecorator.string_decorate(symbol='-')

    def run(self):
        self.show_head()
        self.show_description()
        self.start_menu()
