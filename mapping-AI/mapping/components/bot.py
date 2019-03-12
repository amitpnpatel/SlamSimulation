from .constants import Directions


class Bot:
    def __init__(self):
        self.__head = (0, 1)
        self.__direction = Directions.NORTH

    def do_action(self, action):
        self.__head, self.__direction = action(self.__head, self.__direction)

    def display(self, display_func):
        display_func(self.__head)
