# test_student.py

from student import Wall

def test_wall_volume():
    depth = 3
    height = 4
    width = 5
    wall = Wall(depth, height, width)
    assert wall.volume == depth * height * width
