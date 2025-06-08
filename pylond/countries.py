from .mutual import open_data, levenshtein_ratio

def alpha2(alpha2) -> dict:
    '''Returns a dict based on the ISO-3166-1 alpha2 code.'''
    if not isinstance(alpha2, str):
        raise TypeError(f'alpha2 should be str, got: {type(alpha2).__name__}')
    items = open_data()
    headers = next(items)
    result = {}
    for row in items:
        if row[1].lower() == alpha2.lower():
            for key, value in zip(headers, row):
                result[key] = value
    return result

def alpha3(alpha3) -> dict:
    '''Returns a dict based on the ISO-3166-1 alpha3 code.'''
    if not isinstance(alpha3, str):
        raise TypeError(f'alpha3 should be str, got: {type(alpha3).__name__}')
    items = open_data()
    headers = next(items)
    result = {}
    for row in items:
        if row[2].lower() == alpha3.lower():
            for key, value in zip(headers, row):
                result[key] = value
    return result

def numeric(numeric) -> dict:
    '''Returns a dict based on the ISO-3166-1 numeric code.'''
    if not isinstance(numeric, int):
        raise TypeError(f'numeric should take int, got: {type(numeric).__name__}')
    items = open_data()
    headers = next(items)
    result = {}
    for row in items:
        if int(row[3]) == numeric:
            for key, value in zip(headers, row):
                result[key] = value
    return result

def country_lookup(name, lang='en', lev_ratio=1) -> list:
    '''
    Returns a list based on English or Icelandic short name. 
    The lang parameter can take "en" (default) or "is".
    Optional lev_ratio parameter should be in range of 0 to 1 (default).
    '''
    if not isinstance(name, str):
        raise TypeError(f'Country name should be str, got: {type(name).__name__}')
    if not isinstance(lev_ratio, (int, float)):
        raise TypeError(f'lev_ratio should be int or float, got: {type(lev_ratio).__name__}')
    if not 0 <= lev_ratio <= 1:
        raise ValueError(f'lev_ratio should be in range of 0 and 1, got: {lev_ratio}')
    if lang not in ['en', 'is']:
        raise ValueError(f'Lang can only take en or is, got: {lang}')
    items = open_data()
    headers = next(items)
    result = []
    for row in items:
        if lang == 'en':
            comparison = row[0]
        elif lang == 'is':
            comparison = row[4]
        ratio = levenshtein_ratio(comparison.lower(), name.lower())
        if ratio >= lev_ratio:
            inner_dict = {}
            for key, value in zip(headers, row):
                inner_dict[key] = value
            inner_dict['lev_ratio'] = round(ratio, 2)
            result.append(inner_dict)
    return result

def iter_countries(sort='en') -> list:
    '''Returns a list of countries. The sort parameter can take "en" (default) or "is"'''
    if sort not in ['en', 'is']:
        raise ValueError(f'Sort can only take en or is, got: {sort}')
    items = open_data()
    headers = next(items)
    result = []
    for row in items:
        inner_dict = {}
        for key, value in zip(headers, row):
            inner_dict[key] = value
        result.append(inner_dict)
    if sort == 'is':
        result = sorted(result, key = lambda d: d['short_name'])
    return result
