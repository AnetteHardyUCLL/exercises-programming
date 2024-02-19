import pytest
from student import CircularBuffer


def test_len():
    buffer = CircularBuffer(5)

    assert len(buffer) == 0
    buffer.add(1)
    assert len(buffer) == 1

    buffer.add(2)
    assert len(buffer) == 2

    buffer.add(3)
    assert len(buffer) == 3

    buffer.add(4)
    assert len(buffer) == 4

    buffer.add(5)
    assert len(buffer) == 5

    buffer.add(6)
    assert len(buffer) == 5

    buffer.add(7)
    assert len(buffer) == 5


def test_indexing():
    buffer = CircularBuffer(5)

    assert [buffer[i] for i in range(len(buffer))] == []
    buffer.add(1)
    assert [buffer[i] for i in range(len(buffer))] == [1]

    buffer.add(4)
    assert [buffer[i] for i in range(len(buffer))] == [1, 4]

    buffer.add(9)
    assert [buffer[i] for i in range(len(buffer))] == [1, 4, 9]

    buffer.add(2)
    assert [buffer[i] for i in range(len(buffer))] == [1, 4, 9, 2]

    buffer.add(5)
    assert [buffer[i] for i in range(len(buffer))] == [1, 4, 9, 2, 5]

    buffer.add(0)
    assert [buffer[i] for i in range(len(buffer))] == [4, 9, 2, 5, 0]

    buffer.add(7)
    assert [buffer[i] for i in range(len(buffer))] == [9, 2, 5, 0, 7]
