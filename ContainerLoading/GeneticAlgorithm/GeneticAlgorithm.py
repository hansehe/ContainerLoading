import copy
from typing import Tuple

from ContainerLoading.GeneticAlgorithm import PopulationGenerator
from ContainerLoading.GeneticAlgorithm import FitnessCalculation
from ContainerLoading.GeneticAlgorithm import NSGA2
from ContainerLoading.GeneticAlgorithm import OffSpringrecombination
from ContainerLoading.GeneticAlgorithm import OffSpringMutation
from ContainerLoading.GeneticAlgorithm import SurvivorSelection


def LoadContainer(containerDimensions: list, 
                  boxes: dict,
                  totalBoxesValue: int,
                  numberOfGenerations: int = 200, 
                  numberOfIndividuals: int = 36, 
                  rotations: int = None, 
                  PC: int = None, 
                  PM1: float = 0.2, 
                  PM2: float = 0.02, 
                  K: int = 2) -> Tuple[list, list]:
    rotations = rotations if rotations is not None else 6  # 1, 2 or 6
    PC = PC if PC is not None else int(0.8 * numberOfIndividuals)
    population = PopulationGenerator.generate_pop(boxes, numberOfIndividuals, rotations)
    generations = 0
    average_fitness = []
    while generations < numberOfGenerations:
        population, fitness = FitnessCalculation.evaluate(population, containerDimensions, boxes, totalBoxesValue)
        population = NSGA2.rank(population, fitness)
        offsprings = OffSpringrecombination.crossover(copy.deepcopy(population), PC, k=K)
        offsprings = OffSpringMutation.mutate(offsprings, PM1, PM2, rotations)
        population = SurvivorSelection.select(population, offsprings, containerDimensions, boxes, totalBoxesValue, numberOfIndividuals)
        average_fitness.append(FitnessCalculation.calc_average_fitness(population))
        generations += 1

    results = []
    for key, value in population.items():
        if value['Rank'] == 1:
            results.append(value['result'])

    return results, average_fitness
