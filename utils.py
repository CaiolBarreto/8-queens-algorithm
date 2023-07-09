class ParentsSelection:
    TOURNAMENT = 1
    ROULETTE = 2

class SurvivorChoice:
    SUBSTITUTE_WORSE = 1
    GENERACIONAL = 2

# prints given chromosome
def print_chromosome(dna):
    integer_chromosome_array = [binary_to_integer(gene) for gene in dna.chromosome]
    print(
        "Chromosome = {},  Fitness = {}".format(
            str(integer_chromosome_array), dna.fitness()
        )
    )


# prints given chromosome board
def print_board(chromosome, number_of_queens):
    board = []

    for _ in range(number_of_queens):
        board.append(["x"] * number_of_queens)

    for index in range(number_of_queens):
        current_gene = binary_to_integer(chromosome[index])
        board[current_gene][index] = "Q"

    for row in board:
        print(" ".join(row))

    print()


# prints each generation and the max fitness of it
def print_generation(generation, population):
    print("=== Generation {} ===".format(generation))
    print("Maximum Fitness = {}".format(max([DNA.fitness() for DNA in population])))


# transform a binary number to integer
def binary_to_integer(number):
    return int(number, 2)


# transform a integer number to binary
def integer_to_binary(number):
    return bin(number)
