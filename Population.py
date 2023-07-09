import random
from DNA import DNA
from utils import integer_to_binary, ParentsSelection


class Population:
    def __init__(self, population_size, parents_pool_size, max_fitness, parents_selection):
        self.population = []
        self.population_size = population_size
        self.parents_pool_size = parents_pool_size
        self.max_fitness = max_fitness
        self.parents_selection = parents_selection

    def crossover(self, first_parent, second_parent):
        first_chromosome = first_parent.chromosome
        second_chromosome = second_parent.chromosome

        size = len(first_chromosome)

        # Cut-and-crossfill crossover
        cut_point = random.randint(1, size - 2)
        child = first_chromosome[:cut_point]

        for gene in second_chromosome[cut_point:]:
            child.append(gene)

        return DNA(child, self.max_fitness)

    def create_population(self, number_of_queens):
        self.population = [
            self.__create_chromosome(number_of_queens)
            for _ in range(self.population_size)
        ]

    def __create_chromosome(self, number_of_queens):
        chromosome = [
            integer_to_binary(random.randint(0, number_of_queens - 1))
            for _ in range(number_of_queens)
        ]
        return DNA(chromosome, self.max_fitness)

    def choose_parents(self):
        if self.parents_selection == ParentsSelection.TOURNAMENT:
            parent_pool = random.sample(self.population, self.parents_pool_size)

            # Sort the parent pool based on fitness level
            parent_pool.sort(key=lambda dna: dna.fitness(), reverse=True)

            # Select the best 2 parents from the parent pool
            return parent_pool[0], parent_pool[1]

        else:
            fitness_sum = sum(dna.fitness() for dna in self.population)
            roulette_wheel = []
            cumulative_fitness = 0.0

            for dna in self.population:
                fitness_ratio = dna.fitness() / fitness_sum
                cumulative_fitness += fitness_ratio
                roulette_wheel.append((cumulative_fitness, dna))

            parent_pool = []
            for _ in range(2):  # Select 2 parents
                spin = random.random()
                for cumulative_fitness, dna in roulette_wheel:
                    if spin <= cumulative_fitness:
                        parent_pool.append(dna)
                        break
            

            return parent_pool[0], parent_pool[1]



