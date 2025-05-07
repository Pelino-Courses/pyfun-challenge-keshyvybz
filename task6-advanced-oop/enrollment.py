from student import Student
from course import Course

class Enrollment:
    def __init__(self, student: Student, course: Course):
        if not isinstance(student, Student) or not isinstance(course, Course):
            raise TypeError("Enrollment requires a Student and a Course.")
        self.student = student
        self.course = course
