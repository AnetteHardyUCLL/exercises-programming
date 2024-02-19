import pytest
from student import *


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in globals(), reason=f'{class_name} is not defined')


@if_class_exists('Pawn')
@pytest.mark.parametrize('x', [0, 3, 7])
@pytest.mark.parametrize('y', [0, 4, 7])
@pytest.mark.parametrize('color', ['black', 'white'])
def test_pawn_valid_creation(x, y, color):
    pawn = Pawn(
        position=Position(x, y),
        color=color)
    assert pawn.position == Position(x, y)
    assert pawn.color == color


@if_class_exists('Pawn')
@pytest.mark.parametrize('position', [
    Position(-1, 0),
    Position(8, 0),
    Position(0, -1),
    Position(0, 8),
])
def test_pawn_creation_invalid_position(position):
    with pytest.raises(ValueError):
        Pawn(position=position, color='white')


@if_class_exists('Pawn')
def test_pawn_creation_invalid_color():
    with pytest.raises(ValueError):
        Pawn(position=Position(0, 0), color='red')


@if_class_exists('Pawn')
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x, y),
            'white',
            Position(x, y + 1)
        )
        for x in [0, 2, 6]
        for y in [0, 5, 6]
    ),
    *(
        (
            Position(x, y),
            'black',
            Position(x, y - 1)
        )
        for x in [0, 2, 7]
        for y in [1, 4, 7]
    ),
])
def test_pawn_legal_move(position, color, move):
    pawn = Pawn(position=position, color=color)
    pawn.move(move)
    assert pawn.position == move


@if_class_exists('Pawn')
@pytest.mark.parametrize('position, color, move', [
    (
        Position(0, 0),
        'white',
        Position(0, 2)
    ),
    (
        Position(0, 0),
        'white',
        Position(1, 1)
    ),
    (
        Position(3, 7),
        'white',
        Position(3, 8)
    ),
])
def test_pawn_white_illegal_move(position, color, move):
    pawn = Pawn(position=position, color=color)
    with pytest.raises(ValueError):
        pawn.move(move)
    assert pawn.position == position


@if_class_exists('Pawn')
@pytest.mark.parametrize('position, color, move', [
    (
        Position(0, 0),
        'black',
        Position(0, -1)
    ),
    (
        Position(0, 2),
        'black',
        Position(0, 0)
    ),
    (
        Position(5, 5),
        'black',
        Position(4, 4)
    ),
])
def test_pawn_black_illegal_move(position, color, move):
    pawn = Pawn(position=position, color=color)
    with pytest.raises(ValueError):
        pawn.move(move)
    assert pawn.position == position


@if_class_exists('King')
@pytest.mark.parametrize('x', range(0, 8))
@pytest.mark.parametrize('y', range(0, 8))
@pytest.mark.parametrize('color', ['black', 'white'])
def test_king_valid_creation(x, y, color):
    pawn = King(
        position=Position(x, y),
        color=color)
    assert pawn.position == Position(x, y)
    assert pawn.color == color


@if_class_exists('King')
@pytest.mark.parametrize('position', [
    Position(-1, 0),
    Position(8, 0),
    Position(0, -1),
    Position(0, 8),
])
def test_king_creation_invalid_position(position):
    with pytest.raises(ValueError):
        King(position=position, color='white')


@if_class_exists('King')
def test_king_creation_invalid_color():
    with pytest.raises(ValueError):
        King(position=Position(0, 0), color='red')


@if_class_exists('King')
@pytest.mark.parametrize('position, color, move', [
    *(
        (
            Position(x, y),
            color,
            Position(x + dx, y + dy)
        )
        for x in [0, 4, 7]
        for y in [0, 2, 7]
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if dx != 0 or dy != 0
        if 0 <= x + dx < 8 and 0 <= y + dy < 8
        for color in ['black', 'white']
    ),
])
def test_king_legal_move(position, color, move):
    pawn = King(position=position, color=color)
    pawn.move(move)
    assert pawn.position == move


@if_class_exists('King')
@pytest.mark.parametrize('position, color, move', [
    (
        Position(0, 0),
        'white',
        Position(2, 0),
    ),
    (
        Position(0, 0),
        'white',
        Position(-1, 0),
    ),
    (
        Position(5, 3),
        'black',
        Position(4, 1),
    ),
    (
        Position(5, 3),
        'black',
        Position(5, 3),
    ),
])
def test_king_illegal_move(position, color, move):
    pawn = King(position=position, color=color)
    with pytest.raises(ValueError):
        pawn.move(move)
    assert pawn.position == position


@if_class_exists('Pawn')
@if_class_exists('ChessPiece')
def test_pawn_is_child_class_of_chesspiece():
    assert ChessPiece in Pawn.__mro__


@if_class_exists('King')
@if_class_exists('ChessPiece')
def test_king_is_child_class_of_chesspiece():
    assert ChessPiece in King.__mro__
