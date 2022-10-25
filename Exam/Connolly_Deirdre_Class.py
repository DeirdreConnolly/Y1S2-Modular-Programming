# Name:         Deirdre Connolly
# Student ID:   R00112962


class Musician:
    def __init__(self, first_name, instrument, grade):
        self._first_name = first_name
        self._instrument = instrument
        self._grade = int(grade)

    def set_grade(self, grade):
        self._grade = int(grade)

    def get_grade(self):
        return self._grade

    def set_details(self, first_name, instrument):
        self._first_name = first_name
        self._instrument = instrument

    def get_details(self):
        return self._first_name, self._instrument

    def print_details(self):
        print("Name: " + self._first_name)
