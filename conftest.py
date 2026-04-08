import pytest

from data import BurgersData
from praktikum.burger import *


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def ingredient():
    ingredient = Ingredient(BurgersData.INGREDIENT_TYPE_SAUCE, BurgersData.Spicy_sauce, BurgersData.price_Spicy_sauce)
    return ingredient


