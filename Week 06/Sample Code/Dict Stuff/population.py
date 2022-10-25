#  Desc: loading items into a list from a file
#
#
def  main():
    infile = open("population.txt", 'r')
    population = infile.readlines();
    i = 0
    while i < len(population):
        #print(population[i])
        population[i] = population[i].rstrip("\n")
        i = i + 1

    print(population)


main()

