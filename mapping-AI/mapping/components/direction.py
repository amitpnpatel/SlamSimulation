import numpy as np
import math
class Direction:
    NORTH = (0, 1)
    NE = (1, 1)
    EAST = (1, 0)
    SE = (1, -1)
    SOUTH = (0, -1)
    SW = (-1, -1)
    WEST = (-1, 0)
    NW = (-1, 1)

    @staticmethod
    def get_direction_angle(direction):
        x,y = direction
        
        angle = np.rad2deg(math.atan2(y, x))
        if np.sign(angle) == -1:
            angle += 360

        return angle
