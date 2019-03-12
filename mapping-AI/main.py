from snake.components import Snake, Fruit
from snake.gui import Canvas


def main():
    height = 50
    width = 50

    snake = Snake()
    fruit = Fruit()
    fruit.place_fruit(coord=(width // 2, height // 2))

    canvas = Canvas(width, height, snake, fruit)

    canvas.run()


main()
