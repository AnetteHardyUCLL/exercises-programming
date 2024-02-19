# Queue

## Concepts Used

* Classes
* Access control

## Some Explanation

Imagine you go to your favorite sandwich shop (which of course is 't Smullerke).
Sadly it's around noon, so the there's a long queue of two dozen people.
Oh well, at least there's five people working in parallel, so the wait is bearable.

Let us focus on this queue thing, what exactly is it?
Well, it's kind of a "list" of people.
When someone wants to buy a sandwich, that person must take place at the very end of the queue.

When a worker is ready, he or she will serve the next customer in the queue.
That person is the one in the front of the queue.

So, in essence:

* Adding a customer to the queue = adding them at the *end* of the list
* Retrieving a customer from the queue = removing them from the *beginning* of the list

## Task

We want to implement queues in Python.

* Create a class `Queue`.
* Its constructor takes no parameters.
  A new queue is initially empty.
* Add a method `add(self, item)` to add an item to the queue.
* Add a method `next(self)` that removes and returns the next item from the queue.
* Add a method `is_empty(self)` that checks if the queue is empty.

It is important that `add` and `next` behave as described above:

```python
# Create an empty queue
queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie') # And Charlie as third

queue.next()   # Alice arrived first, so she's the first to be served next
queue.next()   # This must return Bob
queue.next()   # Finally, it's Charlie's turn
```

Internally, the `Queue` object will rely on a `list` to keep track of all the customers, let's call it `items`.
However, this `list` must remain hidden, otherwise some malicious person could cut in line.

```python
# Mallory inserts herself at the beginning of the queue instead of at the end
queue.items.insert(0, "Mallory")
# Many frowns ensue
```

In other words, the `items` must be made private.

## Conclusion

A `list` is a general purpose data structure that allows you to access any item you want, and add or remove items anywhere you want.
A `Queue` is a more limited list, one that enforces a "queueing discipline": only add at the end, only remove at the beginning.
Therefore, it needs to hide the list it internally uses for storage so as to prevent abuse.

In general, objects will often hide their internal state (i.e., its attributes) to prevent outsiders from tinkering directly with it.
An attribute can be public if it can take any value, but as soon as you want to limit what can be done with it, you should make it private and only allow access to it indirectly using methods.

A few examples:

* A `Point` class that represents a point with `x`, `y` coordinates does not need to hide its attributes: `x` and `y` are free to have any value they want.
* A `Person` class might want to restrict its `age` to positive values.
  The `age` should then be stored in a private attribute and setting the field should be done using a method (or better, a property) which checks that the new value is indeed positive.
