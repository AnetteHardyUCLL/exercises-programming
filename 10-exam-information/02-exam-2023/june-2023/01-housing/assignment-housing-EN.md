# Exam Question 1: Housing

* Place all code for this exercise in `housing.py`.
* In these instructions we will always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure to get the names exactly right, even those of the parameters.
* You have received a `basic_test_housing.py` file which contains basic testing, like if certain classes exist and if you've used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_test_housing.py
    ``` 

  * A missing class will cause tests focusing on that class to be skipped.
    Skipped tests therefore still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests means that your code is definitely incomplete or incorrect.
    But passing tests do not mean that your code is fully correct!
* You must also create some of your own tests in the `test-housing.py` file.
  * Any tests you must write yourself are indicated in this assignment file.
  * You may add additional tests here if you want to check your code more thoroughly. Only those asked for in the assignment will be graded.
  * This test file must be able to run correctly to earn credit.

## Person

* Define a class `Person`.
* Define a static method `is_valid_name(name)` that returns `True` if `name` is valid and `False` otherwise.
  * A name must consist of at least two parts separated by a space.
  * Examples: "Harry Styles" and "Machine Gun Kelly" are valid names, but "Rihanna" is not.
* Define `Person`'s constructor.
  * The constructor takes three parameters: `id` (a string), `name` (a string) and `is_a_student` (a boolean).
  * The constructor should raise a `ValueError` if the name is invalid.
* Store `id` and `is_a_student` in public fields and `name` in a private field.
* Make `name` available via a property.
  * Define a getter and a setter.
  * If the name is invalid, the setter should raise a `ValueError`.

## Residence

A `Residence` represents a place where a person or people can live. There are multiple types of residences but all residences share some common members. Therefore we will create an abstract class `Residence` to store common features of different residence types.

* Define an abstract class `Residence`.
* Define a constructor for `Residence`.
  * It has three parameters: `address` (a string), `area` (a float, measured in square meters), and `number_of_rooms` (an integer).
  * Store these in *public* fields.
  * Add another *private* field `occupants` to store a dictionary of all the `Person`s registered at this `Residence`. <br>
      This dictionary will use `Person` ids as keys and `Person` objects as values.
  * Upon creation, a `Residence` has no people registered as living there.
* Define a read-only property `number_of_occupants` which returns the number of `Person`s registered at this `Residence`.
* Define a read-only property `maximum_occupants`.
  * The maximum number of occupants in a `Residence` is determined by law. To avoid overcomplicating the calculation on this exam, we've simplified the rules, as shown here:
    * Each `Person` requires at least 20 square meters of space.
    * Each room can accommodate up to 2 people.
* Define a method `register_resident(person)` which adds a `Person` to the dictionary of people registered at this `Residence`.
  * If the person is already registered at this `Residence`, nothing should happen.
  * If there is not enough room for another `Person` to legally register at this `Residence`, raise a `RuntimeError`.
  * If there is enough room for another `Person`, add this `Person` to the dictionary of people registered at this `Residence`. Use the `id` of the `Person` as the key and the `Person` object as the value.
* Define a method `unregister_resident(id)` which removes a `Person` from the dictionary of people registered at this `Residence`.
* Define a property `resident_names` which returns a list of the names (strings) of all the people registered at this `Residence`.
  * Use what you learned about functional programming to generate this list.
* Define an abstract method `calculate_value()`.
  * This method takes no parameters.

## Types of Residences

As previously stated, there are different kinds of residences: villas, row houses, apartments, and student kots.
Common functionality was already implemented in `Residence`. Below we will define two such subclasses to differentiate between different types of residences. To keep this exam from becoming too long, we will only implement `Villa` and `StudentKot`.

### `Villa`

A `Villa` has inherits from `Residence`.
Aside from address, area, and number_of_rooms (inherited from `Residence`), a `Villa` can also have a garage.

* Define a constructor for `Villa`.
  * It has four parameters: three from `Residence`'s constructor and `garage_capacity` (an integer).
  * Store `garage_capacity` in a public field.
* Implement `calculate_value`. The value of a `Villa` is calculated in the following way:
  * villa_value = (25000 * number_of_rooms) + (2100 * area) + (10000 * garage_capacity)

### `StudentKot`

An `StudentKot` inherits from `Residence`.
A student kot has an address and area, but the number_of_rooms is always 1.

* Define a constructor for `StudentKot`.
  * It has two parameters: `address` and `area` from `Residence`. The `number_of_rooms` is always 1.
* Add an extra constraint to the inherited method `register_resident(person)`.
  * A `Person` must be a student in order to register in a `StudentKot`. If a `Person` who is not a student tries to register in a `StudentKot`, raise a `RuntimeError`.
* The value of a `StudentKot` is calculated in the following way:
  * kot_value = 150000 + (750 * area)

## Example usage

```python
# create some people
>>> aimee = Person("12.34.56-789.01","Aimee Backiel",False)
>>> bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# create some residences
>>> my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
>>> my_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)

# check the values of the properties
>>> my_villa.calculate_value()
427100

>>> my_kot.calculate_value()
165000

# move the people into a residence
>>> my_villa.register_resident(aimee)
>>> my_villa.register_resident(bastian)

# check the residents of the villa
>>> my_villa.resident_names
["Aimee Backiel","Bastian Li Backiel"]

# Someday, sadly Bastian will grow up and move into his student kot
>>> my_villa.unregister_resident(bastian.id)
>>> my_kot.register_resident(bastian)

# check the residents again
>>> my_villa.resident_names
["Aimee Backiel"]

>>> my_kot.resident_names
["Bastian Li Backiel"]

# With all her free time, Aimee can expand the garage to make space for all her hobbies
>>> my_villa.garage_capacity = 3
>>> my_villa.calculate_value()
447100
```

# Testing

You must write tests which sufficiently test the property `maximum_occupants`. Include these tests in the `test-housing.py` file.

This information is copied from the `Residence` class and additional clarification is provided for your convenience:
* Define a read-only property `maximum_occupants`.
  * The maximum number of occupants in a `Residence` is determined by law. To avoid overcomplicating the calculation on this exam, we've simplified the rules, as shown here:
    * Each `Person` requires at least 20 square meters of space.
    * Each room can accommodate up to 2 people.
* These rules must be combined. So a `Residence` with 72 square meters and 3 rooms can only fit 3 people (the smaller of the two calculations above).
  * Other examples:
    * A small studio with only 1 room and 30 square meters can have 1 person living in it.
    * A slightly larger studio with 1 room and 40 square meters can have 2 people.
    * An apartment with 3 rooms and 200 square meters can accommodate up to 6 people.
* Use the conventions you learned in the Testing chapter to be able to test this functionality.