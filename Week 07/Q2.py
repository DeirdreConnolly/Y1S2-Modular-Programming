def main():
    file = open("Fruit2.txt")
    fruit = []
    while True:
        line = file.readline().rstrip().upper()
        if line == "":
            break
        fruit.sort()
        fruit.append(line)
    file.close()
    print(", ".join(fruit))

main()


def g_words():
    fruit_file = open("Fruit2.txt", "r")
    fruit_list = fruit_file.readlines()
    g_words = []
    for fruit in fruit_list:
        if fruit.startswith("g"):
            g_words.append(fruit)
    g_words2 = [item.rstrip().upper() for item in g_words]
    print(", ".join (g_words2))

g_words()