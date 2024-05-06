# Static Methods

A class is typically described as a blueprint for objects.
Another way of looking at it is to see a class as a factory of objects.
As far as you know, there's very little you can do with the class itself, except for asking it to create an object.

```python
class Plumbus:
    def schleem(self):
        ...

# Invalid
Plumbus.schleem()

# Valid
plumbus = Plumbus()    # Create an object
plumbus.schleem()      # Now we can call the shleem method
```

The syntax for defining classes is perhaps a bit misleading: it seems to imply that members are part of the class, while in fact they are members of _objects_ of that class.
However, it is indeed possible to attach methods to the class itself instead of to its objects:

```python
class Plumbus:
    def schleem(self):
        # ...

    @staticmethod
    def fleeb():     # No self parameter!
        # ...
```

Here, `fleeb` is a _static method_ (do **not** call it a class method, that's something different).
We can now write the following code:

```python
Plumbus.fleeb()
```

As you can see, we call `fleeb` directly on the class instead of creating an object first.
Also notice that `fleeb` is missing the `self` parameter: `self` is meant to refer to the object a method is called on, but in this case, there is no object, so having a `self` parameter would make no sense.

## Usage: Factory Functions

So, what good are these static methods?
How useful are they?

Well, they're definitely used way less than regular methods.
But they do have a purpose.
You can see them as regular functions (i.e., functions outside of a class) that conceptually belong to a class: placing them inside the class makes this relation clear.

Consider the following class:

```python
class Distance:
    def __init__(self, size):
        self.size = size

distance = Distance(10)
```

Here, we created a `Distance` object of size 10.
But 10 what?
10 meters?
10 miles?
10 lightyears?
We don't know: it's not clear from the code.

We can make it a bit clearer:

```python
class Distance:
    def __init__(self, size_in_meters):
        self.size_in_meters = size_in_meters

distance = Distance(10)
```

If you just see the last line, again, it's not clear what unit of distance is used.
We could make it explicit as follows:

```python
distance = Distance(size_in_meters=10)
```

However, mentioning the parameter name is optional.
We can force the user to mention it using [keyword-only arguments](https://peps.python.org/pep-3102/):

```python
class Distance:
    def __init__(self, *, size_in_meters):
        self.size_in_meters = size_in_meters

distance = Distance(10)                  # Error
distance = Distance(size_in_meters=10)   # Valid
```

But what if we want to express our distance in a different unit, like miles?
It would make sense that we have some helper functions for this.

```python
def meters(amount):
    return Distance(size_in_meters=amount)

def millimeters(amount):
    return Distance(size_in_meters=amount / 1000)

def miles(amount):
    return Distance(size_in_meters=amount * 1609.34)

# and so on
```

Since their only purpose is to _create_ objects, such functions are also _factory functions_.
This is a perfectly valid approach: code creating distance will be clear since the unit is always mentioned explicitly.
It can, however, be helpful to bundle these functions together.
And this is where static methods come into play:

```python
class Distance:
    def __init__(self, *, size_in_meters):
        self.size_in_meters = size_in_meters

    @staticmethod
    def meters(amount):
        return Distance(size_in_meters=amount)

    @staticmethod
    def millimeters(amount):
        return Distance(size_in_meters=amount / 1000)

    @staticmethod
    def miles(amount):
        return Distance(size_in_meters=amount * 1609.34)

    # ...
```

Creating a distance can now be written as

```python
distance = Distance.miles(5)
```

## Task

Create a class `Duration` that can be used as follows:

```python
>>> duration = Duration.from_seconds(60)
>>> duration.seconds
60

>>> duration.minutes
1

>>> duration = Duration.from_hours(1)
>>> duration.minutes
60

>>> duration.seconds
3600
```

We want the following members:

* Static factory methods named `from_seconds`, `from_minutes` and `from_hours`.
* Readonly properties named `seconds`, `minutes` and `hours`.

Note: the reason we named the factory functions `from_unit()` instead of just `unit()` is that we wanted to be able to name our properties after the units.
Sadly, we cannot have static methods and properties with the same name inside one class.
