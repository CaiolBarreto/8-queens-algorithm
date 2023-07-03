from operator import indexOf
from Population import Population
from utils import *
import random

class Main:
    def __init__(self, population_object, max_fitness):
        self.population_object = population_object
        self.max_fitness = max_fitness

    # Genetic algorithm
    def genetic_queen(self):
        mutation_probability = 0.4
        recombination_probability = 0.9
        new_population = []

        for _ in range(len(self.population_object.population) - 2):

            parent_1, parent_2 = self.population_object.choose_parents(self.max_fitness)

            # Recombination
            if random.random() < recombination_probability:
                first_child = self.population_object.crossover(parent_1, parent_2)
                second_child = self.population_object.crossover(parent_1, parent_2)
            else:
                first_child = parent_1
                second_child = parent_2

            # Mutations
            if random.random() < mutation_probability:
                first_child = first_child.mutate()

            if random.random() < mutation_probability:
                second_child = second_child.mutate()

            new_population.append(first_child)
            new_population.append(second_child)

            if first_child.fitness(self.max_fitness) == self.max_fitness:
                break

            if second_child.fitness(self.max_fitness) == self.max_fitness:
                break

        new_population.sort(key=lambda dna: dna.fitness(self.max_fitness), reverse=True)

        # Substitute worse
        new_population = new_population[:len(self.population_object.population)]

        return new_population


if __name__ == "__main__":
    POPULATION_SIZE = 100

    while True:
        # say N = 8
        number_of_queens = int(input("Please enter your desired number of queens (0 for exit): "))
        if number_of_queens == 0:
            break

        max_fitness = (number_of_queens * (number_of_queens - 1)) / 2  # 8*7/2 = 28

        population_object = Population(POPULATION_SIZE)
        population_object.create_population(number_of_queens)

        main = Main(population_object, max_fitness)

        generation = 1
        while (
            not max_fitness in [DNA.fitness(max_fitness) for DNA in population_object.population]
            and generation < 10000
        ):

            population_object.population = main.genetic_queen()
            if generation % 10 == 0:
                print_generation(generation, max_fitness, population_object.population)
            generation += 1

        fitness_of_dna = [DNA.fitness(max_fitness) for DNA in population_object.population]

        best_dna = population_object.population[
            indexOf(fitness_of_dna, max(fitness_of_dna))
        ]

        if max_fitness in fitness_of_dna:
            print("\nSolved in Generation {}!".format(generation - 1))

            print_chromosome(best_dna, max_fitness)

            print_board(best_dna.chromosome, number_of_queens)

        else:
            print(
                "\nUnfortunately, we could't find the answer until generation {}. The best answer that the algorithm found was:".format(
                    generation - 1
                )
            )
            print_board(best_dna.chromosome, number_of_queens)