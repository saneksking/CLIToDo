from tools.config import Config
from tools.menu import AppMenu


class AppManager:
    def __init__(self):
        self.config = Config()
        self.menu = AppMenu()
