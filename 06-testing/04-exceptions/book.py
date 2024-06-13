class Book:
    def __init__(self, title, isbn):
        if not Book.__is_valid_title(title):
            raise RuntimeError("invalid title")
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError("invalid isbn")
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def isbn(self):
        return self.__isbn

    @staticmethod
    def __is_valid_title(title):
        return len(title) > 0

    @staticmethod
    def __is_valid_isbn(isbn):
        digits = [int(char) for char in isbn if "0" <= char <= "9"]
        if len(digits) != 13:
            return False

        for i in range(len(digits)):
            if i % 2 != 0:
                digits[i] *= 3

        return sum(digits) % 10 == 0
