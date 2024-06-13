from abc import ABC, abstractmethod
import re
from typing import Dict, List


class Person:
    def __init__(self, id: str, name: str, is_a_student: bool) -> None:
        if not Person.is_valid_name(name):
            raise ValueError("invalid name")
        self.id = id
        self.is_a_student = is_a_student
        self.name = name  # calls name's setter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not Person.is_valid_name(value):
            raise ValueError
        self.__name = value

    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r"[A-Za-z]+[\sA-Za-z]+", name) is not None


class Residence(ABC):
    def __init__(self, address: str, area: float, number_of_rooms: int) -> None:
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants: Dict[int, Person] = {}

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    def maximum_occupants(self) -> int:
        return min(self.area // 20, self.number_of_rooms * 2)

    def register_resident(self, person: Person):
        if person not in self.__occupants:
            if len(self.__occupants) >= self.maximum_occupants:
                raise RuntimeError
            self.__occupants[person.id] = person

    def unregister_resident(self, id):
        del self.__occupants[id]

    @property
    def resident_names(self) -> List[str]:
        return [person.name for person in self.__occupants.values()]

    @abstractmethod
    def calculate_value(self): ...


class Villa(Residence):
    def __init__(
        self, address: str, area: float, number_of_rooms: int, garage_capacity: int
    ) -> None:
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (
            (25000 * self.number_of_rooms)
            + (2100 * self.area)
            + (10000 * self.garage_capacity)
        )


class StudentKot(Residence):
    def __init__(self, address: str, area: float) -> None:
        super().__init__(address, area, number_of_rooms=1)

    def register_resident(self, person: Person):
        if not person.is_a_student:
            raise RuntimeError
        return super().register_resident(person)

    def calculate_value(self):
        return 150000 + (750 * self.area)


# create some people
aimee = Person("12.34.56-789.01", "Aimee Backiel", False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# create some residences
my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
my_kot = StudentKot("Kortestraat 6, 3000 Leuven", 20)

# check the values of the properties
print(my_villa.calculate_value())


print(my_kot.calculate_value())


# move the people into a residence
my_villa.register_resident(aimee)
my_villa.register_resident(bastian)

# check the residents of the villa
print(my_villa.resident_names)


# Someday, sadly Bastian will grow up and move into his student kot
my_villa.unregister_resident(bastian.id)
my_kot.register_resident(bastian)

# check the residents again
print(my_villa.resident_names)


print(my_kot.resident_names)


# With all her free time, Aimee can expand the garage to make space for all her hobbies
my_villa.garage_capacity = 3
print(my_villa.calculate_value())
