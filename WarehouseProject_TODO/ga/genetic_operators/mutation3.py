from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

from WarehouseProject_TODO.ga.genetic_algorithm import GeneticAlgorithm


class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO (rever)
        # Scramble Mutation
        num_genes = ind.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        while cut1 == cut2:
            cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        if cut1 > cut2:
            cut1, cut2 = cut2, cut1

        subset = ind.genome[cut1:cut2]
        GeneticAlgorithm.rand.shuffle(subset)

        ind.genome[cut1:cut2] = subset

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
