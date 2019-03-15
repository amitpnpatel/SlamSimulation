import numpy as np
import math
import cv2
from .constants import MAX_RANGE, len2ind, cos, sin, DELTA_R, DELTA_THETA, METRE_2_PIX
from .action import Action
from .direction import Direction
import time

class SlamMap:
    def __init__(self, width, height):
        self.__np_map = np.ones((width, height)) * -1

    def set_map(self, pre_initialised_map):
        self.__np_map = pre_initialised_map    

    def __getitem__(self, key):
        return self.__np_map[key]

    def __setitem__(self, key, value):
        self.__np_map[key] = value

    def get_map(self):
        return np.flip(self.__np_map.transpose(), 0)
        
    def __get_line_of_sight(self, line, starting_angle, current_position, size_sensory_array):
        current_angle = starting_angle + (line * DELTA_THETA)
        xc, yc = current_position

        for i in np.arange(0, MAX_RANGE, DELTA_R):
            xInd, yInd = len2ind(xc, i, cos, current_angle), len2ind(yc, i, sin, current_angle)
            if xInd in (-1, self.__np_map.shape[0]) or yInd in (-1, self.__np_map.shape[1]):
                return np.inf

            if self.__np_map[xInd, yInd] == 1:
                return np.sqrt(((xInd/METRE_2_PIX) - xc)**2 + ((yInd/METRE_2_PIX) - yc)**2)

        return np.inf

    def sensor_array(self, current_position, direction, fov_angle):
        seconds = time.time()
        #create sensory_array

        direction_angle = Direction.get_direction_angle(direction)
        size_sensory_array = int(fov_angle//DELTA_THETA)
        current_angle = direction_angle - ((size_sensory_array/2) * DELTA_THETA)
        
        
        x =  [self.__get_line_of_sight(scan, current_angle, current_position, size_sensory_array) for scan in range(size_sensory_array)]
        print(time.time() - seconds)
        return x

    def update_map(self, sensory_array, current_position, current_angle):
        seconds = time.time()
        xc, yc = current_position
        sensory_array_updated = [
            (MAX_RANGE if scan == np.inf else scan, current_angle + i * DELTA_THETA, scan == np.inf)
            for i, scan in enumerate(sensory_array)
        ]

        # Flipping X, Y for opencv to do the manipulation on numpy array
        scan_lines = [
            (
                (yc * METRE_2_PIX, xc * METRE_2_PIX),
                (len2ind(yc, radius, sin, theta), len2ind(xc, radius, cos, theta))
            ) for radius, theta, is_inf in sensory_array_updated
        ]

        sensed_points = [
            (len2ind(xc, radius, cos, theta), len2ind(yc, radius, sin, theta))
            for radius, theta, is_inf in sensory_array_updated if not is_inf
        ]        

        for line in scan_lines:
            self.__np_map = cv2.line(self.__np_map, *line, 0, 1)

        # update map with data
        for sensed_point in sensed_points:
                self.__np_map[sensed_point] = 1
        print(time.time() - seconds)
