# Assignment

## `process_data`

Create a function `process_data(string_data)` that transforms a list of strings into a dictionary.

The input list has the following format:

```python
['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math']
```

It must be transformed into

```python
{
        'John Smith': {
            'age': 20,
            'courses': ['Math', 'Physics']
        },
        'Jane Doe': {
            'age': 21,
            'courses': ['Biology', 'Chemistry', 'Math']
        }
    }
```


## `average_age`

Create a function `average_age(data)` that calculates the average age of the students in the input dictionary.
The parameter `data` is a dictionary with the same structure as what `process_data` returns.

## `courses`

Create a function `courses(data)` that returns a collection of all the courses taken by the students in the input dictionary.
Return them as a set.

The parameter `data` is a dictionary with the same structure as what `process_data` returns.

## `most_common_courses`

Create a function `most_common_courses(data)` that returns the set of courses that is taken by the most number of students.
The parameter `data` is a dictionary with the same structure as what `process_data` returns.
For example, say `Math` is taken by 5 students, `Spanish` by 3, and `Biology` by 5, the function should return `{'Math', 'Biology'}`.
