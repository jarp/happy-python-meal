import pytest
from happymeal.models.hamburger import Hamburger
from happymeal.models.condiment import Condiment

class Sand:
    def __init__(self):
        print("sand")



@pytest.fixture
def basic_hamburger():
    return Hamburger()

@pytest.fixture
def hamburger_with_stuff():
    return Hamburger(condiments=[Condiment(name="mayo", calories=20), Condiment(name="Tomato", calories=5)])

@pytest.fixture
def hamburger_with_non_stuff():
    return Hamburger(condiments=[Condiment(name="mayo", calories=20), Sand()])


def test_basic_hamburger_has_300_calories(basic_hamburger):
    assert basic_hamburger.calories() == 300

def test_hamburger_with_condiments(hamburger_with_stuff):
    assert hamburger_with_stuff.calories() == 325

def test_hamburger_with_non_food_condiment(hamburger_with_non_stuff):
    assert hamburger_with_non_stuff.calories() == 320 