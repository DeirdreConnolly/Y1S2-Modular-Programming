class Animal:   # capital letter when naming a class
    def __init__(self, name, type, age):
        self._name = name
        self._type = type
        self._age = age

    def print_details(self):
        print(self._name + " is a " + self._type + " age " + str(self._age))

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age
