# CLASS VARIABLES VS INSTANCE

## VARIABLES
So far we've worked with both class variables and instance variables, but we haven't talked about the difference yet. Below are 2 code samples that demonstrate the variable height being declared as an instance variable, and a class variable.

## INSTANCE VARIABLES
Instance variables vary from object to object and are declared in the constructor.

```python
class Wall:
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20 # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"
```

## CLASS VARIABLES
Class variables remain the same between instances of the same class and are declared at the top level of a class definition.

```python
class Wall:
    height = 10

south_wall = Wall()
print(south_wall.height)
# prints "10"

Wall.height = 20 # updates all instances of a Wall

print(south_wall.height)
# prints "20"
```

## WHICH SHOULD I USE?
Generally speaking, stay away from class variables. Just like global variables, class variables are usually a bad idea because they make it hard to keep track of which parts of your program are making data updates. However, it is important to understand how they work because you may see them out in the wild.

## ASSIGNMENT
Due to our terrible class design, some lazy code owned by a different development team is causing some bugs in our class. We can fix it by using instance variables instead of class variables.

In the `main()` function (that our team isn't responsible for), a line like `Dragon.element = "fire"` should not affect our existing dragon instances! We don't like near-global variables. We want our users to specify each dragon's element in the constructor.

Update the `Dragon` class. Remove the `element` class variable and instead use an instance variable that's configurable via the constructor.