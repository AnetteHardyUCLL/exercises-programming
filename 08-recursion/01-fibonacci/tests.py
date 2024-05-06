from student import fibonacci

def test_fibonacci_base_cases():
    assert fibonacci(0) == 0, "The 0th Fibonacci number should be 0"
    assert fibonacci(1) == 1, "The 1st Fibonacci number should be 1"

def test_fibonacci_recursive_cases():
    assert fibonacci(2) == 1, "The 2nd Fibonacci number should be 1"
    assert fibonacci(3) == 2, "The 3rd Fibonacci number should be 2"
    assert fibonacci(4) == 3, "The 4th Fibonacci number should be 3"
    assert fibonacci(5) == 5, "The 5th Fibonacci number should be 5"
    assert fibonacci(6) == 8, "The 6th Fibonacci number should be 8"
    assert fibonacci(7) == 13, "The 7th Fibonacci number should be 13"

def test_fibonacci_negative_input():
    assert fibonacci(-1) == 0, "Negative indices should return 0"
    assert fibonacci(-10) == 0, "Negative indices should return 0"

def test_fibonacci_large_input():
    assert fibonacci(20) == 6765, "Test with a larger input to check function efficiency"
