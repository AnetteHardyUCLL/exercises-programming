# test_student.py

from student import Wall

def test_wall_armor():
    wall = Wall()
    assert wall.armor == 10

def test_wall_height():
    wall = Wall()
    assert wall.height == 5

def test_wall_fortify():
    wall = Wall()
    wall.fortify()
    assert wall.armor == 20  # Since fortify doubles the armor

def test_wall_fortify_multiple_times():
    wall = Wall()
    wall.fortify()
    wall.fortify()
    assert wall.armor == 40  # After fortifying twice, armor should be 40
