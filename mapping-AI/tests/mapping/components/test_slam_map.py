import pytest
import numpy as np
from mapping.components.slam_map import SlamMap

def test_should_insert_value_as_map_coordinate():
    slam_map = SlamMap(5,5)
    slam_map[3,3] = 3

    expected_map = np.ones((5,5))*-1
    expected_map[1,3] = 3

    assert np.all(slam_map.slam_map == expected_map)

def test_should_initialize_pre_built_map():
    pre_initialised_map = np.ones((5,5)) * -1
    pre_initialised_map[3,3] = 3
    slam_map = SlamMap(5,5)
    slam_map.set_map(pre_initialised_map)
    expected_map = np.ones((5,5))*-1
    expected_map[1,3] = 3

    assert np.all(slam_map.slam_map == expected_map)
