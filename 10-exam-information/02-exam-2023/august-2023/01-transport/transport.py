import re
from abc import ABC, abstractmethod
from typing import Dict, List


class Passenger:
    def __init__(self, id: str, name: str, money: int) -> None:
        self.id = id
        self.money = money
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not Passenger.is_valid_name(value):
            raise ValueError
        self.__name = value

    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r"[A-Za-z]+[\sA-Za-z]+", name) is not None


class Vehicle(ABC):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants: Dict[str:Passenger] = {}

    @property
    def number_of_occupants(self) -> int:
        return len(self.__occupants)

    @property
    @abstractmethod
    def maximum_occupants(self): ...

    def add_passenger(self, passenger: Passenger):
        self.__occupants[passenger.id] = passenger

    def remove_passenger(self, passenger: Passenger):
        del self.__occupants[passenger.id]

    def remove_all_passengers(self):
        self.__occupants.clear()

    @property
    def occupant_names(self) -> List[str]:
        return [passenger.name for passenger in self.__occupants.values()]


class Taxi(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int):
        super().__init__(license_plate, amount_of_seats)
        self.is_available: bool = True

    @property
    def maximum_occupants(self) -> int:
        return self.amount_of_seats

    def pickup(self, passengers: List[Passenger], distance: float):
        if not self.is_available or len(passengers) > self.maximum_occupants:
            raise ValueError("Taxi is unavailable or too many passengers.")

        fare = max(5, 1 + distance)
        if passengers[0].money < fare:
            raise RuntimeError("Passenger does not have enough money.")

        passengers[0].money -= fare
        for passenger in passengers:
            self.add_passenger(passenger)
        self.is_available = False

    def dropoff(self):
        self.remove_all_passengers()
        self.is_available = True


class Bus(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        super().__init__(license_plate, amount_of_seats)

    @property
    def maximum_occupants(self) -> int:
        return 2 * self.amount_of_seats

    def board(self, passenger: Passenger):
        if self.number_of_occupants + 1 > self.maximum_occupants:
            raise RuntimeError("Bus is full.")

        fare = 2
        if passenger.money < fare:
            raise RuntimeError("Passenger does not have enough money.")
        else:
            passenger.money -= fare
            self.add_passenger(passenger)

    def disembark(self, passenger: Passenger):
        self.remove_passenger(passenger)


# ---- EXAMPLE USAGE ----

# create some passengers
aimee = Passenger("12.34.56-789.01", "Aimee Backiel", 40)
bastian = Passenger("01.02.03-040.05", "Bastian Li Backiel", 5)

# create some vehicles
my_taxi = Taxi("1-NGL-760", 4)
my_bus = Bus("1-HUE-344", 30)

# taking a bus ride together; Bastian likes to pay for himself
my_bus.board(aimee)
my_bus.board(bastian)

# check the occupants of the bus
print(my_bus.occupant_names)

# they get off at the zoo
my_bus.disembark(aimee)
my_bus.disembark(bastian)

# check the occupants again
print(my_bus.occupant_names)

# Bastian wants to take the bus alone for the first time, and Aimee follows him in a taxi
# they only ride 5 km to be sure he doesn't get lost
my_bus.board(bastian)
my_taxi.pickup([aimee], 5)

# check the occupants in each vehicle
print(my_bus.occupant_names)

print(my_taxi.occupant_names)


# check how much money remains in their wallets
print(aimee.money)
print(bastian.money)
