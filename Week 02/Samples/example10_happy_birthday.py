def sing(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear", name)
    print("Happy Birthday to you!")
    name = "Mickey Mouse"


def main():
    childs_name = input("What is the child's name?")
    sing(childs_name)
    # lest there be any doubt, childs_name has not become "Mickey Mouse"!
    print(childs_name)

main()

