class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_information(self, new_name=None, new_age=None, new_address=None):
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        if new_address:
            self.address = new_address

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

person1 = Person("John Doe", 25, "123 Main St")
person1.display_information()

person1.update_information(new_name="Jane Doe", new_age=26, new_address="456 Oak St")

person1.display_information()
