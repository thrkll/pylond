from .mutual import open_data, levenshtein_ratio

def lang_alpha3(lang_alpha3) -> dict:
    '''Returns a dict based on the ISO-639-3 alpha3 code.'''
    if not isinstance(lang_alpha3, str):
        raise TypeError(f'lang_alpha3 should be str, got: {type(lang_alpha3).__name__}')
    items = open_data('languages')
    headers = next(items)
    result = {}
    for row in items:
        if row[0].lower() == lang_alpha3.lower():
            for key in headers:
                for value in row:
                    result[key] = value
                    row.remove(value)
                    break
    return result

def lang_lookup(name, lang='en', lev_ratio=1) -> list:
    '''
    Returns a list based on English or Icelandic name. 
    The lang parameter can take "en" (default) or "is".
    Optional lev_ratio parameter should be in range of 0 to 1 (default).
    '''
    if not isinstance(name, str):
        raise TypeError(f'Language name should be str, got: {type(name).__name__}')
    if not isinstance(lev_ratio, (int, float)):
        raise TypeError(f'lev_ratio should be int or float, got: {type(lev_ratio).__name__}')
    if not 0 <= lev_ratio <= 1:
        raise ValueError(f'lev_ratio should be in range of 0 and 1, got: {lev_ratio}')
    if lang not in ['en', 'is']:
        raise ValueError(f'Lang can only take en or is, got: {lang}')
    items = open_data('languages')
    headers = next(items)
    result = []
    for row in items:
        if lang == 'en':
            comparison = row[1]
        elif lang == 'is':
            comparison = row[2]
        ratio = levenshtein_ratio(comparison.lower(), name.lower())
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

def iter_languages(sort='en') -> list:
    '''Returns a list of languages. The sort parameter can take "en" (default) or "is"'''
    if sort not in ['en', 'is']:
        raise ValueError(f'Sort parameter can only take en or is, got: {sort}')
    items = open_data('languages')
    headers = next(items)
    result = []
    for row in items:
        inner_dict = {}
        for key in headers:
            for value in row:
                inner_dict[key] = value
                row.remove(value)
                break
        result.append(inner_dict)
    if sort == 'is':
        result = sorted(result, key = lambda d: d['icelandic_name'])
    return result