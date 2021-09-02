import pytest
from happymeal.models.condiment import Condiment
from happymeal.models.hamburger import Hamburger

def test_basic_hamburger_has_300_calories():
    c = Condiment()
    assert c.calories() == 20
