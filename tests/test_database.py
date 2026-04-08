from data import *
import allure
import pytest
from praktikum.database import Database



class TestDatabase:
    @allure.title("Проверка доступных булок")
    def test_available_buns(self):
        buns = Database()
        available_buns = buns.available_buns()
        assert (available_buns[0].get_name() == "black bun"
        and available_buns[1].get_name() == "white bun" 
        and available_buns[2].get_name() == "red bun")

    @allure.title("Проверка доступных соусов")
    def test_available_ingredients_sauce(self):
        sauce = Database()
        available_sauce = sauce.available_ingredients()
        assert available_sauce[2].get_name() == "chili sauce"
    @allure.title("Проверка доступных топпингов")
    def test_available_ingredients_filling(self):
        filling = Database()
        available_filling = filling.available_ingredients()
        assert available_filling[4].get_name() == "dinosaur"    
    @allure.title("Проверка цены доступных булочек")
    def test_available_buns_price(self):
        buns = Database()
        available_buns = buns.available_buns()
        assert (available_buns[0].get_price() == 100
        and available_buns[1].get_price() == 200
        and available_buns[2].get_price() == 300)
    @allure.title("Проверка цены доступных ингредиентов")
    def test_available_ingredients_price(self):
        ingredient = Database()
        available_ingredient = ingredient.available_ingredients()
        assert available_ingredient[5].get_price() == 300
