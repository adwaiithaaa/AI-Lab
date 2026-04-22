import random

dist = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

cities = list(range(8))

def cost(path):

    total = 0

    for i in range(len(path)-1):
        total += dist[path[i]][path[i+1]]

    total += dist[path[-1]][path[0]]

    return total


def create_population(size):

    population = []

    for _ in range(size):
        p = cities.copy()
        random.shuffle(p)
        population.append(p)

    return population

def single_crossover(p1,p2):

    point = random.randint(1,len(p1)-2)

    child = p1[:point]

    for city in p2:
        if city not in child:
            child.append(city)

    return child


def two_point_crossover(p1,p2):

    a = random.randint(1,len(p1)-3)
    b = random.randint(a+1,len(p1)-2)

    child = [None]*len(p1)

    child[a:b] = p1[a:b]

    pos = 0

    for city in p2:
        if city not in child:
            while child[pos] != None:
                pos += 1
            child[pos] = city

    return child

def mutate(path):

    i,j = random.sample(range(len(path)),2)

    path[i],path[j] = path[j],path[i]

    return path


def genetic(crossover_type):

    population = create_population(20)

    for generation in range(200):

        population.sort(key=cost)

        new_population = population[:5]

        while len(new_population) < 20:

            p1,p2 = random.sample(population[:10],2)

            if crossover_type == 1:
                child = single_crossover(p1,p2)
            else:
                child = two_point_crossover(p1,p2)

            if random.random() < 0.2:
                child = mutate(child)

            new_population.append(child)

        population = new_population

    best = min(population,key=cost)

    return best,cost(best)


print("Single Point Crossover")
path,c = genetic(1)
print(path,c)

print("\nTwo Point Crossover")
path,c = genetic(2)
print(path,c)