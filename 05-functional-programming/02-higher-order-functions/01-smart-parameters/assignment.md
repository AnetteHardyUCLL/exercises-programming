# Smart Parameters

Say we're working on our `Movie`s and we want to determine how many movies a certain director has made.
We can then write the following code:

```python
len([movie for movie in movies if movie.director == 'Steven Spielberg'])
```

For some reason, we need this in multiple places.
We build a function around it so we don't need to repeat this code:

```python
def count_movies_by_spielberg(movies):
    return len([movie for movie in movies if movie.director == 'Steven Spielberg'])
```

Now, hard coding values like this is a bit of a [code smell](https://en.wikipedia.org/wiki/Code_smell).
Let's first put the string in a separate variable:

```python
def count_movies_by_spielberg(movies):
    director = 'Steven Spielberg'
    return len([movie for movie in movies if movie.director == director])
```

And now we can turn this very specific function into a more generalized one by promoting the `director` variable to a parameter:

```python
def count_movies_by_director(movies, director):
    return len([movie for movie in movies if movie.director == director])
```

This is much better: it still allows us to count movies made by Spielberg, but also by any other director.

But what if we want to count movies with a certain actor in it?
We can easily write a new function:

```python
def count_movies_with_actor(movies, actor):
    return len([movie for movie in movies if actor in movie.actors])
```

Oh no, now we want to count the number of movies made in a certain year:

```python
def count_movies_in_year(movies, year):
    return len([movie for movie in movies if movie.year == year])
```

Or movies made during a certain time period:

```python
def count_movies_between_years(movies, min_year, max_year):
    return len([movie for movie in movies if min_year <= movie.year <= max_year])
```

You see where this is going: these functions have a lot in common, and that counts as duplication.
And that's a bit of a problem.
Let's see how we can solve this.

## Generalizing `count_movies_by_spielberg`

Let's go back to our `count_movies_by_spielberg` function.

```python
def count_movies_by_spielberg(movies):
    return len([movie for movie in movies if movie.director == 'Steven Spielberg'])
```

It is identical to all other functions except for the condition in the `if`.
Let's move this condition in a separate function.

```python
def is_made_by_right_director(movie):
    return movie.director == 'Steven Spielberg'


def count_movies_by_spielberg(movies):
    return len([movie for movie in movies if is_made_by_right_director(movie)])
```

Remember what we did when we generalized `count_movies_by_spielberg` to `count_movies_by_director`?
This is very similar: instead of introducing a new variable (`director`) we put the entire condition in a separate function `is_made_by_right_director`.
Now we can perform the same trick and turn it into a _parameter_:

```python
def count_movies_by_director(movies, is_made_by_right_director):
    return len([movie for movie in movies if is_made_by_right_director(movie)])
```

This will work: functions are values just like integers, booleans, list, etc. so there's no reason to believe we cannot pass them as arguments.

## Generalizing `count`

Let's see how we can use `count_movies_by_director`:

```python
def is_made_by_spielberg(movie):
    return movie.director == "Steven Spielberg"

def is_made_by_scorsese(movie):
    return movie.director == "Martin Scorsese"


>>> count_movies_by_director(movies, is_made_by_spielberg)
>>> count_movies_by_director(movies, is_made_by_scorsese)
```

This is not very impressive: we could do that before too.
But if you look at `count_movies_by_director`'s implementation, there's nothing specific about _directors_.
The function is not restricted to only considering a movie's director.

```python
def has_tom_cruise_as_actor(movie):
    return 'Tom Cruise' in movie.actors

>>> count_movies_by_director(movies, has_tom_cruise_as_actor)
```

This would actually work and return the number of movies with Tom Cruise in it.
The name of the function, `count_movies_by_director`, is quite misleading really: it can actually be used with _any_ condition.
Let's rename it:

```python
def count_movies(movies, should_be_counted):
    return len([movie for movie in movies if should_be_counted(movie)])
```

This function `count_movies` can replace all the functions we discussed above.
For example,

```python
def is_from_eighties(movie):
    return 1980 <= movie.year < 1990

>>> count_movies(movies, is_from_eighties)
```

## Higher Order Functions

`count_movies` takes a function as parameter.
Functions receiving functions are called _higher order functions_.

We can further generalize `count_movies`: nowhere does it "know" its first parameter is a list of `Movie`s.
It could be a list of `Person`s, strings, numbers, etc.

```python
def count(xs, should_be_counted):
    return len([x for x in xs if should_be_counted(x)])
```

Now we have a single `count` function that can count any kind of objects based on any condition.
This would not have been possible without using function arguments.

This kind of generalization is very important.
When writing code, you should always watch out for arbitrary limitations and see if introducing parameters can make it more generally usable.

## Task

Let's have you write some higher order functions.
We start off simple:

```python
def say_hello():
    print("Hello!")

>>> repeat(say_hello, 5)
Hello!
Hello!
Hello!
Hello!
Hello!
```

Write a function `repeat(function, n)` that simply calls `function` `n` times.
You can assume `function` takes no arguments and returns nothing useful.
