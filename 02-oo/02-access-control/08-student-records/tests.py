from student import Student

def test_student_initialization():
    student = Student("John")
    assert student.name == "John"
    assert student._Student__courses == {}  # Verify that the courses attribute is initialized as an empty dictionary

def test_student_calculate_letter_grade():
    student = Student("John")
    assert student.calculate_letter_grade(95) == "A"
    assert student.calculate_letter_grade(85) == "B"
    assert student.calculate_letter_grade(75) == "C"
    assert student.calculate_letter_grade(65) == "D"
    assert student.calculate_letter_grade(55) == "F"

def test_student_add_course():
    student = Student("John")
    student.add_course("Math", 92)
    student.add_course("Science", 85)
    student.add_course("History", 75)

    # Verify that courses are added correctly
    assert student.get_courses() == {"Math": "A", "Science": "B", "History": "C"}

# Run the tests
if __name__ == "__main__":
    test_student_initialization()
    test_student_calculate_letter_grade()
    test_student_add_course()
