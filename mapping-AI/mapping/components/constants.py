import math
import numpy as np

MAX_RANGE = 10
METRE_2_PIX = 5
DELTA_R = 0.1

cos = lambda x: np.cos(np.deg2rad(x))
sin = lambda x: np.sin(np.deg2rad(x))

len2ind = lambda cPos, rad, func, alpha: math.floor( (cPos + rad * func(alpha)) * METRE_2_PIX )

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
    METRE_2_PIX = 5


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
        directionAngle = np.rad2deg(math.atan2(y, x))
        if np.sign(directionAngle) == -1:
            directionAngle += 360

        maxr = MAX_RANGE

        size_sensory_array = len(sensory_array)
        current_angle = directionAngle - ((size_sensory_array/2) * Directions.DELTA_THETA)

        for scan in sensory_array:
            if scan != math.inf:
                radius = scan
                new_internal_map[len2ind(xc, radius, cos, current_angle)][
                    len2ind(yc, radius, sin, current_angle)] = 1
            else:
                radius = maxr

            for i in np.arange(0, radius, DELTA_R):
                new_internal_map[len2ind(xc, i, cos, current_angle)][
                    len2ind(yc, i, sin, current_angle)] = 0

            current_angle += Directions.DELTA_THETA

        return current, direction, new_internal_map
