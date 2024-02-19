# EMPLOYEE MANAGEMENT
You've recently been hired to work at a new startup, Dev.boot! The company has yet to implement any system for tracking employees within the company. Your manager has assigned you the task!

## CHALLENGE
Unfortunately, Dev.boot engineers kinda suck. Rather than creating a `Company` class that uses instance variables to track employees, they've decided to use an `Employee` class that uses class variables to track employees.

It's not the cleanest implementation, but you're stuck with it. Hey, at least you get to practice using class variables!

## CLASS VARIABLES
Initialize the following class variables:

1. `company_name` set to `"Dev.boot"`.
2. `total_employees` set to `0`.

## CONSTRUCTOR
The constructor should take the following parameters (in order) and set them to the corresponding instance variables:

1. `first_name` = `first_name`
2. `last_name` = `last_name`
3. `id` = `id`
4. `position` = `position`
5. `salary` = `salary`

Also, it should increment the `total_employees` class variable each time a new Employee is created. Remember, `total_employees` is a class variable, not an instance variable.

## GETTER
Add a `get_name` method that returns the employee's full name as a string (e.g. "John Doe").