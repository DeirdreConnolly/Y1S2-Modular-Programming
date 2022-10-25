# Name:         Deirdre Connolly
# Student ID:   R00112962


from Connolly_Deirdre_Class import Musician

def main():
    musician1 = Musician("Susan", "piano", "0")

    musicians = [musician1]
    for item in musicians:
        item.print_details()

    musician1.set_grade(5)
    grade = musician1.get_grade()
    print("Grade: " + str(grade))

main()