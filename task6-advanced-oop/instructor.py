from person import Person
from typing import List
from course import Course

class Instructor(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self._courses_taught: List[Course] = []

    def add_course(self, course: Course):
        self._courses_taught.append(course)

    def get_role(self) -> str:
        return "Instructor"
