import numpy as np
import math
from .constants import MAX_RANGE, DELTA_THETA
from .direction import Direction

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
    def update_map(sensory_array, current, direction, slam_map):
        # update map with data
        direction_angle = Direction.get_direction_angle(direction)
        
        size_sensory_array = len(sensory_array)
        current_angle = direction_angle - ((size_sensory_array/2) * DELTA_THETA)

        slam_map.update_map(sensory_array, current, current_angle)
        
        return current, direction, slam_map
