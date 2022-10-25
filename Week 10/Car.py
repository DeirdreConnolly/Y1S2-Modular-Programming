class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def print_details(self):
        print(self._make + self._model + self._year)

