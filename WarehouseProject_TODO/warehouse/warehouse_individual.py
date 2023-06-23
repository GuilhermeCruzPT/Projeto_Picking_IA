from ga.individual_int_vector import IntVectorIndividual

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO

    def compute_fitness(self) -> float:
        # TODO (rever)
        # fitness = biggest path covered by a forklift
        path, fitness = self.obtain_all_path()
        self.fitness = fitness
        return self.fitness

    def obtain_all_path(self):
        # TODO (rever)
        maximum_distance = 0
        full_path = []
        separator_indexes = [-1]

        # store separator indexes
        for i in range(len(self.genome)):
            if self.genome[i] > len(self.problem.products):
                separator_indexes.append(i)
        separator_indexes.append(len(self.genome))

        for i in range(len(self.problem.forklifts)):
            current_distance = 0
            current_path = []

            if separator_indexes[i + 1] - separator_indexes[
                i] > 1:  # there is at least one product assigned to the forklift i
                # calculate path between forklift and the first product
                cell1 = self.problem.forklifts[i]
                cell2 = self.problem.products[self.genome[separator_indexes[i] + 1] - 1]
                pair, inverted = self.get_pair(cell1, cell2)
                current_distance += pair.value
                if inverted:
                    for cell in reversed(pair.path):
                        current_path.append(cell)
                else:
                    for cell in pair.path:
                        current_path.append(cell)

                # calculate path between the following products
                for j in range(separator_indexes[i] + 1, separator_indexes[i + 1] - 1):
                    cell1 = self.problem.products[self.genome[j] - 1]
                    cell2 = self.problem.products[self.genome[j + 1] - 1]
                    pair, inverted = self.get_pair(cell1, cell2)
                    current_distance += pair.value
                    current_path.pop()
                    if inverted:
                        for cell in reversed(pair.path):
                            current_path.append(cell)
                    else:
                        for cell in pair.path:
                            current_path.append(cell)

                # calculate path between the last product and the exit
                cell1 = self.problem.products[self.genome[separator_indexes[i + 1] - 1] - 1]
                cell2 = self.problem.agent_search.exit
                pair, inverted = self.get_pair(cell1, cell2)
                current_distance += pair.value
                current_path.pop()
                if inverted:
                    for cell in reversed(pair.path):
                        current_path.append(cell)
                else:
                    for cell in pair.path:
                        current_path.append(cell)

            # compare current distance to maximum distance found
            if current_distance > maximum_distance:
                maximum_distance = current_distance

            full_path.append(current_path)

        return full_path, maximum_distance

    def get_pair(self, cell1, cell2):
        for pair in self.problem.agent_search.pairs:
            if pair.cell1 == cell1 and pair.cell2 == cell2:
                return pair, False
            if pair.cell1 == cell2 and pair.cell2 == cell1:
                return pair, True
        return None

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance