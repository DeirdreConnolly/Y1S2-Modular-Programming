def get_data():
    infile = open("countries.txt", 'r')
    names = []
    population = []
    while True:
        line = infile.readline().rstrip()
        if line == "":
            break
        line = line.split()
        names.append(line[0])
        population.append(line[1])
    return population, names


def display_details(countries, populations):
    for i in range(len(countries)):
        print(countries[i], " has a population of ", populations[i], "m.", sep="")


def main():
    country_populations, country_names = get_data()
    display_details(country_names, country_populations)


main()

