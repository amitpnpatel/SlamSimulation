from .constants import MAX_RANGE, DELTA_R, DELTA_THETA
from .direction import Direction
from .slam_map import SlamMap
from .action import Action
import numpy as np


class Bot:
    bot_actions = {
        'UPDATE_MAP': Action.update_map,
        'MOVE': Action.move,
        'TURN_LEFT': Action.turn_left,
        'TURN_RIGHT': Action.turn_right
    }
    
    def __init__(self, width, height, model, sensor):
        self.__current = (0, 1)
        self.__direction = Directions.NORTH
        self.__internal_map = SlamMap(width, height)
        self.__model = model
        self.__sensor = sensor
        self.__fov = 180
        self.__r_t_fov = np.array([(r, t) for r in np.arange(0,MAX_RANGE,DELTA_R) for t in np.arange(0,self.__fov, DELTA_THETA)])

    def do_action(self, sensory_array, action_key):
        self.__current, self.__direction, self.__internal_map = self.bot_action[action_key](
            sensory_array, self.__current, self.__direction, self.__internal_map
        )

    def unknown_map_ratio(self):
        unknown_count = self.__internal_map.get_element_count(-1)
        total_elements = np.prod(self.__internal_map.shape)
        return unknown_count / total_elements

    def iter(self):
        sensory_array = self.__sensor.sensor_array(self.__current, self.__direction, self.__fov)
        action_key = self.__model.get_action(sensor_array)
        self.do_action(sensory_array, action_key)
        
