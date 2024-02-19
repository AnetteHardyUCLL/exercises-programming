# INHERITANCE
We've made it to the Holy-grail of object-oriented programming: inheritance. Inheritance is the defining trait of object-oriented languages. Non-OOP languages like Go and Rust provide encapsulation and abstraction features as almost every language does. Inheritance on the other hand tends to be unique to class-based languages like Python, Java, and Ruby.

## WHAT IS INHERITANCE?
Inheritance allows one class (aka "the child class") to inherit the properties and methods of another class (aka "the parent class").

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

## SYNTAX
In Python, one class can inherit from another using the following syntax.

```python
class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"
```
To use the constructor of the parent class, we can use Python's built-in `super()` method.

```python
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)
```

## ASSIGNMENT
In Age of Dragons, all the archers in the game are humans, though not all humans are necessarily archers. The thing all humans have in common is that they need a name, so the `Human` class has taken care of the naming logic.

Now we need to write an `Archer` class. Archers are humans, and therefore need a name, but we don't want to re-write all that code! Let's just inherit the `Human` class!

Complete the `Archer` class. It should inherit from its parent. In its constructor it should call its parent's constructor, then also set its unique `__num_arrows` property.
