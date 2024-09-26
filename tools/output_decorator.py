import shutil


class StringDecorator:
    @classmethod
    def term_width(cls):
        return shutil.get_terminal_size()[0]

    @classmethod
    def string_decorate(cls, text='', symbol='*', print_flag=True):
        if text:
            result_string = f' {text} '.center(cls.term_width(), symbol)
        else:
            result_string = ''.center(cls.term_width(), symbol)

        if print_flag:
            print(result_string)
        else:
            return result_string
