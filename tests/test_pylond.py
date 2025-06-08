import pytest
from pylond import (open_data,
                    alpha2, 
                    alpha3,
                    numeric,
                    country_lookup,
                    iter_countries,
                    lang_alpha3,
                    lang_lookup,
                    iter_languages)

def test_open_data():
    assert open_data()

# Alpha2 tests

def test_alpha2_valid_country():
    res = alpha2('is')
    assert res
    assert isinstance(res, dict)
    assert len(res) == 11
    assert res['short_name'] == 'Ísland'

def test_alpha2_invalid_country():
    res = alpha2('invalid country')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_alpha2_invalid_type():
    with pytest.raises(TypeError):
        alpha2(1)

# Alpha3 tests

def test_alpha3_valid_country():
    res = alpha3('nor')
    assert res
    assert isinstance(res, dict)
    assert len(res) == 11
    assert res['short_name'] == 'Noregur'

def test_alpha3_invalid_country():
    res = alpha3('invalid country')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_alpha3_invalid_type():
    with pytest.raises(TypeError):
        alpha2(1)

# Numeric tests

def test_numeric_valid_country():
    res = numeric(752)
    assert res
    assert isinstance(res, dict)
    assert len(res) == 11
    assert res['short_name'] == 'Svíþjóð'

def test_numeric_invalid_country():
    res = alpha3('invalid country')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_numeric_invalid_type():
    with pytest.raises(TypeError):
        numeric('invalid type')

# Country_lookup tests

def test_country_lookup_valid_country():
    res = country_lookup('Finland')
    assert res
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0]['short_name'] == 'Finnland'

def test_country_lookup_invalid_country():
    res = country_lookup('invalid country')
    assert isinstance(res, list)
    assert len(res) == 0

def test_country_lookup_invalid_types_and_values():
    with pytest.raises(TypeError):
        country_lookup(name=1)
    with pytest.raises(TypeError):
        country_lookup(lev_ratio="invalid type")
    with pytest.raises(ValueError):
        country_lookup(name="Belarus", lang='invalid value')
    with pytest.raises(ValueError):
        country_lookup(name="Ukraine", lev_ratio=11)

def test_country_lookup_valid_parameters():
    res = country_lookup('Irap', lang='en', lev_ratio=0.75)
    assert res
    assert isinstance(res, list)
    assert len(res) == 2
    assert res[0]['short_name'] == 'Íran'
    assert res[1]['short_name'] == 'Írak'
    res = country_lookup('Írap', lang='is', lev_ratio=0.75)
    assert res[0]['short_name'] == 'Íran'
    assert res[1]['short_name'] == 'Írak'

# Iter_countries tests

def test_valid_iter_countries():
    res = iter_countries()
    assert res
    assert isinstance(res, list)
    assert len(res) >= 195
    assert res[-1]['short_name'] == 'Simbabve'
    res = iter_countries(sort='is')
    assert res
    assert isinstance(res, list)
    assert len(res) >= 195
    assert res[-1]['short_name'] == 'Þýskaland'

def test_iter_countries_sort_invalid_type():
    with pytest.raises(ValueError):
        iter_countries(sort=1)

def test_iter_countries_sort_invalid_string():
    with pytest.raises(ValueError):
        iter_countries(sort='english')

# Lang_alpha3 tests

def test_lang_alpha3_valid_language():
    res = lang_alpha3('isl')
    assert res
    assert isinstance(res, dict)
    assert len(res) == 3
    assert res['icelandic_name'] == 'íslenska'

def test_lang_alpha3_invalid_language():
    res = alpha3('xyz')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_lang_alpha3_invalid_type():
    with pytest.raises(TypeError):
        lang_alpha3(1)

# lang_lookup tests

def test_lang_lookup_valid_country():
    res = lang_lookup('danish')
    assert res
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0]['icelandic_name'] == 'danska'

def test_lang_lookup_invalid_country():
    res = lang_lookup('invalid language')
    assert isinstance(res, list)
    assert len(res) == 0

def test_lang_lookup_invalid_types_and_values():
    with pytest.raises(TypeError):
        lang_lookup(name=1)
    with pytest.raises(TypeError):
        lang_lookup(lev_ratio="invalid type")
    with pytest.raises(ValueError):
        lang_lookup(name="dutch", lang='invalid value')
    with pytest.raises(ValueError):
        lang_lookup(name="french", lev_ratio=11)

def test_lang_lookup_valid_parameters():
    res = lang_lookup('Luburian', lev_ratio=0.70)
    assert res
    assert isinstance(res, list)
    assert len(res) == 3
    assert res[0]['icelandic_name'] == 'búlgarska'
    assert res[1]['icelandic_name'] == 'lígúríska'
    assert res[2]['icelandic_name'] == 'limbúrgíska'

# Iter_languages tests

def test_valid_iter_languages():
    res = iter_languages()
    assert res
    assert isinstance(res, list)
    assert len(res) >= 226
    assert res[-1]['english_name'] == 'Zulu'
    res = iter_languages(sort='is')
    assert res
    assert isinstance(res, list)
    assert len(res) >= 226
    assert res[-1]['icelandic_name'] == 'þýska'

def test_iter_languages_sort_invalid_type():
    with pytest.raises(ValueError):
        iter_languages(sort=1)

def test_iter_languages_sort_invalid_string():
    with pytest.raises(ValueError):
        iter_languages(sort='english')

def test_preposition_field():
    res = alpha2("IS")
    assert "preposition" in res
    assert res["preposition"] == "á"
