import csv
import os
import numpy as np

def open_data():
    '''Opens data to be utilized by other functions.'''
    root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(root_dir, 'pylond', 'data', 'country_data.csv')
    with open(data_path, 'r', encoding = 'utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row

def alpha2(alpha2) -> dict:
    '''Returns a dict based on the ISO-3166-1 alpha2 code.'''
    countries = open_data()
    headers = next(countries)
    result = {}
    for row in countries:
        if row[1].lower() == alpha2.lower():
            for key in headers:
                for value in row:
                    result[key] = value
                    row.remove(value)
                    break
    return result

def alpha3(alpha3) -> dict:
    '''Returns a dict based on the ISO-3166-1 alpha3 code.'''
    countries = open_data()
    headers = next(countries)
    result = {}
    for row in countries:
        if row[2].lower() == alpha3.lower():
            for key in headers:
                for value in row:
                    result[key] = value
                    row.remove(value)
                    break
    return result

def numeric(numeric)-> dict:
    '''Returns a dict based on the ISO-3166-1 numeric code.'''
    countries = open_data()
    headers = next(countries)
    result = {}
    for row in countries:
        if int(row[3]) == numeric:
            for key in headers:
                for value in row:
                    result[key] = value
                    row.remove(value)
                    break
    return result

def from_english(english_name, lev_ratio=1) -> list:
    '''Returns a list based on the English short name. Optional lev_ratio parameter should be in range of 0 to 1 (default).'''
    if not isinstance(lev_ratio, (int, float)):
        raise TypeError(f'lev_ratio should be int or float, got: {type(lev_ratio).__name__}')
    if not 0 <= lev_ratio <= 1:
        raise ValueError(f'lev_ratio should be in range of 0 and 1, got: {lev_ratio}')
    countries = open_data()
    headers = next(countries)
    result = []
    for row in countries:
        ratio = levenshtein_ratio(row[0].lower(), english_name.lower())
        if ratio >= lev_ratio:
            inner_dict = {}
            for key in headers:
                for value in row:
                    inner_dict[key] = value
                    row.remove(value)
                    break
            inner_dict['lev_ratio'] = round(ratio, 2)
            result.append(inner_dict)
    return result

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

def iter_countries(sort='en') -> list:
    '''Returns a list of countries. The sort parameter can take "en" (default) or "is"'''
    if sort not in ['en', 'is']:
        raise ValueError(f'Sort parameter can only take en or is, got: {sort}')
    countries = open_data()
    headers = next(countries)
    result = []
    for row in countries:
        inner_dict = {}
        for key in headers:
            for value in row:
                inner_dict[key] = value
                row.remove(value)
                break
        result.append(inner_dict)
    if sort == 'is':
        result = sorted(result, key = lambda d: d['short_name'])
    return result