import pytest
from mapping.components.constants import Action, Directions

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
    pass
