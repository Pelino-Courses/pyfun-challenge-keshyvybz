from person import Person
from typing import Iterator, List
from enrollment import Enrollment
from course import Course

class Student(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self._enrollments: List[Enrollment] = []

    def enroll(self, course: Course):
        enrollment = Enrollment(self, course)
        self._enrollments.append(enrollment)
        course.add_enrollment(enrollment)

    def __iter__(self) -> Iterator[Course]:
        return (en.course for en in self._enrollments)

    def __add__(self, other: "Student") -> List[Course]:
        return list(set(self) | set(other))

    def get_role(self) -> str:
        return "Student"
