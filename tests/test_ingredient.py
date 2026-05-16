from data import *
import pytest
import allure

class TestIngredient:
    @allure.title("Проверка цены ингредиента")
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == BurgersData.price_Spicy_sauce
    @allure.title("Проверка названия ингредиента")
    def test_get_name(self, ingredient):
        assert ingredient.get_name() == BurgersData.Spicy_sauce
    @allure.title("Проверка типа ингредиента")
    def test_get_type(self, ingredient):
        assert ingredient.get_type() == BurgersData.INGREDIENT_TYPE_SAUCE        