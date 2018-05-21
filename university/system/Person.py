class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.get_address

    def to_string(self):
        return "Name: {}\nAddress: {}".format(self.name, self.address.to_string())
