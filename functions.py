from collections import defaultdict
from copy import deepcopy
import matplotlib.pyplot as plt
import os


def group_and_count_tags(questions):
    # return dictionary{tag: (tag count)}
    tagsContainer = defaultdict(int)
    for record in questions['items']:
        for tag in record['tags']:
            tagsContainer[tag] += 1
    return tagsContainer


def get_highest_record(dictTagCount, numberOfHighestRecords=10):
    # returns the list of records with highest score in {key:score}
    sortedByCount = [(tag, score)
                     for tag, score in sorted(dictTagCount.items(), key=lambda column: column[1], reverse=True)]
    return sortedByCount[:numberOfHighestRecords]


def get_normalized_count(dictTagCount):
    # returns normalized number of frequency
    normalizedCount = deepcopy(dictTagCount)
    sum = 0
    for key, value in normalizedCount.items():
        sum += value
    for key, value in normalizedCount.items():
        normalizedCount[key] = value/sum
    return normalizedCount


def print_bar_chart(dictTagCount, Columns=['Column 1', 'Column 2'], fontSize=12, yAxisFactor=1, chartTitle='Bar Chart', save=False):
    data = {}
    data[Columns[0]] = [key for key, value in dictTagCount]
    data[Columns[1]] = [value*yAxisFactor for key, value in dictTagCount]
    plt.title(chartTitle)
    plt.bar(data[Columns[0]], data[Columns[1]])
    plt.xlabel(Columns[0],)
    plt.xticks(fontsize=fontSize-2)
    plt.ylabel(Columns[1])
    plt.tick_params('x', labelrotation=60)
    plt.tick_params('both', grid_alpha=0.5, grid_linestyle='--')
    plt.grid(True)
    plt.show()
    plt.savefig(chartTitle+'.pdf', dpi=600, orientation='portrait', transparent=True,
                bbox_inches='tight', pad_inches=0.1,  metadata=None,)
