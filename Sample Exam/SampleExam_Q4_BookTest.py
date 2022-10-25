from SampleExam_Q4_Book import Book

def display():
    book1 = Book("HP1", 10)
    book2 = Book("HP2", 20)
    book3 = Book("HP3", 30)
    # book1.print_details()
    # book2.print_details()
    # book3.print_details()

    my_books = [book1, book2, book3]
    for item in my_books:
        item.print_details()


display()