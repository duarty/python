class Costumers:
    def __init__(self, name, age):
        self.name =  name;
        self.age = age;
        self.address = []

    def insert_address(self, city, state):
        self.address.append(Address(city, state));


    def show_address(self):
        for aaddress in self.address:
            print(aaddress.city, aaddress.state);




class Address:
    def __init__(self, city, state):
        self.city = city;
        self.state = state;