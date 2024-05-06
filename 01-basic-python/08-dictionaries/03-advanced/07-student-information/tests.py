import pytest
from pytest import approx
import student
import solution


testdata = [
    {
        'John Smith': {
            'age': 18,
            'courses': ['Math']
        },
    },
    {
        'John Smith': {
            'age': 18,
            'courses': ['Chemistry']
        },
        'Jane Doe': {
            'age': 18,
            'courses': ['Biology']
        },
    },
    {
        'John Smith': {
            'age': 18,
            'courses': ['Math', 'French']
        },
        'Jane Doe': {
            'age': 19,
            'courses': ['Latin', 'Greek']
        },
    },
    {
        'John Smith': {
            'age': 20,
            'courses': ['Economics', 'Geography', 'History']
        },
        'Jane Doe': {
            'age': 18,
            'courses': ['German', 'Math', 'Biology', 'History']
        },
    },
    {
        'John Smith': {
            'age': 20,
            'courses': ['Math', 'Latin', 'Physics']
        },
        'Jane Doe': {
            'age': 18,
            'courses': ['Math', 'Latin', 'Physics']
        },
        'Alan Smithee': {
            'age': 22,
            'courses': ['Math', 'Latin', 'Physics']
        },
    },
    {
        'John Smith': {
            'age': 20,
            'courses': ['Math', 'Latin', 'Physics']
        },
        'Jane Doe': {
            'age': 18,
            'courses': ['Math', 'German', 'Physics', 'Biology']
        },
        'Alan Smithee': {
            'age': 29,
            'courses': ['Math', 'Latin', 'Economics']
        },
    },
]

@pytest.mark.parametrize("data", [
    [],
    ['John Smith,20'],
    ['John Smith,20,Math'],
    ['John Smith,20,Math,Physics'],
    ['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math']
])
def test_process_data(data):
    function_name = 'process_data'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(data)
    expected = solution_function(data)

    assert expected == actual, f"Wrong result for {(data)}, expected {expected}, received {actual}"


@pytest.mark.parametrize("dictionary", testdata)
def test_average_age(dictionary):
    function_name = 'average_age'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary)
    expected = solution_function(dictionary)

    assert expected == approx(actual), f"Wrong result for {(dictionary)}, expected {expected}, received {actual}"


@pytest.mark.parametrize("dictionary", testdata)
def test_courses(dictionary):
    function_name = 'courses'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary)
    expected = solution_function(dictionary)

    assert expected == actual, f"Wrong result for {(dictionary)}, expected {expected}, received {actual}"


@pytest.mark.parametrize("dictionary", testdata)
def test_most_common_courses(dictionary):
    function_name = 'most_common_courses'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary)
    expected = solution_function(dictionary)

    assert expected == actual, f"Wrong result for {(dictionary)}, expected {expected}, received {actual}"
