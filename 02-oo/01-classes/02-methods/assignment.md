# METHODS

After the last exercise, you might be wondering why classes are useful, they seem like `dictionaries` but worse!

What makes classes cool is that they allow us to define custom `methods` on them. A method is a function that is associated with a class, and it has access to all the properties of the object.

```python
class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"
```

## THE SPECIAL "SELF" VALUE


As you can see, methods are nested within the class declaration. Methods always take a special parameter as their first argument called `self`. The self variable is a reference to the object itself, so by using it you can read and update the properties of the object.

Notice that methods are called directly on an object using the dot operator.

```python
object.method()
```

# Task

Add a `fortify()` method to your wall class. It should double the current `armor` property.

