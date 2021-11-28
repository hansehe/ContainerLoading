import matplotlib.pyplot as plt
import matplotlib.tri as mtri


def plot_stats(average_fitness, title=""):
    x1 = range(len(average_fitness))
    avg_freespace = []
    avg_number = []
    avg_value = []

    for item in average_fitness:
        avg_freespace.append(item[0])
        avg_number.append(item[1])
        avg_value.append(item[2])

    plt.plot(x1, avg_freespace, label='Average Occupied Volume')
    plt.plot(x1, avg_number, label='Average Number of Boxes')
    plt.plot(x1, avg_value, label='Average Value of Boxes')
    plt.xlabel('Number of Generations')
    plt.ylabel('Fitness Values')
    plt.xticks(ticks=[t for t in x1 if t % 20 == 0])
    plt.title(title)
    plt.legend()
    plt.show()


def calc_average_fitness(individuals):
    fitness_sum = [0.0, 0.0, 0.0]
    count = 0
    for key, value in individuals.items():
        if value['Rank'] == 1:
            count += 1
            fitness_sum[0] += value['fitness'][0]
            fitness_sum[1] += value['fitness'][1]
            fitness_sum[2] += value['fitness'][2]
    average = [number / count for number in fitness_sum]
    return average


def draw_pareto(population):
    fitness = []
    number = []
    weight = []
    fitness2 = []
    number2 = []
    weight2 = []
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = []

    for key, value in population.items():
        if value['Rank'] == 1:
            fitness.append(value['fitness'][0])
            number.append(value['fitness'][1])
            weight.append(value['fitness'][2])
            colors.append('red')
        else:
            colors.append('blue')
            fitness2.append(value['fitness'][0])
            number2.append(value['fitness'][1])
            weight2.append(value['fitness'][2])

    if len(fitness) > 2:
        try:
            ax.scatter(fitness2, number2, weight2, c='b', marker='o')
            ax.scatter(fitness, number, weight, c='r', marker='o')
            triang = mtri.Triangulation(fitness, number)
            ax.plot_trisurf(triang, weight, color='red')
            ax.set_xlabel('occupied space')
            ax.set_ylabel('no of boxes')
            ax.set_zlabel('value')
            plt.show()
        except:
            print(
                "ERROR : Please try increasing the number of individuals as the unique Rank 1 solutions is less than 3")
