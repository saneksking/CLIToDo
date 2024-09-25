from output_decorator.decorators import StringDecorator
from tools.app_manager import AppManager


def main():
    app_manager = AppManager()
    StringDecorator().string_decorate(text=app_manager.config.title,  symbol='|')

    StringDecorator().string_decorate()
    StringDecorator().string_decorate(text=app_manager.config.description, symbol="|")
    StringDecorator().string_decorate()

    app_manager.menu.start_menu()

    StringDecorator().string_decorate()
    StringDecorator().string_decorate(text=app_manager.config.copr, symbol='|')
    StringDecorator().string_decorate()


if __name__ == '__main__':
    main()
