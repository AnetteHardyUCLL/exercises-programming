# Circular Buffer

We want to create a special kind of list, namely one that only keeps track of the N most recently added elements.
An example will make this clearer:

```python
# We are only interested in the last 3 items
>>> buffer = CircularBuffer(3)

# Initially the buffer is empty
>>> len(buffer)
0

# Let's add a few items
>>> buffer.add('a')
>>> buffer.add('b')
>>> buffer.add('c')
>>> len(buffer)
3

# We want to be able to read the elements
>>> buffer[0]
'a'
>>> buffer[1]
'b'
>>> buffer[3]
'c'

# Now watch what happens when we add a fourth element!
>>> buffer.add('d')
>>> len(buffer)
3
>>> [buffer[0], buffer[1], buffer[2]]
['b', 'c', 'd']
```

As you can see, when we added the fourth item `d`, we went over the maximum size of `3`, so the "oldest" element was removed, i.e., `'a'`.
Let's add a fifth element:

```python
>>> buffer.add('e')
>>> len(buffer)
3
>>> [buffer[0], buffer[1], buffer[2]]
['c', 'd', 'e']
```

## Length

Given a `CircularBuffer` object, it can be useful to be able to ask for its size, i.e., how many items it contains.
We could simply define a method:

```python
class CircularBuffer:
    def size(self):
        # ...
```

However, Python would prefer you to stick to the standard way of doing things, namely using `len()`.
You should already know `len` from other data structures:

```python
# len works on lists
>>> len([1, 2, 3])
3

# and on strings
>>> len("abcd")
4

# and on sets
>>> len({1, 2, 3, 4, 5})
5
```

How do we make `len` understand our `CircularBuffer`?
Very simple: `len(obj)` will actually call `obj.__len__()` behind the scenes.
So, for example,

```python
class CircularBuffer:
    def __len__(self):
        return 10

>>> buffer = CircularBuffer(3)
>>> len(buffer)
10
```

## Indexing

You should also be familiar with indexing using the `[]` operator:

```python
# Indexing arrays
>>> [1, 2, 3, 4][0]
1

# Indexing strings
>>> 'abcd'[1]
'b'
```

You can have your own classes respond to `[]` by defining the `__getitem__` dunder method:

```python
class CircularBuffer:
    def __getitem__(self, index):
        # ...
```

## Task

Implement the `CircularBuffer` class as described above.

* `CircularBuffer(n)` should create a `CircularBuffer` object with maximum size `n`.
* `buffer.add(item)` adds an extra item to the buffer. If the maximum size is reached, the oldest element is removed.
* `buffer[index]` returns the `index`th item in the buffer.
* `len(buffer)` returns the number of items in the buffer. This can never be greater than `n`.
