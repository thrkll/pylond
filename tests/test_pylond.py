import pytest
from pylond import *

def test_alpha2_valid_country():
    assert isinstance(alpha2('is'), dict)
    assert len(alpha2('is')) == 10
    assert alpha2('is')['short_name'] == 'Ísland'

def test_alpha2_invalid_country():
    assert isinstance(alpha2('iz'), dict)
    assert len(alpha2('iz')) == 0
