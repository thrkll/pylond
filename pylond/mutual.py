import os
import csv
import numpy as np

def open_data(file='countries'):
    '''Opens data to be utilized by other functions.'''
    root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    if file == 'languages':
        data_path = os.path.join(root_dir, 'pylond', 'data', 'language_data.csv')
    elif file == 'countries':
        data_path = os.path.join(root_dir, 'pylond', 'data', 'country_data.csv')
    with open(data_path, 'r', encoding = 'utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row

def levenshtein_ratio(s, t) -> float:
    '''Calculates levenshtein distance and ratio for from_english().'''
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 2
            distance[row][col] = min(distance[row-1][col] + 1,
                                 distance[row][col-1] + 1,
                                 distance[row-1][col-1] + cost)
    ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
    return ratio