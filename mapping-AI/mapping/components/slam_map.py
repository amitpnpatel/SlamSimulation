import numpy as np
from mapping.components.constants import MAX_RANGE, len2ind, cos, sin, DELTA_R, DELTA_THETA
from .action import Action
from .direction import Direction

class SlamMap:
    def __init__(self, width, height):
        self.__np_map = np.ones((width, height)) * -1
        self.slam_map = np.flip(self.__np_map, 0)

    def set_map(self, pre_initialised_map):
        self.__np_map = pre_initialised_map
        self.slam_map = np.flip(self.__np_map, 0)        

    def __getitem__(self, key):
        return self.slam_map[key]

    def __setitem__(self, key, value):
        self.__np_map[key] = value

    def sensor_array(self, current_position, direction, fov):
    #create sensory_array
        xc, yc = current_position

        direction_angle = Direction.get_direction_angle(direction)
        
        size_sensory_array = int(fov//DELTA_THETA)
        sensory_array = [np.inf for i in range(size_sensory_array)] #  np.ones(size_sensory_array, dtype=np.int) * np.inf

        current_angle = direction_angle - ((size_sensory_array/2) * DELTA_THETA)

        for scan in range(size_sensory_array):
            for i in np.arange(0, MAX_RANGE, DELTA_R):

                xInd, yInd = len2ind(xc, i, cos, current_angle), len2ind(yc, i, sin, current_angle)
                if xInd in (-1, size_sensory_array) or yInd in (-1, size_sensory_array):
                        sensory_array[scan] = np.sqrt((xInd/Direction.METRE_2_PIX)**2 + (yInd/Direction.METRE_2_PIX)**2)
                else:
                    val = self.slam_map[xInd, yInd]
                    if val == 1:
                        sensory_array[scan] = np.sqrt((xInd/Direction.METRE_2_PIX)**2 + (yInd/Direction.METRE_2_PIX)**2)

            current_angle += Direction.DELTA_THETA

        return sensory_array



