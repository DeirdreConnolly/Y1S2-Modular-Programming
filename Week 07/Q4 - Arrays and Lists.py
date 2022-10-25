# For when the text is in two separate lines/arrays


def main():
    file = open("Fruit.txt")
    fruit = []
    stock = []
    while True:
        line = file.readline().rstrip()
        if line == "":
            break
        fruit.append(line)
        line = file.readline().rstrip()
        stock.append(int(line))
    file.close()
    print(fruit)
    print(stock)

main()