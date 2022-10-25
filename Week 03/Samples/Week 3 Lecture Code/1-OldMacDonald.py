def verse(animal, sound):
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print("And on the farm he had a", animal)
    print("E-I-E-I-O")
    print("With a", sound, sound,'here')
    print("And a", sound, sound, 'there')
    print("Here a", sound)
    print("There a", sound)
    print("Everywhere a", sound, sound)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")


def main():
    verse("Oink", "Pig")
    verse("Pig", "Oink")
    verse("Cow", "Moo")
    verse("Duck", "Quack")

main()