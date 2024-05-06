# Exam Question 1: Transportation Vehicles

* Place all code for this exercise in `transport.py`.
* In these instructions we will always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure to get the names exactly right, even those of the parameters.
* You have received a `basic_test_transport.py` file which contains basic testing, like if certain classes exist and if you've used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_test_transport.py
    ```

  * A missing class will cause tests focusing on that class to be skipped.
    Skipped tests therefore still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests means that your code is definitely incomplete or incorrect.
    But passing tests do not mean that your code is fully correct!
* You must also create some of your own tests in the `test-transport.py` file.
  * Any tests you must write yourself are indicated in this assignment file.
  * You may add additional tests here if you want to check your code more thoroughly. Only those asked for in the assignment will be graded.
  * This test file must be able to run correctly to earn credit.

## Passenger

* Define a class `Passenger`.
* Define a static method `is_valid_name(name)` that returns `True` if `name` is valid and `False` otherwise.
  * A name must consist of at least two parts separated by a space.
  * Examples: "Harry Styles" and "Machine Gun Kelly" are valid names, but "Rihanna" is not.
* Define `Passenger`'s constructor.
  * The constructor takes three parameters: `id` (a string), `name` (a string), and `money` (an int).
  * The constructor should raise a `ValueError` if the name is invalid.
* Store `id` and `money` in public fields.
* Store `name` in a private field and make it accessible via a property.
  * Define a getter and a setter for `name`.

## Vehicle

A `Vehicle` represents a vehicle that people can use to go to a destination, some of which require paying a fare. There are multiple types of vehicles but all vehicles share some common members. Therefore we will create an abstract class `Vehicle` to store common features of different vehicle types.

* Define an abstract class `Vehicle`.
* Define a constructor for `Vehicle`.
  * It has two parameters: `license_plate` (a string), `amount_of_seats` (an int)
  * Store these in *public* fields.
  * Add another *private* field `occupants` to store a dictionary of all the people riding in this `Vehicle`. <br>
      This dictionary will use `Passenger` ids as keys and `Passenger` objects as values.
  * Upon creation, a `Vehicle` has no people registered as riding in it.
* Define a read-only property `number_of_occupants` which returns the number of `Passengers`s registered for this `Vehicle`.
* Define an abstract read-only property `maximum_occupants`.
* Define a method `add_passenger(passenger)` to add a `Passenger` to the `occupants` dictionary with their id as the key and the `passenger` as the item.
* Define a method `remove_passenger(passenger)` to remove a `Passenger` from the `occupants` dictionary.
* Define a method `remove_all_passengers()` to remove all `Passenger`s from the `occupants` dictionary.
* Define a property `occupant_names` which returns a list of the names (strings) of all the people riding in this `Vehicle`.
  * Use what you learned about functional programming to generate this list.

## Types of Vehicles

As previously stated, there are different kinds of vehicles: taxis, busses, cars, planes, etc.
Common functionality was already implemented in `Vehicle`. Below we will define two such subclasses to differentiate between types of vehicles. To keep this exam from becoming too long, we will only implement `Bus` and `Taxi`.

### `Taxi`

A `Taxi` inherits from `Vehicle`. Each seat in a `Taxi` can hold exactly one passenger.

* Define a constructor for `Taxi`.
  * It has two parameters: both inherited from `Vehicle`'s constructor.
  * Add another public field `is_available`. This boolean indicates if the `Taxi` is available to accept new passengers. When a `Taxi` is created, it is by default available. It becomes unavailable when it picks up one or more passengers.
* Implement `maximum_occupants`: one passenger per seat.
* Create a method `pickup(passengers, distance)`. The parameter `passengers` is a list of `Passenger` objects who would like to ride in the `Taxi` and `distance` is how far in kilometers they need to go. Assume the entire group is traveling together from beginning to end of their journey. The following should happen:
  * A `ValueError` should be thrown if the `Taxi` is currently unavailable or if the number of passengers exceeds the maximum number allowed in this `Taxi`.
  * If the `Taxi` is available and can accommodate the passengers:
    * Calculate the fare: fare = 1 + distance, there is a minimum fare of 5 euros
    * The first `Passenger` in the `passengers` list is responsible to pay for the ride. If this `Passenger` does not have enough money to cover the fare, raise a `RuntimeError`.
    * This responsible `Passenger` is deducted money equal to the fare.
    * All `Passenger`s in the `passengers` list should be registered as riding in this `Taxi`.
* Create a method `dropoff()` to let the passengers out of the taxi at their destination.
  * There should be no more passengers in the `Taxi`.
  * The `Taxi` should become available for the next group of passengers.
  * If there are no current passengers, no action is required.


### `Bus`

A `Bus` inherits from `Vehicle`.

* Define a constructor for `Bus`.
  * It has two parameters: `license plate` and `amount_of_seats` inherited from `Vehicle`.
* Implement `maximum_occupants`: for a bus, `maximum_occupants = 2 * amount_of_seats`.
* Create a method `board(passenger)` to allow a passenger to enter the bus:
  * If adding one passenger would exceed the maximum number of riders, raise a `RuntimeError`.
  * The fare is 2 euros for all passengers.
  * If the `Passenger` does not have enough money to cover the fare, raise a `RuntimeError`.
  * Otherwise, the fare should be deducted from the `Passenger`'s money.
  * The `Passenger` should be registered in the `occupants` dictionary.
* Create a method `disembark(passenger)` to allow a passenger to leave the bus:
  * The `Passenger` should be removed from the `occupants` dictionary if they are riding the bus.

## Example usage

```python
# create some passengers
>>> aimee = Passenger("12.34.56-789.01", "Aimee Backiel", 40)
>>> bastian = Passenger("01.02.03-040.05", "Bastian Li Backiel", 5)

# create some vehicles
>>> my_taxi = Taxi("1-NGL-760", 4)
>>> my_bus = Bus("1-HUE-344", 30)


# taking a bus ride together; Bastian likes to pay for himself
>>> my_bus.board(aimee)
>>> my_bus.board(bastian)

# check the occupants of the bus
>>> my_bus.occupant_names
["Aimee Backiel", "Bastian Li Backiel"]

# they get off at the zoo
>>> my_bus.disembark(aimee)
>>> my_bus.disembark(bastian)

# check the occupants again
>>> my_bus.occupant_names
[]

# Bastian wants to take the bus alone for the first time, and Aimee follows him in a taxi
# they only ride 5 km to be sure he doesn't get lost
>>> my_bus.board(bastian)
>>> my_taxi.pickup([aimee],5)

# check the occupants in each vehicle
>>> my_bus.occupant_names
["Bastian Li Backiel"]
>>> my_taxi.occupant_names
["Aimee Backiel"]

# check how much money remains in their wallets
>>> aimee.money
32
>>> bastian.money
1
```

# Testing

You must write tests which sufficiently test the property `maximum_occupants`. Include these tests in the `test-transport.py` file.

* Refer to the description of both `Taxi` and `Bus` for information about how to implement `maximum_occupants`.
* Use the conventions you learned in the Testing chapter to be able to test this functionality.