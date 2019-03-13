import math
import numpy as np

class Directions:
    NORTH = (0, 1)
    NE = (1, 1)
    EAST = (1, 0)
    SE = (1, -1)
    SOUTH = (0, -1)
    SW = (-1, -1)
    WEST = (-1, 0)
    NW = (-1, 1)
    DELTA_THETA = 0.5


class Action:
    @staticmethod
    def move(sensory_array, current, direction, internal_map):
        return (current[0] + direction[0], current[1] + direction[1]), direction, internal_map

    @staticmethod
    def turn_left(sensory_array, current, direction, internal_map):
        x, y = direction
        new_x, new_y = (x - y, x + y)

        new_x = (new_x / abs(new_x)) if new_x != 0 else new_x
        new_y = (new_y / abs(new_y)) if new_y != 0 else new_y
        return current, (new_x, new_y), internal_map

    @staticmethod
    def turn_right(sensory_array, current, direction, internal_map):
        x, y = direction
        new_x, new_y = (x + y, y - x)

        new_x = (new_x / abs(new_x)) if new_x != 0 else new_x
        new_y = (new_y / abs(new_y)) if new_y != 0 else new_y
        return current, (new_x, new_y), internal_map

    @staticmethod
    def update_map(sensory_array, current, direction, internal_map):
        # update map with data
        xc, yc = current
        new_internal_map = internal_map
        x, y = direction
        directionAngle = math.atan(y / x)

        maxr = 10
        delta_r = 0.5

        size_sensory_array = len(sensory_array)
        current_angle = directionAngle - ((size_sensory_array/2) * Directions.DELTA_THETA)

        for scan in sensory_array:
            if scan != math.inf:
                new_internal_map[xc + radius * math.cos(current_angle)][
                    yc + radius * math.sin(current_angle)] = 1
                radius = scan
            else:
                radius = maxr

            for i in np.arange(0, radius, delta_r):
                new_internal_map[xc + i * math.cos(current_angle)][
                    yc + i * math.sin(current_angle)] = 0

            current_angle += Directions.DELTA_THETA

        return current, direction, new_internal_map
