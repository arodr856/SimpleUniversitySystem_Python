from university.system.Person import Person


class Student(Person):

    def __init__(self, name, address, cin):

        super().__init__(name, address)
        self.cin = cin
        self.courses = []

    def get_cin(self):
        return self.cin

    def get_courses(self):
        return self.courses

    def to_string(self):
        return "Name: {}\nCIN: {}\nAddress: {}".format(self.name, self.cin, self.address.to_string())

    def add_course(self, course):
        self.courses.append(course)

