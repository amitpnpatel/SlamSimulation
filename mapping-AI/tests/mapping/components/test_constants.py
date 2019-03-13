import pytest
from mapping.components.constants import Action, Directions, MAX_RANGE
from tests.map2sensorArray import sensor_array
import numpy as np

def test_should_move():
    current = (0,0)
    direction = (1,1)

    new_current, direction, _ = Action.move(None, current, direction, None)

    assert new_current == (1,1)

def test_should_turn_left():
    current = (0,0)
    result = Action.turn_left(None, current, Directions.NORTH, None)
    assert result[1] == Directions.NW
    result = Action.turn_left(None, current, Directions.NE, None)
    assert result[1] == Directions.NORTH
    result = Action.turn_left(None, current, Directions.EAST, None)
    assert result[1] == Directions.NE
    result = Action.turn_left(None, current, Directions.SE, None)
    assert result[1] == Directions.EAST
    result = Action.turn_left(None, current, Directions.SOUTH, None)
    assert result[1] == Directions.SE
    result = Action.turn_left(None, current, Directions.SW, None)
    assert result[1] == Directions.SOUTH
    result = Action.turn_left(None, current, Directions.WEST, None)
    assert result[1] == Directions.SW
    result = Action.turn_left(None, current, Directions.NW, None)
    assert result[1] == Directions.WEST

def test_should_turn_right():
    current = (0,0)
    result = Action.turn_right(None, current, Directions.NORTH, None)
    assert result[1] == Directions.NE
    result = Action.turn_right(None, current, Directions.NE, None)
    assert result[1] == Directions.EAST
    result = Action.turn_right(None, current, Directions.EAST, None)
    assert result[1] == Directions.SE
    result = Action.turn_right(None, current, Directions.SE, None)
    assert result[1] == Directions.SOUTH
    result = Action.turn_right(None, current, Directions.SOUTH, None)
    assert result[1] == Directions.SW
    result = Action.turn_right(None, current, Directions.SW, None)
    assert result[1] == Directions.WEST
    result = Action.turn_right(None, current, Directions.WEST, None)
    assert result[1] == Directions.NW
    result = Action.turn_right(None, current, Directions.NW, None)
    assert result[1] == Directions.NORTH

def test_should_update_map():
    current = (0,0)
    direction = Directions.NE

    # 20 x 20m grid
    actual_map = 0 * np.ones((20 * Directions.METRE_2_PIX, 20 * Directions.METRE_2_PIX))
    actual_map[15:20, 15:20] = 1
    actual_map[20:25, 10:15] = 1

    inner_map = -1 * np.ones((20 * Directions.METRE_2_PIX, 20 * Directions.METRE_2_PIX))
    result = Action.update_map(sensor_array(current, direction, actual_map, 180), current, Directions.NW, inner_map)
    np.save('/Users/divyesingh/Documents/SLAM/workspace/SlamSimulation/mapping-AI/actual.npy', actual_map)
    np.save('/Users/divyesingh/Documents/SLAM/workspace/SlamSimulation/mapping-AI/sensed.npy', result[2])
    # return(result, actual_map)

    #import pdb; pdb.set_trace()

