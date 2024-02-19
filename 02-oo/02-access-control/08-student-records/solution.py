class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade

    def get_courses(self):
        return self.__courses
