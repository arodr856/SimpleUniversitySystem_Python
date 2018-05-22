from university.system.Person import Person
from university.system.Address import Address
from university.system.Student import Student
from university.system.Course import Course


def main():
    address = Address(13069, 'Mineola St.', 'Arleta', 'CA', 91331)
    student = Student('Alex Rodriguez', address, '303601563')
    course1 = Course('cs-2013', 3)
    course2 = Course('cs-3337', 3)
    student.add_course(course1)
    student.add_course(course2)

    courses = student.get_courses()
    student.remove_course('cs-3337')
    for course in courses:
        print(course.get_name())


main()

