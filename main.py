import json
import time
import math
from typing import List
from ContainerLoading.Models.BinModel import BinModel
from ContainerLoading.Models.ItemModel import ItemModel
from tests.tools import visualize_plotly
from tests.tools import plotTools
from ContainerLoading import ContainerLoading, enums
from tabulate import tabulate

if __name__ == "__main__":
    with open('tests/testData/input.json', 'r') as outfile:
        data = json.load(outfile)
    problemIndices = list(data.keys())

    for problemIndice in problemIndices:

        print("Running Problem Set {}".format(problemIndice))

        containerDimension = data[problemIndice]['truck dimension']
        solution = data[problemIndice]['solution']
        boxItems = data[problemIndice]['boxes']
        totalWeight = data[problemIndice]['total value']

        averageVolume = []
        averagePlacedItems = []
        averageWeight = []

        container = BinModel(length=containerDimension[0], 
                             width=containerDimension[1], 
                             height=containerDimension[2], 
                             weight=totalWeight,
                             maxWeight=totalWeight)
        items: List[ItemModel] = list(map(lambda box: ItemModel(length=box[0], 
                                                                width=box[1], 
                                                                height=box[2], 
                                                                weight=box[4]), boxItems))
        startTime = time.time()
        results, averageFitness = ContainerLoading.LoadContainer(container, 
                                                                  items, 
                                                                  enums.ContainerLoadingAlgorithm.GENETIC_ALGORITHM)
        stopTime = int(math.ceil(time.time() - startTime))
        color_index = visualize_plotly.draw_solution(pieces=solution)
        visualize_plotly.draw(results, color_index)

        averageVolume.append(averageFitness[-1][0])
        averagePlacedItems.append(averageFitness[-1][1])
        averageWeight.append(averageFitness[-1][2])
        plotTools.plot_stats(averageFitness, title=f"Average Fitness Values - Process Time: {stopTime} sec")

        print(tabulate(
            [['Problem Set', problemIndice], ['Avg. Volume%', sum(averageVolume) / len(averageVolume)],
             ['Avg. Number%', sum(averagePlacedItems) / len(averagePlacedItems)],
             ['Avg. Value%', sum(averageWeight) / len(averageWeight)]],
            headers=['Parameter', 'Value'], tablefmt="github"))
