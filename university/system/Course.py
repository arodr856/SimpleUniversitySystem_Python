class Course:

    def __init__(self, course_initials, units):
        self.course_initials = course_initials
        self.units = units

    def get_name(self):
        return self.course_initials
