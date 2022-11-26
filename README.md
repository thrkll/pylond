# pylond

[![Python](https://img.shields.io/badge/Python_3-3776AB?logo=python&logoColor=white)](https://opensource.org/licenses/MIT)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/pylond?logo=python&logoColor=white)]()
[![Release](https://img.shields.io/github/v/release/thrkll/pylond)]()
[![pytest](https://github.com/thrkll/pylond/actions/workflows/python-app.yml/badge.svg)]()

### Icelandic translations of countries, nationalities and languages

`pylond` is a Python 3.6+ package that provides Icelandic translations of countries, nationalities and languages.

## Installation

`pylond` is available to install via [PyPi](). 

```
$ pip install pylond
```

Alternatively, clone the repository and install the package using the following commands.

```
$ git clone https://github.com/thrkll/pylond.git
$ cd pylond
$ python setup.py install
```

## Usage examples

###  Look up a country based on the ISO-3166 codes

###### 🔎 By two letter country code (ISO-3166-1 alpha2)

```python
>>> from pylond import alpha2

>>> result = alpha2('KG')
>>> pprint(result)

{'adjective_f': 'kirgisk',
 'adjective_m': 'kirgiskur',
 'adjective_n': 'kirgiskt',
 'alpha2': 'KG',
 'alpha3': 'KGZ',
 'english_short_name': 'Kyrgyzstan',
 'formal_name': 'Kirgiska lýðveldið',
 'demonym': 'Kirgisi',
 'numeric': '417',
 'short_name': 'Kirgistan'}
```

###### 🔎 By three letter country code (ISO-3166-1 alpha3)

```python
>>> from pylond import alpha3

>>> result = alpha2('BWA')
>>> pprint(result)

{'adjective_f': 'botsvönsk',
 'adjective_m': 'botsvanskur',
 'adjective_n': 'botsvanskt',
 'alpha2': 'BW',
 'alpha3': 'BWA',
 'english_short_name': 'Botswana',
 'formal_name': 'Lýðveldið Botsvana',
 'demonym': 'Botsvanamaður',
 'numeric': '72',
 'short_name': 'Botsvana'}
```

###### 🔎 By three digit numeric code (ISO-3166-1 numeric)

```python
>>> from pylond import numeric

>>> result = numeric(203)
>>> pprint(result)

{'adjective_f': 'tékknesk',
 'adjective_m': 'tékkneskur',
 'adjective_n': 'tékkneskt',
 'alpha2': 'CZ',
 'alpha3': 'CZE',
 'english_short_name': 'Czechia',
 'formal_name': 'Tékkneska lýðveldið',
 'demonym': 'Tékki',
 'numeric': '203',
 'short_name': 'Tékkland'}
```

### Country lookup based on English short name

###### 🔎 By English short name as defined by ISO-3166-1

```python
>>> from pylond import country_lookup

>>> result = country_lookup('guyana')
>>> pprint(result)

[{'adjective_f': 'gvæjönsk',
  'adjective_m': 'gvæjanskur',
  'adjective_n': 'gvæjanskt',
  'alpha2': 'GY',
  'alpha3': 'GUY',
  'english_short_name': 'Guyana',
  'formal_name': 'Samvinnulýðveldið Gvæjana',
  'lev_ratio': 1.0,
  'demonym': 'Gvæjanamaður',
  'numeric': '328',
  'short_name': 'Gvæjana'}]
```

###### 🔎 The optional `lev_ratio` parameter can aid with unconvential name spelling. The input string will be compared to the data with a [levensthein matching]() ratio. A value of `1.0` (default) represents a perfect match. Additionally, you can supply a `lang` parameter that takes either `is` or `en` (default) depending on which of the languages you want to iterate through. 


```python
>>> from pylond import country_lookup

>>> result = country_lookup('iseland', lev_ratio=0.8, lang='en')
>>> pprint(result)

[{'adjective_f': 'írsk',
  'adjective_m': 'írskur',
  'adjective_n': 'írskt',
  'alpha2': 'IE',
  'alpha3': 'IRL',
  'english_short_name': 'Ireland',
  'formal_name': '',
  'lev_ratio': 0.86,
  'demonym': 'Íri',
  'numeric': '372',
  'short_name': 'Írland'},
 {'adjective_f': 'íslensk',
  'adjective_m': 'íslenskur',
  'adjective_n': 'íslenskt',
  'alpha2': 'IS',
  'alpha3': 'ISL',
  'english_short_name': 'Iceland',
  'formal_name': '',
  'lev_ratio': 0.86,
  'demonym': 'Íslendingur',
  'numeric': '352',
  'short_name': 'Ísland'}]
```

### Return all countries or languages 

###### 🔎 `iter_countries` and `iter_languages` will return an alphabetic list of all countries or languages respectively. The optional `sort` parameter takes either `is` or `en` (default) depending on which language to sort by.

```python
>>> from pylond import iter_countries, iter_languages

>>> result = iter_countries(sort='is')
>>> pprint(result)

[{country 1 🌎},
 {country 2 🌎},
 {et cetera 🌎}]

>>> result = iter_languages(sort='is')
>>> pprint(result)

[{language 1 🧾},
 {language 2 🧾},
 {et cetera  🧾}]

```
### Look up a language based on the ISO-639 code

###### 🔎 By three letter language code (ISO-3166-3 alpha3)

```python
>>> from pylond import lang_alpha3

>>> result = lang_alpha3('bre')
>>> pprint(result)

{'alpha3': 'bre', 
 'english_name': 'Breton', 
 'icelandic_name': 'bretónska'}

```

### Language lookup based on English name

###### 🔎 Based on English language name as defined by ISO-639-3
```python
>>> from pylond import lang_lookup

>>> result = lang_lookup('polish')
>>> pprint(result)

[{'alpha3': 'pol',
  'english_name': 'Polish',
  'icelandic_name': 'pólska',
  'lev_ratio': 1.0}]

```
###### 🔎 The optional `lev_ratio` parameter can aid with unconvential name spelling. The input string will be compared to the data with a [levensthein matching]() ratio. A value of `1.0` (default) represents a perfect match. Additionally, you can supply a `lang` parameter that takes either `is` or `en` (default) depending on which of the languages you want to iterate through. 

```python
>>> from pylond import lang_lookup

>>> result = lang_lookup('albaníska', lang='is', lev_ratio=0.9)
>>> pprint(result)

[{'alpha3': 'sqi',
  'english_name': 'Albanian',
  'icelandic_name': 'albanska',
  'lev_ratio': 0.94}]

```

## Data

The data is [stored as CSV files](https://github.com/thrkll/pylond/blob/main/pylond/data) so it can also be utilized independent of the `pylond` package.


### Limitations

`pylond` exclusively includes sovereign UN member and observer state countries. Not all names of languages specified in ISO 639 have been translated to Icelandic. Included in `pylond` are nonetheless all languages that have a status of an official language in any sovereign UN member state with some additional ones.  

For some countries, no official formal name exists and is therefore not translatable to Icelandic. Similarly, some countries either do not have an existing demonym (e.g. the Holy See) or no Icelandic translation exists (e.g. Saint Kitts and Nevis). In rare cases, adjectives of nationalities do not exist (e.g. Côte d'Ivoire) and are therefore missing from the data.

### Source of data

Codes and English names are as per the ISO 3166 and ISO 639 standards.

Icelandic translations of language names, short and formal country names are from the Icelandic Term Bank. If two or more translations of a country name exist, only the translation recommended by the Language Planning Department of the Árni Magnússon Institute for Icelandic Studies is used. 

`pylond` also embeds data from the [Database of Icelandic Morphology (DIM)](https://bin.arnastofnun.is/DMII/).

#### 📄 [ISO 3166 Country codes](https://www.iso.org/iso-3166-country-codes.html)

#### 📄 [ISO 639 Language codes](https://www.iso.org/iso-639-language-codes.html)

#### 📄 [The Icelandic Term bank / Íðorðabankinn](https://clarin.is/en/resources/termbank/) (CC-BY-SA 4.0)

#### 📄 [Database of Icelandic Morphology / Beygingarlýsing íslensks nútímamáls](https://bin.arnastofnun.is/) (CC-BY-SA 4.0)


## Versions

📦 0.0.2 - Added support for translations of languages

📦 0.0.1 - Initial unstable release

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

---

The recipient of data from DIM is required to accredit the right holder clearly in the user interface of all products based on the data. The following is hereby attributed: _The Database of Icelandic Morphology. The Árni Magnússon Institute for Icelandic Studies. Author and editor Kristín Bjarnadóttir_
