import pytest
from pylond import alpha2
from pylond import alpha3


# def test_alpha2_valid_country():
#     res = alpha2('is')
#     assert res
#     assert isinstance(res, dict)
#     assert len(res) == 10
#     assert res['short_name'] == 'Ísland'

# def test_alpha3():
#     assert alpha3('nor')



def test_alpha2_valid_country():
    assert alpha2('is')


def test_alpha3_valid_country():
    assert alpha3('nor')