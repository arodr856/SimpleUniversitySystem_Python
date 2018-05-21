from university.system.Person import Person
from university.system.Address import Address
from university.system.Student import Student


def main():
    address = Address(13069, 'Mineola St.', 'Arleta', 'CA', 91331)
    person = Person('Alex Rodriguez', address)
    student = Student('Alex Rodriguez', address, '303601563')
    print(student.to_string())


main()

