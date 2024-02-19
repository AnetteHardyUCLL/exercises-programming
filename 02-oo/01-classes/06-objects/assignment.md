# MULTIPLE OBJECTS

If a class is just a type, then an object is just a value.

You'll hear often that an object is an "instance" of a class. Let's look at what that word means.

```
In object-oriented programming, an instance is a concrete occurrence of any object... "Instance" is synonymous with "object" as they are each a particular value... "Instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.
-- Wikipedia
```

So for our wall class, I can create three different "instances" of the class. Or in other words, I'll create three separate objects.

```python
wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)
```

In the example above, `Wall` and `Integer` are types, and each variable is an instance of one of those types.

# Task

Take a look at the `Brawler` class and the `fight` function provided. In the `main` function, create 4 new brawlers with the following stats:

- Name: Aragorn. Speed: 4. Strength: 4.
- Name: Gimli. Speed: 2. Strength: 7.
- Name: Legolas. Speed: 7. Strength: 7.
- Name: Frodo. Speed: 3. Strength: 2.
Then call fight twice. The first fight should be Aragorn vs Gimli. The second will be Legolas vs Frodo.