import random


class Individual:
    def __init__(self, chromosome=[], diff=0, fitness=0.0):
        self.chromosome = chromosome
        self.diff = diff
        self.fitness = fitness


target_individual = [2, 1, 19, 21, 11, 9]
population = []


def count_fitness(target, ind: Individual):
    diff_sum = 0
    for i in range(len(target)):
        diff_sum = abs(diff_sum + (ind.chromosome[i] - target[i]))
    ind.diff = diff_sum
    ind.fitness = 1 / (1 + diff_sum)
    print(ind.diff, ind.fitness)


def select_one(population_arg):
    maximum = sum([c.fitness for c in population_arg])
    pick = random.uniform(0, maximum)
    current = 0
    for individual in population_arg:
        current += individual.fitness
        if current > pick:
            return individual
    return None


def crossover(individual1: Individual, individual2: Individual):
    intersection = random.uniform(0, len(individual1.chromosome))


def main():
    # initialize
    for i in range(10):
        ind = Individual(random.sample(range(1, 26), len(target_individual)))
        population.append(ind)

    # count fitness
    for i in range(len(population)):
        count_fitness(target_individual, population[i])

    # selection in population amount
    new_population = []
    for i in range(len(population)):
        new_population.append(select_one(population))

    print("\nThe Chosen Ones")
    for i in range(len(new_population)):
        print(new_population[i].diff, new_population[i].fitness)

    for i in range(0, len(new_population) - 1, 2):
        crossover_point = random.uniform(0, 1)
        crossover_prob = random.uniform(0, 1)
        if crossover_point < crossover_prob:
            crossover(new_population[i], new_population[i + 1])


main()