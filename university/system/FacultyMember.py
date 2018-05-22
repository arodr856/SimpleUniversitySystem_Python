from university.system.Person import Person


class FacultyMember(Person):

    def __init__(self, name, address, id):
        super().__init__(name, address)
        self.employee_id = id
        self.courses = []

