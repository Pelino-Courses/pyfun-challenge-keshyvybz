from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def get_role(self) -> str:
        return "Teaching Assistant"
