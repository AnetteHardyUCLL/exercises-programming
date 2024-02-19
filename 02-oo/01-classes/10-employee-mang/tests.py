from student import Employee

def test_employee_initialization():
    employee = Employee("John", "Doe", 1234, "Software Engineer", 60000)
    assert employee.first_name == "John"
    assert employee.last_name == "Doe"
    assert employee.id == 1234
    assert employee.position == "Software Engineer"
    assert employee.salary == 60000

def test_employee_total_employees():
    # Ensure total_employees increments correctly
    initial_count = Employee.total_employees
    employee1 = Employee("John", "Doe", 1234, "Software Engineer", 60000)
    assert Employee.total_employees == initial_count + 1

    # Ensure total_employees increments correctly with multiple instances
    employee2 = Employee("Jane", "Doe", 5678, "Project Manager", 80000)
    assert Employee.total_employees == initial_count + 2

def test_employee_get_name():
    employee = Employee("John", "Doe", 1234, "Software Engineer", 60000)
    assert employee.get_name() == "John Doe"

# Run the tests
test_employee_initialization()
test_employee_total_employees()
test_employee_get_name()
