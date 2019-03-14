import pytest
from mapping.components.direction import Direction

def test_should_return_direction_angle():
    assert Direction.get_direction_angle(Direction.NORTH) == 90
    assert Direction.get_direction_angle(Direction.NE) == 45
    assert Direction.get_direction_angle(Direction.EAST) == 0
    assert Direction.get_direction_angle(Direction.SE) == 315
    assert Direction.get_direction_angle(Direction.SOUTH) == 270
    assert Direction.get_direction_angle(Direction.SW) == 225
    assert Direction.get_direction_angle(Direction.WEST) == 180
    
