from operator import indexOf
from Population import Population
from utils import *
import random
import numpy


class Main:
    def __init__(
        self,
        population_size=100,
        mutation_probability=0.4,
        recombination_probability=0.9,
        offspring_size=2,
        parents_pool_size=5,
        number_of_queens=8,
    ):
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.recombination_probability = recombination_probability
        self.offspring_size = offspring_size
        self.parents_pool_size = parents_pool_size
        self.number_of_queens = number_of_queens
        self.max_fitness = (number_of_queens * (number_of_queens - 1)) / 2  # 8*7/2 = 28

        self.population_object = Population(
            population_size, parents_pool_size, self.max_fitness
        )

    # Genetic algorithm
    def genetic_queen(self):
        new_population = []

        for _ in range(len(self.population_object.population) - 2):
            parent_1, parent_2 = self.population_object.choose_parents()

            # Recombination
            if random.random() < self.recombination_probability:
                for child in range(self.offspring_size):
                    child = self.population_object.crossover(parent_1, parent_2)

                    # Mutations
                    if random.random() < self.mutation_probability:
                        child = child.mutate()

                    new_population.append(child)

                    if child.fitness() == self.max_fitness:
                        break
            else:
                for parent in [parent_1, parent_2]:
                    if random.random() < self.mutation_probability:
                        parent = parent.mutate()

                    new_population.append(parent)

        new_population.sort(key=lambda dna: dna.fitness(), reverse=True)

        # Substitute worse
        new_population = new_population[: len(self.population_object.population)]

        return new_population

    def run(self):
        self.population_object.create_population(self.number_of_queens)
        result_converged = 0

        generation = 1

        while (
            not self.max_fitness
            in [DNA.fitness() for DNA in self.population_object.population]
            and generation < 10000
        ):
            self.population_object.population = self.genetic_queen()

            if generation % 10 == 0:
                print_generation(generation, self.population_object.population)
            generation += 1

        fitness_of_dna = [DNA.fitness() for DNA in self.population_object.population]

        best_dna = self.population_object.population[
            indexOf(fitness_of_dna, max(fitness_of_dna))
        ]

        best_dna_fitness = best_dna.fitness()

        if self.max_fitness in fitness_of_dna:
            print("\nSolved in Generation {}!".format(generation - 1))

            print_chromosome(best_dna)
            print_board(best_dna.chromosome, self.number_of_queens)

            result_converged += 1

        else:
            print(
                "\nUnfortunately, we could't find the answer until generation {}. The best answer that the algorithm found was:".format(
                    generation
                )
            )
            print_board(best_dna.chromosome, self.number_of_queens)

        return best_dna_fitness, result_converged
