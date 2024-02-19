class Employee:
    company_name = "Dev.boot"
    total_employees = 0

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary

        Employee.total_employees += 1

    def get_name(self):
        return f"{self.first_name} {self.last_name}"
