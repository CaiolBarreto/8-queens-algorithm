import random
from utils import binary_to_integer


class DNA:
    def __init__(self, chromosome, max_fitness):
        self.chromosome = chromosome
        self.max_fitness = max_fitness

    def fitness(self):
        horizontal_collisions = (
            sum([self.chromosome.count(queen) - 1 for queen in self.chromosome]) / 2
        )

        diagonal_collisions = 0

        size = len(self.chromosome)
        left_diagonal = [0] * (2 * size - 1)
        right_diagonal = [0] * (2 * size - 1)
        for index in range(size):
            current_gene = binary_to_integer(self.chromosome[index])
            left_diagonal[index + current_gene - 1] += 1
            right_diagonal[len(self.chromosome) - index + current_gene - 2] += 1

        diagonal_collisions = 0

        for index in range(2 * size - 1):
            counter = 0
            if left_diagonal[index] > 1:
                counter += left_diagonal[index] - 1
            if right_diagonal[index] > 1:
                counter += right_diagonal[index] - 1
            diagonal_collisions += counter

        return int(self.max_fitness - (horizontal_collisions + diagonal_collisions))

    def mutate(self):
        size = len(self.chromosome)
        mutation_indices = random.sample(
            range(size), 2
        )  # Select two distinct indices for gene swapping

        # Swap genes
        self.chromosome[mutation_indices[0]], self.chromosome[mutation_indices[1]] = (
            self.chromosome[mutation_indices[1]],
            self.chromosome[mutation_indices[0]],
        )

        return self
