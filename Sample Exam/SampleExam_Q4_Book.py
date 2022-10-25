class Book:
    def __init__(self, title, price):
        self._title = title
        self._price = price

    def print_details(self):
        print(self._title + " costs €" + str(self._price))

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price
