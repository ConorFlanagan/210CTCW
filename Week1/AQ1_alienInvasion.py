def alienInvasion(x,y,n):
    population = []
    eggs = []
    for i in range(0,n):
        if i<y:
            population.append(1)
            eggs.append(x)
        else:
            population.append(population[i-1]+eggs[i-1])
            eggs.append(population[i])
        print(population[i])
    print("Population after " + str(n) + " days: ")
    print(population[i])

alienInvasion(3,5,30)
