# CLASSES

A class is a special type of value in an object-oriented programming language like Python. Just like a string, integer or float, a class is essentially a custom type that has some special properties.

An object is an instance of a class type. In this example, health is an instance of an integer type.

```python
health = 50
```

In `object-oriented programming`, we create special types called "classes". And each instance of a class is called an "object".

## HOW DO I CREATE A CLASS?

In Python, you just need to use the `class` keyword, and you can set custom properties in the following way. It is a common convention in Python to capitalize the first character in the name of your class.

```python
class Soldier:
    health = 5
```

Then to create an instance of a `Soldier` we simply call the class. Notice that a class isn't a function. It doesn't take input parameters directly.

```python
first_soldier = Soldier()
print(first_soldier.health)
# prints "5"

```

# Task

Create a class called `Wall` on line 1. It should have a property called `armor` that is initialized to `10` and a `height` that starts at `5`.
