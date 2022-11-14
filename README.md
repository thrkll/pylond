# pylond

[![Python](https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/pylond?style=for-the-badge&logo=python&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)

### Icelandic translations of countries and nationalities

`pylond` is a Python 3 package that provides translations of countries and nationalities into Icelandic.

## Installation

`pylond` is available to install via PyPi.

```
$ pip install pylond
```

Alternatively, clone the repository.

```
$ git clone https://github.com/thrkll/pylond.git
```

## Usage examples

Look up countries based on the ISO-3166 codes

###### By two letter country codes (ISO-3166-1 alpha2)

```python
>>> from pylond import alpha2

>>> result = alpha2('KG')
>>> pprint(result)

{'adjective': 'kirgiskur',
 'alpha2': 'KG',
 'alpha3': 'KGZ',
 'english_short_name': 'Kyrgyzstan',
 'formal_name': 'Kirgiska lýðveldið',
 'nationality': 'Kirgisi',
 'numeric': '417',
 'short_name': 'Kirgistan'}
```

###### By three letter country codes (ISO-3166-1 alpha3)

```python
>>> from pylond import alpha3

>>> result = alpha2('BWA')
>>> pprint(result)

{'adjective': 'botsvanskur',
 'alpha2': 'BW',
 'alpha3': 'BWA',
 'english_short_name': 'Botswana',
 'formal_name': 'Lýðveldið Botsvana',
 'nationality': 'Botsvanamaður',
 'numeric': '72',
 'short_name': 'Botsvana'}
```

###### By three digit numeric codes (ISO-3166-1 numeric)

```python
>>> from pylond import numeric

>>> result = numeric(203)
>>> pprint(result)

{'adjective': 'tékkneskur',
 'alpha2': 'CZ',
 'alpha3': 'CZE',
 'english_short_name': 'Czechia',
 'formal_name': 'Tékkneska lýðveldið',
 'nationality': 'Tékki',
 'numeric': '203',
 'short_name': 'Tékkland'}
```

Look up countries based on English short name

###### By short English name.

```python
>>> from pylond import from_english

>>> result = from_english('uganda')
>>> pprint(result)

[{'adjective': 'úgandskur',
  'alpha2': 'UG',
  'alpha3': 'UGA',
  'english_short_name': 'Uganda',
  'formal_name': 'Lýðveldið Úganda',
  'lev_ratio': 1.0,
  'nationality': 'Úgandamaður',
  'numeric': '800',
  'short_name': 'Úganda'}]
```

###### Optionally, you can provide a `lev_ratio` parameter to aid with unconvential name spelling. The submitted string will be compared to the data with fuzzy [levensthein matching]() ratio. A value of `1.0` represents a perfect match (the default).

```python
>>> from pylond import from_english

>>> result = from_english('iseland', lev_ratio=0.8)
>>> pprint(result)

[{'adjective': 'írskur',
  'alpha2': 'IE',
  'alpha3': 'IRL',
  'english_short_name': 'Ireland',
  'formal_name': '',
  'lev_ratio': 0.86,
  'nationality': 'Íri',
  'numeric': '372',
  'short_name': 'Írland'},
 {'adjective': 'íslenskur',
  'alpha2': 'IS',
  'alpha3': 'ISL',
  'english_short_name': 'Iceland',
  'formal_name': '',
  'lev_ratio': 0.86,
  'nationality': 'Íslendingur',
  'numeric': '352',
  'short_name': 'Ísland'}]
```

## Data

### Source of data

Codes and english short names are as per the ISO-3166 standard.

Icelandic translations of short and formal country names are from the Icelandic Term Bank. If two or more translation of a country name exist, only the translation recommended by the Language Planning Department of the Árni Magnússon Institute for Icelandic Studies.

📄 [The International Standard for country codes and codes for their subdivisions](https://www.iso.org/iso-3166-country-codes.html)

📄 [The Icelandic Term bank](https://clarin.is/en/resources/termbank/) (CC-BY-SA)

## Versions

▶️ 1.0.0 - Initial release

## Licence

MIT License

Copyright (c) 2022 Þorkell Einarsson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
