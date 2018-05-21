class Address:

    def __init__(self, street_number, street_name, city, state, zip_code):
        self.street_number = street_number
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_street_number(self):
        return self.street_number

    def get_street_name(self):
        return self.street_name

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def set_street_number(self, street_number):
        self.street_number = street_number

    def set_street_name(self, street_name):
        self.street_name = street_name

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def to_string(self):
        return "{} {} {} {} {}".format(self.street_number, self.street_name, self.city,self.state, self.zip_code)