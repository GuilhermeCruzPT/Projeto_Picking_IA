from ga.individual_int_vector import IntVectorIndividual

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO

    def compute_fitness(self) -> float:
        # TODO (rever)
        # fitness = biggest path covered by a forklift
        self.fitness = 0
        separator_indexes = [-1]

        # store separator indexes
        for i in range(len(self.genome)):
            if self.genome[i] > len(self.problem.products):
                separator_indexes.append(i)
        separator_indexes.append(len(self.genome))

        for i in range(len(self.problem.forklifts)):
            current_distance = 0
            if separator_indexes[i + 1] - separator_indexes[
                i] > 1:  # there is at least one product assigned to the forklift i
                # calculate distance between forklift and the first product
                cell1 = self.problem.forklifts[i]
                cell2 = self.problem.products[self.genome[separator_indexes[i] + 1] - 1]
                current_distance += self.get_pair_value(cell1, cell2)

                # calculate distance between the following products
                for j in range(separator_indexes[i] + 1, separator_indexes[i + 1] - 1):
                    cell1 = self.problem.products[self.genome[j] - 1]
                    cell2 = self.problem.products[self.genome[j + 1] - 1]
                    current_distance += self.get_pair_value(cell1, cell2)

                # calculate distance between the last product and the exit
                cell1 = self.problem.products[self.genome[separator_indexes[i + 1] - 1] - 1]
                cell2 = self.problem.agent_search.exit
                current_distance += self.get_pair_value(cell1, cell2)

            # compare current distance to maximum distance found
            if current_distance > self.fitness:
                self.fitness = current_distance

        return self.fitness

    def get_pair_value(self, cell1, cell2):
        for pair in self.problem.agent_search.pairs:
            if (pair.cell1 == cell1 and pair.cell2 == cell2) or (pair.cell1 == cell2 and pair.cell2 == cell1):
                return pair.value
        return None

    def obtain_all_path(self):
        # TODO
        # suponhamos que o número de forklifts é 2 e que o primeiro percorre 10 células, e o segundo percorre 5
        # devolve 2 coisas: lista de cels com o percurso das forklifts, e tamanho do maior percurso
        # na gui o steps será o número de passos do caminho mais longo
        # este método pode também ser usado na fit()
        # return [[Cell(4,0), (4,1), (4,2), (4,3), (3,3), ...], [Cell(4,0), (4,1), (4,2), (4,3)]], 10
        pass

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