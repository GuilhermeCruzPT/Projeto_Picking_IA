from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

from WarehouseProject_TODO.ga.genetic_algorithm import GeneticAlgorithm


class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO (rever)
        # Swap Mutation
        num_genes = ind.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        while cut1 == cut2:
            cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        aux = ind.genome[cut1]
        ind.genome[cut1] = ind.genome[cut2]
        ind.genome[cut2] = aux

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
