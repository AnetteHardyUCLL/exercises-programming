class InclusiveRange:
    def __init__(self, start, finish):
        self.__start = start
        self.__finish = finish

    def __iter__(self):
        return InclusiveRangeIterator(self.__start, self.__finish)


class InclusiveRangeIterator:
    def __init__(self, start, finish):
        self.__current = start
        self.__finish = finish

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current <= self.__finish:
            result = self.__current
            self.__current += 1
            return result
        else:
            raise StopIteration()
