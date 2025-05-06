from student import Student
from instructor import Instructor
from teaching_assistant import TeachingAssistant
from course import Course

def main():
    # Create students and instructors
    alice = Student("Alice Smith", "alice@example.com")
    bob = Student("Bob Jones", "bob@example.com")
    dr_brown = Instructor("Dr. Brown", "brown@example.edu")

    # Create courses
    cs101 = Course.create_lecture_course("Intro to CS", "CS101")
    cs102 = Course.create_lab_course("Advanced Python", "CS102")

    # Assign instructor
    dr_brown.add_course(cs101)

    # Enroll students
    alice.enroll(cs101)
    alice.enroll(cs102)
    bob.enroll(cs101)

    # Create and assign TA
    ta = TeachingAssistant("Charlie TA", "charlie@university.edu")
    ta.enroll(cs101)
    ta.add_course(cs102)

    print("Alice's courses:")
    for course in alice:
        print(f" - {course.name}")

    print("\nStudents in CS101:")
    for student in cs101:
        print(f" - {student.name}")

    print("\nCombined courses of Alice and Bob:")
    for course in alice + bob:
        print(f" - {course.name}")

if __name__ == "__main__":
    main()
