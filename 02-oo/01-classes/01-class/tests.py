# test_student.py

from student import Wall

def test_wall_armor():
    wall = Wall()
    assert wall.armor == 10

def test_wall_height():
    wall = Wall()
    assert wall.height == 5
