# Inheritance

## Duplication in Functions

Say you have the following two functions:

```python
def smallest_sum(ns):
    sums = (
        x + y
        for x in ns
        for y in ns
    )
    return min(sums)


def greatest_sum(ns):
    sums = (
        x + y
        for x in ns
        for y in ns
    )
    return max(sums)
```

As you can see, they both compute the same `sums`.
Generally, you should really avoid duplication.
Shared code should be factored out as follows:

```python
def compute_sums(ns):
    return (
        x + y
        for x in ns
        for y in ns
    )


def smallest_sum(ns):
    return min(compute_sums(ns))


def greatest_sum(ns):
    return max(compute_sums(ns))
```

## Duplication in Classes

Duplication can also occur on the level of classes.
To demonstrate this, let's implement a (very small) part of a chess game.

You are given a file `startercode.py`.
Take a good look at the code inside.
Let's briefly discuss the three classes inside.

### `Position`

`Position` is a class that represents, well, positions.
Nothing special about it, really.

### `Pawn`

`Pawn` objects have a `position` and `color`.

* The `pawn.position` is only valid if it refers to a position on the chessboard (chessboards are 8&times;8 grids).
  The logic for checking resides in `is_valid_position`.
* `pawn.color` can only have one of two values: `black` or `white`, as is verified in `is_valid_color`.
* `pawn.is_legal_move(new_position)` checks if the `pawn` can move from its current position to `new_position`.
  The details behind the logic are not very important.
* `pawn.move(new_position)` moves the `pawn` to `new_position` on condition that it represents a legal move as determined by `is_legal_move`.

### `King`

You will notice that `King` is very similar to `Pawn`.
There's really only one difference, namely the logic in `is_legal_move`.
All the rest is identical.

## Factoring Out the Common Code

As mentioned before, `Pawn` and `King` have a lot of code in common.
However, duplication is generally a Very Bad Thing: it just adds more opportunities for bugs to arise.
The more code you write, the higher the odds you make a mistake.

So, let's try to get rid of all duplicated code.

* Start by copying all starter code to your own `student.py` file.
* Run the tests.
  They should all pass, because all functionality is implemented correctly.
* Create a new class `ChessPiece`.
* Move all members `Pawn` and `King` have identical implementations for to `ChessPiece`.
* Only one method should remain in `Pawn` and `King`, namely their specialized implementation for `is_legal_move`.

Restructuring code like this is called [refactoring](https://en.wikipedia.org/wiki/Code_refactoring): it is the process of modifying code _without changing its behavior_.
Remember this word as you will hear it often.

Now we need a way to say that `Pawn` and `King` must "import" all members defined in `ChessPiece`.
The actual term used in Python is _inherit_: `Pawn` and `King` must _inherit_ members from `ChessPiece`.
For this reason, `ChessPiece` is often called the _parent class_ (or base class).
`Pawn` and `King` are _child classes_ of `ChessPiece`.

How do we tell Python about this relationship?
Very simple:

```python
class ChessPiece:
    # ...

class Pawn(ChessPiece):
    # ...

class King(ChessPiece):
    # ...
```

In essence, this means that `Pawn` "copies" all members of `ChessPiece` and then adds its own extra members.
Idem for `King`.

Run the tests.
They should all pass.

## Refactoring

Refactoring is a very common process and its importance cannot be overstated.
As explained before, the goal is to perform _structural_ changes, not _behavioral_ ones.

In order to safely refactoring, you will typically start off with tests.
Tests check behavior, they "pin" it down as it were.
Next, you perform a small modification (refactoring) to your code, after which you run the tests again.
They should all keep passing.
If they don't, you accidentally broke something and you'll need to fix it.
You repeat this process of making small changes and running the tests until your code is cleaned up.

Few students like this refactoring process because they're already content that their code works.
However, building on top of badly structured code is a risky endeavor:

* the complexity of your code grows quickly and soon enough you won't understand it more: it works seemingly by magic but you don't want to touch it out of fear to break something
* bugs tend to appear out of nowhere and are very hard to locate
* your progress slows down to a crawl

This is known as [technical debt](https://en.wikipedia.org/wiki/Technical_debt) and it has been the downfall of many.
