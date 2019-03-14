import pytest
from mapping.components.constants import MAX_RANGE, METRE_2_PIX
from mapping.components.action import Action
from mapping.components.direction import Direction

import numpy as np

def test_should_move():
    current = (0,0)
    direction = (1,1)

    new_current, direction, _ = Action.move(None, current, direction, None)

    assert new_current == (1,1)

def test_should_turn_left():
    current = (0,0)
    result = Action.turn_left(None, current, Direction.NORTH, None)
    assert result[1] == Direction.NW
    result = Action.turn_left(None, current, Direction.NE, None)
    assert result[1] == Direction.NORTH
    result = Action.turn_left(None, current, Direction.EAST, None)
    assert result[1] == Direction.NE
    result = Action.turn_left(None, current, Direction.SE, None)
    assert result[1] == Direction.EAST
    result = Action.turn_left(None, current, Direction.SOUTH, None)
    assert result[1] == Direction.SE
    result = Action.turn_left(None, current, Direction.SW, None)
    assert result[1] == Direction.SOUTH
    result = Action.turn_left(None, current, Direction.WEST, None)
    assert result[1] == Direction.SW
    result = Action.turn_left(None, current, Direction.NW, None)
    assert result[1] == Direction.WEST

def test_should_turn_right():
    current = (0,0)
    result = Action.turn_right(None, current, Direction.NORTH, None)
    assert result[1] == Direction.NE
    result = Action.turn_right(None, current, Direction.NE, None)
    assert result[1] == Direction.EAST
    result = Action.turn_right(None, current, Direction.EAST, None)
    assert result[1] == Direction.SE
    result = Action.turn_right(None, current, Direction.SE, None)
    assert result[1] == Direction.SOUTH
    result = Action.turn_right(None, current, Direction.SOUTH, None)
    assert result[1] == Direction.SW
    result = Action.turn_right(None, current, Direction.SW, None)
    assert result[1] == Direction.WEST
    result = Action.turn_right(None, current, Direction.WEST, None)
    assert result[1] == Direction.NW
    result = Action.turn_right(None, current, Direction.NW, None)
    assert result[1] == Direction.NORTH

# def test_should_update_map():
#     current = (0,0)
#     direction = Direction.NE

#     # 20 x 20m grid
#     actual_map = 0 * np.ones((20 * METRE_2_PIX, 20 * METRE_2_PIX))
#     actual_map[15:20, 15:20] = 1
#     actual_map[20:25, 10:15] = 1

#     inner_map = -1 * np.ones((20 * METRE_2_PIX, 20 * METRE_2_PIX))
#     result = Action.update_map(sensor_array(current, direction, actual_map, 180), current, Direction.NW, inner_map)
#     # np.save('/Users/divyesingh/Documents/SLAM/workspace/SlamSimulation/mapping-AI/actual.npy', actual_map)
#     # np.save('/Users/divyesingh/Documents/SLAM/workspace/SlamSimulation/mapping-AI/sensed.npy', result[2])
#     # return(result, actual_map)

#     #import pdb; pdb.set_trace()

