# Operator Overloading

As you know, classes can have different kinds of members: attributes, methods and properties.
Accessing any one of these members is always done using the same "dot notation":

```python
some_object.attribute   # Accessing an attribute
some_object.method()    # Invoking a method
some_object.property    # Accessing a property
```

However, there are also other kinds of interactions possible.
For example, you can add things together using the operator `+`:

```python
5 + 3             # Adding numbers
"a" + "b"         # Adding strings
[1, 2] + [3, 4]   # Adding lists
```

However, if we use `+` on one of our objects:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


>>> p = Point(1, 2)
>>> q = Point(3, 4)
>>> p + q
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

As you can see, this gives an error.
This makes sense: why would Python know how you mean to add two points together?

Let's add a regular method `add` that defines how this addition must take place:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

This allows us to write

```python
>>> p = Point(1, 2)
>>> q = Point(3, 4)
>>> p.add(q)
Point(4, 6)
```

This is great, but we'd really like to write `p + q` instead of `p.add(q)`.
Luckily, it is simple to make this happen:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

We try once again:

```python
>>> p = Point(1, 2)
>>> q = Point(3, 4)
>>> p + q
Point(4, 6)
```

When Python sees code like `obj1 + obj2`, it will automatically transform this into `obj1.__add__(obj2)` for you.
So, in essence, there's nothing new really: you simply have to know how to name the method: in the case of `+` we must name the method `__add__`.

There are many other operators, e.g., `-`, `*`, `/`, `%`, etc.
Each of them have a [corresponding method](https://docs.python.org/3/reference/datamodel.html):

|Operator|Method|
|-|-|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `//` | `__floordiv__` |
| `%` | `__mod__` |
| `**` | `__pow__` |

As you might have noticed, these methods share a pattern: they're all enclosed by two underscores (`__`).
For this reason, they're often called [dunder methods](https://wiki.python.org/moin/DunderAlias).

Notice that these methods should always return a _new_ object and not modify `self`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Correct implementation
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    # Wrong implementation, never do this!
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
```

## Task

Create a class `Money` that represents a certain `amount` of money in a certain `currency`:

```python
>>> money = Money(10, "EUR")
>>> money.amount
10

>>> money.currency
"EUR"
```

We want to be able to add `Money`s together, but only if their currencies match.

```python
>>> Money(10, "EUR") + Money(20, "EUR")
Money(30, "EUR")

>>> Money(10, "EUR") + Money(20, "USD")
RuntimeError("Mismatched currencies!")
```

Same for subtraction:

```python
>>> Money(30, "EUR") - Money(10, "EUR")
Money(20, "EUR")

>>> Money(30, "EUR") - Money(10, "USD")
RuntimeError("Mismatched currencies!")
```

Finally, we also want to be able to multiply a `Money` with a number.
Notice that we are *not* multiplying two `Money`s together, but a `Money` with an `int` or `float`.

```python
>>> Money(20, "EUR") * 5
Money(100, "EUR")
```
