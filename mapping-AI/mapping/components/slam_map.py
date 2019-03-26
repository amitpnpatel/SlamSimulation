import numpy as np
import math
import cv2
from .constants import MAX_RANGE, len2ind, cos, sin, DELTA_R, DELTA_THETA, METRE_2_PIX, cart2pol, len2ind_np, MULTIPLIER
from .action import Action
from .direction import Direction
import time

class SlamMap:
    def __init__(self, width, height):
        self.__np_map = np.ones((width * METRE_2_PIX, height * METRE_2_PIX)) * -1


    def set_map(self, pre_initialised_map):
        self.__np_map = pre_initialised_map

    def __getitem__(self, key):
        return self.__np_map[key]

    def __setitem__(self, key, value):
        self.__np_map[key] = value

    def get_element_count(self, value):
        return len(self.__np_map[self.__np_map == value])

    def shape(self):
        return self.__np_map.shape

    def get_map(self):
        return  np.flip(self.__np_map.transpose(), 0)

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

    def sensor_array(self, current_position, direction, fov_angle, r_t_fov):
        seconds = time.time()
        #create sensory_array
        direction_angle = Direction.get_direction_angle(direction)
        size_sensory_array = int(fov_angle/DELTA_THETA)
        current_angle =  direction_angle - (((size_sensory_array)/2) * DELTA_THETA)

        angle_buckets = np.array([current_angle + i * DELTA_THETA for i in range(size_sensory_array)])
        theta = np.copy(r_t_fov)
        theta[:,1] = theta[:,1] + current_angle

        xy_coord = np.empty(r_t_fov.shape)
        xy_coord[:,0] = len2ind_np(current_position[0], theta[:,0], cos, theta[:,1])
        xy_coord[:,1] = len2ind_np(current_position[1], theta[:,0], sin, theta[:,1])

        non_zero_coord = np.transpose(np.nonzero(self.__np_map))
        xy1 = xy_coord[:,0] * 10000 +  xy_coord[:,1]
        xy2 = non_zero_coord[:,0] * 10000 + non_zero_coord[:,1]

        # Long procedure approx 2 secs
        index = np.argsort(xy2)
        sorted_xy2 = xy2[index]
        sorted_index = np.searchsorted(sorted_xy2, xy1)
        yindex = np.take(index, sorted_index, mode="clip")
        xy3 = theta[xy2[yindex] == xy1]
        angles = np.unique(xy3[:,1])
        sensor_array = np.ones(angle_buckets.shape)*np.inf

        for angle in angles:
            sensor_array[angle_buckets == angle] = np.min(xy3[xy3[:,1] == angle][:,0])

        sensor_array[(sensor_array > MAX_RANGE) | (sensor_array <= 0)] = np.inf

        print(time.time() - seconds)
        return sensor_array

    def update_map(self, sensory_array, current_position, current_angle):
        seconds = time.time()
        xc, yc = current_position
        sensory_array_updated = [
            (MAX_RANGE if scan == np.inf else scan, np.round(current_angle + i * DELTA_THETA, 3), scan == np.inf)
            for i, scan in enumerate(sensory_array)
        ]

        # Flipping X, Y for opencv to do the manipulation on numpy array
        scan_lines = [
            (
                (yc * METRE_2_PIX, xc * METRE_2_PIX),
                (len2ind(yc, radius, sin, theta), len2ind(xc, radius, cos, theta))
            ) for radius, theta, _ in sensory_array_updated
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

        if MULTIPLIER != 1:

            if (DELTA_R/MULTIPLIER) > 0.025:
                print("Applying dilation")
                kernel = np.ones((MULTIPLIER-1,MULTIPLIER-1),np.uint8)
                self.__np_map = cv2.dilate(self.__np_map, kernel, iterations = 1)
            else:
                print("Applying openning")
                kernel = np.ones((MULTIPLIER+1,MULTIPLIER+1),np.uint8)
                self.__np_map = cv2.morphologyEx(self.__np_map, cv2.MORPH_CLOSE, kernel)

        print(time.time() - seconds)
