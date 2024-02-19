# ENCAPSULATION IN PYTHON
Python is a very dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards. That's why encapsulation in Python is achieved mostly by [convention](https://en.wikipedia.org/wiki/Coding_conventions) rather than by force.

Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff. If a developer wanted to break convention, there are ways to get around the double underscore rule.

```python
class Wall:
    def __init__(self, height):
        # this warns developers to not
        # access the `__height` property directly
        self.__height = height

    def get_height(self):
        return self.__height

```


Python `can not` enforce encapsulation by fully preventing developers from touching private class members