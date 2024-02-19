# CONSTRUCTORS (OR INITIALIZERS)

It's quite rare in the real world to see a class that defines properties in the way we've been doing it.

```python
class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2
```

It's much more practical to use a `constructor`. In Python, the constructor is the `__init__()` method, and it is called when a new object is created.

So, with a constructor, the code would look like this.

```python
class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2
```

However, because the constructor is a method, we can now make the name, starting armor and number of weapons configurable with some parameters.

```python
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
# prints "Legolas"
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"
```

# Task

Add a constructor to our `Wall` class. It should take `depth`, `height` and `width` as parameters, in that order, and set them as properties. It should also compute an additional property called `volume`. Volume is the width times height times depth.