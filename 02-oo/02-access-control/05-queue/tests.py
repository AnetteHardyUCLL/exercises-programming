from student import *


def test_queue():
    queue = Queue()
    assert queue.is_empty()

    queue.add('john')
    assert not queue.is_empty()

    assert queue.next() == 'john'
    assert queue.is_empty()

    queue.add('a')
    queue.add('b')
    queue.add('c')
    assert queue.next() == 'a'
    assert queue.next() == 'b'
    assert queue.next() == 'c'
