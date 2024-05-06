# Assignment

Say we have written the following class.

```python
class Person:
    def __init__(self, age):
        self.age = age
```

This class is used throughout our codebase, many times over.
However, there's a problem with it: `age` can take any value you want.
Somewhere, we made a mistake and in certain cases the `age` becomes negative.
This causes a lot of problems.

The problem with public attributes is that they're rather... dumb.
It's just a simple memory location that can be overwritten at whim.
We somehow want to make it smarter somehow, so that it can disallow negative values.

Enter properties.
Properties allow us to make "intelligent attributes".
In essence, there's two things we can do with attributes: we can read their value, and we can overwrite their value.
Properties make it possible for us to define what exactly should happen when someone tries to read or write it.
In the case of our `age`, properties allow us to prevent anyone from writing a negative value to it.

The nice thing about properties is that they obey the "Uniform Access Principle".
This simply means that the code used to read/write attributes is exactly the same as the code used to read/write properties.

```python
# In case age is a simple attribute
print(person.age)
person.age = 5

# In case age is a smart property
print(person.age)
person.age = 5
```

See! No difference at all.
This is great news: we can promote our dumb `age` attribute to a smart `age` property without having to change any of the client code!
This actually is a very important rule in software development: we want to be able to make local changes (upgrading `age`) without having it global ramifications.

## Readonly Properties

Let's start with a very basic application of properties.
Say we want to have an attribute/property, but we don't want to allow it to be changed:

```python
print(person.age)   # Should be allowed
person.age = 10     # Should raise an error
```

How do we go about it?
First of all, we still need a place to store the actual age.
For this, an attribute is inevitable.
Luckily, as we discussed previously, we can hide this attribute.

```python
class Person:
    def __init__(self, age):
        self.__age = age
```

Okay, we store our age in the private `__age` attribute.
Now we want the user to be able to query a `person`'s `age` using the syntax `person.age`.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
```

Here, we have defined the property named `age`.
It looks like a regular method, except for the fact that it has `@property` added just in front of it.
This is a *decorator*, and you can do all kinds of fancy stuff with it, but that's not important for now.

So, what does this `@property` decorator do?
It tells Python that whenever the user tries to read from `age`, that it should call that method.
Because of this, it is also called a *getter method*.
In our example, the `age` getter method simply returns the value hidden in the private `__age` attribute.

Right now, we can write

```python
>>> person = Person(18)

>>> print(person.age)
18
```

The method can actually do whatever it wants.
Say we change it to

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        print("Reading age!")
        return self.__age
```

Then reading the `person`'s `age` will also cause a message to be printed:

```text
>>> person = Person(18)

>>> print(person.age)
Reading age!
18
```

So, we can now *read* the `age`.
But can we write to it?

```text
>>> person = Person(18)

>>> person.age = 10
AttributeError: can't set attribute
```

Yay.
This is exactly what we want.

The reason we can't write is that we only defined a *getter* method.
We didn't define a *setter* method.
We'll show you how to do that in a later exercise.
For now, try to contain your excitement.

## Task

Define a class `MusicalNote`.
It must have two readonly properties: `name` and `pitch`.

```text
>>> note = MusicalNote('a4', 440)

>>> note.name
a4

>>> note.pitch
440

>>> note.name = 'b4'
AttributeError: can't set attribute

>>> note.pitch = 450
AttributeError: can't set attribute
```
