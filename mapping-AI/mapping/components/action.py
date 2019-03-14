import numpy as np
import math

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
        current_angle = directionAngle - ((size_sensory_array/2) * DELTA_THETA)

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

            current_angle += DELTA_THETA

        return current, direction, new_internal_map
