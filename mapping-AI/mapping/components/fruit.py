from random import randint


class Fruit:
    def __init__(self):
        self.__fruit = None

    def __eq__(self, coord):
        return self.__fruit == coord

    def place_fruit(self, width=None, height=None, snake=None, coord=None):
        if coord:
            self.__fruit = coord
            return

        while True:
            x = randint(0, width-1)
            y = randint(0, height-1)
            if (x, y) not in snake:
                self.__fruit = x, y
                return

    def display(self, display_func):
        display_func(self.__fruit)
