from typing import List, Iterator
from enrollment import Enrollment
from person import NonEmptyString

class Course:
    name = NonEmptyString("name")
    code = NonEmptyString("code")

    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code
        self._enrollments: List[Enrollment] = []

    def add_enrollment(self, enrollment: Enrollment):
        self._enrollments.append(enrollment)

    def __iter__(self) -> Iterator:
        return (en.student for en in self._enrollments)

    @classmethod
    def create_lab_course(cls, name: str, code: str):
        return LabCourse(name, code)

    @classmethod
    def create_lecture_course(cls, name: str, code: str):
        return LectureCourse(name, code)

class LabCourse(Course):
    def __init__(self, name: str, code: str):
        super().__init__(name, code)
        self.lab_required = True

class LectureCourse(Course):
    def __init__(self, name: str, code: str):
        super().__init__(name, code)
        self.lab_required = False
