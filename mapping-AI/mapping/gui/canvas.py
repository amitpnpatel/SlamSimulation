import sys

import pygame
from pygame.locals import *

from snake.components import Directions


class Canvas:
    __key_map = {
        pygame.K_UP: Directions.UP,
        pygame.K_DOWN: Directions.DOWN,
        pygame.K_LEFT: Directions.LEFT,
        pygame.K_RIGHT: Directions.RIGHT
    }

    def __init__(self, width, height, snake, fruit):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__snake = snake
        self.__fruit = fruit
        self.__pixel_width = 10

        self.__fruit_image = pygame.Surface((self.__pixel_width, self.__pixel_width))
        self.__fruit_image.fill((0, 255, 0))

        self.__snake_image = pygame.Surface((self.__pixel_width, self.__pixel_width))
        self.__snake_image.fill((255, 0, 0))

        self.__timer = 100
        self.__surface = pygame.display.set_mode((width * self.__pixel_width, height * self.__pixel_width))
        self.__clock = pygame.time.Clock()
        pygame.time.set_timer(1, self.__timer)

    def run(self):
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key in self.__key_map:
                    self.__snake.set_direction(self.__key_map[event.key])

            if not self.__snake.step(self.__width, self.__height, self.__fruit):
                pygame.quit()
                sys.exit(1)

            self.__surface.fill((255, 255, 255))

            self.__snake.display(lambda piece: self.__surface.blit(
                self.__snake_image, (piece[0] * self.__pixel_width, (self.__height - piece[1] - 1) * self.__pixel_width)
            ))

            self.__fruit.display(lambda piece: self.__surface.blit(
                self.__fruit_image, (piece[0] * self.__pixel_width, (self.__height - piece[1] - 1) * self.__pixel_width)
            ))

            pygame.display.flip()
