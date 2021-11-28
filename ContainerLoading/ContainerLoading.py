from typing import List

from ContainerLoading import enums
from ContainerLoading.Models.BinModel import BinModel
from ContainerLoading.Models.ItemModel import ItemModel
from ContainerLoading.GeneticAlgorithm import GeneticAlgorithm


def LoadContainer(container: BinModel, items: List[ItemModel], 
                  algorithm: enums.ContainerLoadingAlgorithm = enums.ContainerLoadingAlgorithm.GENETIC_ALGORITHM, 
                  **kwargs):
    
    if algorithm == enums.ContainerLoadingAlgorithm.GENETIC_ALGORITHM:
        boxes = {}
        for i in range(len(items)):
            boxes[i] = [items[i].length, items[i].width, items[i].height, items[i].volume, items[i].weight]
        rawResults, averageFitness = GeneticAlgorithm.LoadContainer(containerDimensions=[container.length, container.width, container.height], 
                                                                    boxes=boxes,
                                                                    totalBoxesValue=container.maxWeight,
                                                                    **kwargs)
        results = []
        for rawResult in rawResults:
            results.append(list(map(lambda result: ItemModel(x0=result[0],
                                                             y0=result[1],
                                                             z0=result[2],
                                                             length=result[3],
                                                             width=result[4],
                                                             height=result[5],
                                                             weight=0), rawResult)))
        return results, averageFitness
    raise Exception(f'Unknown algorithm: {algorithm}')
