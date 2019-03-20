import pytest
import numpy as np
from mapping.components.slam_map import SlamMap
from mapping.components.constants import METRE_2_PIX
from mapping.components import Direction, Action

def test_should_insert_value_as_map_coordinate():
    slam_map = SlamMap(1,1)
    slam_map[3,3] = 3

    expected_map = np.ones((100,100))*-1
    expected_map[3,3] = 3
    assert np.all(slam_map.get_map() == np.flip(expected_map.transpose(), 0))

def test_should_initialize_pre_built_map():
    pre_initialised_map = np.ones((5,5)) * -1
    pre_initialised_map[3,3] = 3
    slam_map = SlamMap(5,5)
    slam_map.set_map(pre_initialised_map)
    expected_map = np.ones((5,5))*-1
    expected_map[3,3] = 3

    assert np.all(slam_map.get_map() == np.flip(expected_map.transpose(), 0))

def test_should_return_the_count_of_elements_with_value():
    slam_map = SlamMap(1,1)
    slam_map[3:5,3:5] = 0

    assert slam_map.get_element_count(0) == 4


# def test_should_return_sensory_array():
#     current = (5,0)
#     direction = Direction.NORTH

#     # 20 x 20m grid
#     actual_map = np.zeros((20 * METRE_2_PIX, 20 * METRE_2_PIX))
#     actual_map[40:50, 50:60] = 1
#     actual_map[450:600, 450:600] = 1

#     slam_map = SlamMap(5, 5)
#     slam_internal = SlamMap(20, 20)
#     slam_map.set_map(actual_map)
#     x = slam_map.sensor_array(current, direction, 180)
#     result = Action.update_map(x, current, direction, slam_internal)
    
#     current = (5, 10)
#     direction = Direction.SOUTH

#     x = slam_map.sensor_array(current, direction, 180)
#     result = Action.update_map(x, current, direction, result[2])

#     current = (0, 5)
#     direction = Direction.EAST

#     x = slam_map.sensor_array(current, direction, 180)
#     result = Action.update_map(x, current, direction, result[2])

#     current = (10, 5)
#     direction = Direction.WEST

#     x = slam_map.sensor_array(current, direction, 180)
#     result = Action.update_map(x, current, direction, result[2])

    
#     np.save('/Users/in-justin.jose/result.npy', result[2].get_map())
#     np.save('/Users/in-justin.jose/actual.npy', slam_map.get_map())

    

