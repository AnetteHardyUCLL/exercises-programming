# Recursion

A recursive function is a function defined in terms of itself via self-referential expressions.

This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result. All recursive functions share a common structure made up of two parts: base case and recursive case.

To demonstrate this structure, let’s write a recursive function for calculating n!:

```python
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
```

```python
>>> factorial_recursive(5)
120
```

Behind the scenes, each recursive call adds a stack frame (containing its execution context) to the call stack until we reach the base case.


# Task

Implement a recursive method `fibonacci(number)` that returns the number-th fibonacci number
calculates (see https://nl.wikipedia.org/wiki/Rij_van_Fibonacci). Presumably
you will find a simple and short version that is, however, very inefficient. Can you explain why?

## Example
fibonacci(0) --> 0  

fibonacci(3) --> 2  

fibonacci(-5) --> 0  

