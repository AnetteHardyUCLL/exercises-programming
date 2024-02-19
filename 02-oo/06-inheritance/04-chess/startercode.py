class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, dx, dy):
        """
        Returns a new Position object that has been moved horizontally by dx
        and vertically by dy.
        """
        return Position(self.x + dx, self.y + dy)

    def __repr__(self):
        return f'Position({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, Position):
            raise NotImplemented()
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Pawn:
    def __init__(self, position, color):
        if not Pawn.is_valid_position(position):
            raise ValueError('invalid position')
        if not Pawn.is_valid_color(color):
            raise ValueError('invalid color')
        self.__position = position
        self.__color = color

    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color

    @staticmethod
    def is_valid_color(color):
        return color in ['black', 'white']

    @staticmethod
    def is_valid_position(position):
        return 0 <= position.x < 8 and 0 <= position.y < 8

    def is_legal_move(self, new_position):
        if not self.is_valid_position(new_position):
            return False
        direction = 1 if self.color == 'white' else -1
        return self.position.move(0, direction) == new_position

    def move(self, new_position):
        if not self.is_legal_move(new_position):
            raise ValueError("illegal move")
        self.__position = new_position


class King:
    def __init__(self, position, color):
        if not King.is_valid_position(position):
            raise ValueError('invalid position')
        if not King.is_valid_color(color):
            raise ValueError('invalid color')
        self.__position = position
        self.__color = color

    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color

    @staticmethod
    def is_valid_color(color):
        return color in ['black', 'white']

    @staticmethod
    def is_valid_position(position):
        return 0 <= position.x < 8 and 0 <= position.y < 8

    def is_legal_move(self, new_position):
        if new_position == self.position:
            return False
        if not King.is_valid_position(new_position):
            return False
        if abs(new_position.x - self.position.x) > 1:
            return False
        if abs(new_position.y - self.position.y) > 1:
            return False
        return True

    def move(self, new_position):
        if not self.is_legal_move(new_position):
            raise ValueError("illegal move")
        self.__position = new_position
