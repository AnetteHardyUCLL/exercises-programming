# Assignment

Let's delve a little further in what we can do with properties.
Say we have our `Person` class, and we want a person to have an age.

```python
class Person:
    def __init__(self, age):
        self.age = age
```

Now, we don't want this age to be directly modifiable, so we hide it and make a readonly property.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
```

We need this age to be accurate: once a year it should go up by one.
We make a method for this.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    def increment_age(self):
        self.__age += 1
```

Of course, we need to know on what day we need to increment a person's age, meaning we need to store their birthday.

```python
class Person:
    def __init__(self, age, birthday):
        self.__age = age
        self.__birthday = birthday

    @property
    def age(self):
        return self.__age

    @property
    def birthday(self):
        return self.__birthday

    def increment_age(self):
        self.__age += 1
```

This is a bit weird.
Say we have a long list of `Person` objects, then we would need to check if it's their birthday every day:

```python
def process_birthdays(people):
    today = find_out_todays_date()
    for person in people:
        if person.birthday == today:
            person.increment_age()
```

We're not particularly fond of this solution.
One big issue with it is that it suffers from redundancy: the same information is stored twice.
The age can be derived from a person's birthday, meaning there's no need to store both the age and birthday.
The birthday only should suffice.

We want to get rid of the `__age` attribute.
However, we still want to be able to use `person.age` to determine the `person`'s age.

```python
class Person:
    def __init__(self, birthday):
        self.__birthday = birthday

    @property
    def age(self):
        ???

    @property
    def birthday(self):
        return self.__birthday
```

`age` can be computed: we know the `person`'s birthday (it's stored in `__birthday`) and we can find out what the current date is.

```python
class Person:
    def __init__(self, birthday):
        self.__birthday = birthday

    @property
    def age(self):
        today = find_out_todays_date()
        difference = today - self.__birthday
        return difference.years

    @property
    def birthday(self):
        return self.__birthday
```

Using this code, the `age` will be computed based on the birthday, which is why it's also called a *computed attribute*.
It looks like an attribute, but it's not really stored anywhere.
Whenever you read it, its value is computed and returned.
By implementing `age` this way, there is no redundancy.

Redundancy is always a tricky thing.
If we were to store both the birthday and the age, we could end up with inconsistent data:

```python
# Say we are in 2023
person = Person(age=18, birthday=Date(day=18, month=12, year=1980))
```

Clearly, this is incorrect: the person should be 42, not 18.
By removing redundancy, such errors cannot occur: the age will always be consistent with the birthday.

## Task

Write a class `BMICalculator` that we can use as follows:

```text
>>> calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)

>>> calc.bmi
24.69

>>> calc.category
normal
```

The bmi is computed as follows:

```python
bmi = weight_in_kg / height_in_m**2
```

The category can take one of three values:

* `"underweight"` if `bmi` is less than `18.5`.
* `"normal"` if `bmi` is between `18.5` and `25`.
* `"overweight"` if `bmi` is greater than `25`.
