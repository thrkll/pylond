import pytest
from pylond import (open_data,
                    alpha2, 
                    alpha3,
                    numeric,
                    from_english,
                    iter_countries)

def test_open_data():
    assert open_data()

def test_alpha2_valid_country():
    res = alpha2('is')
    assert res
    assert isinstance(res, dict)
    assert len(res) == 10
    assert res['short_name'] == 'Ísland'

def test_alpha2_invalid_country():
    res = alpha2('invalid input')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_alpha3_valid_country():
    res = alpha3('nor')
    assert res
    assert isinstance(res, dict)
    assert len(res) == 10
    assert res['short_name'] == 'Noregur'

def test_alpha3_invalid_country():
    res = alpha3('invalid input')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_numeric_valid_country():
    res = numeric(752)
    assert res
    assert isinstance(res, dict)
    assert len(res) == 10
    assert res['short_name'] == 'Svíþjóð'

def test_numeric_invalid_country():
    res = alpha3('invalid input')
    assert isinstance(res, dict)
    assert len(res) == 0

def test_from_english_valid_country():
    res = from_english('Finland')
    assert res
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0]['short_name'] == 'Finnland'

def test_from_english_invalid_country():
    res = from_english('invalid input')
    assert isinstance(res, list)
    assert len(res) == 0

def test_lev_ratio_valid_parameter():
    res = from_english('Irap', lev_ratio=0.75)
    assert res
    assert isinstance(res, list)
    assert len(res) == 2
    assert res[0]['short_name'] == 'Íran'
    assert res[1]['short_name'] == 'Írak'

def test_lev_ratio_invalid_type():
    with pytest.raises(TypeError):
        from_english('Estonia', lev_ratio='invalid parameter type')

def test_lev_ratio_number_not_in_range():
    with pytest.raises(ValueError):
        from_english('Latvia', lev_ratio=11)

def test_valid_iter_countries():
    res = iter_countries()
    assert res
    assert isinstance(res, list)
    assert len(res) >= 195

def test_sort_invalid_type():
    with pytest.raises(ValueError):
        iter_countries(sort=1)

def test_sort_invalid_string():
    with pytest.raises(ValueError):
        iter_countries(sort='eng')