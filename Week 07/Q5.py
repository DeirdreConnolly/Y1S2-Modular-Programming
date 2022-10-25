# For when the text is in the same line

def main():
    file = open("Passwords.txt")
    username_list = []
    password_list = []
    while True:
        line = file.readline()
        if line == "":
            break
        line_list = line.split()
        username_list.append(line_list[0])
        password_list.append(line_list[1])
    file.close()
    print(username_list)
    print(password_list)

    username = input("Username: ")
    password = input("Password: ")

    username_position = username_list.index(username)
    password_position = password_list.index(password)

    if username_position == password_position:
        print("Welcome!")
    else:
        print("Incorrect username or password. Please try again.")

main()



