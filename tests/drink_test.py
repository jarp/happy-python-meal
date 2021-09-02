import pytest
from happymeal.models.drinks import *



def test_sprite_repr():
    sprite = Sprite()
    assert repr(sprite) == "Sprite"