from data import *
from unittest.mock import Mock
import pytest
from praktikum.bun import Bun 
from praktikum.ingredient import Ingredient
import allure
class TestBurger:
    @allure.title("Проверка добавления булочек")
    def test_set_buns(self, burger):
        mock = Mock(spec=Bun)
        mock.get_name.return_value = BurgersData.fluorescent_bun
        mock.get_price.return_value = BurgersData.price_fluorescent_bun
        burger.set_buns(mock)
        assert (burger.bun.get_name() == BurgersData.fluorescent_bun 
        and burger.bun.get_price() == BurgersData.price_fluorescent_bun)
    @allure.title("Проверка добавления соусов на соответствие названия,цены и типа")
    @pytest.mark.parametrize('name, price', [(BurgersData.Spicy_sauce, BurgersData.price_Spicy_sauce),
                                             (BurgersData.Space_sauce, BurgersData.Space_sauce),
                                             (BurgersData.traditional_sauce, BurgersData.price_traditional_sauce),
                                             (BurgersData.Antarian_sauce, BurgersData.Antarian_sauce)
                                             ])
    def test_add_ingredient_sauce(self, burger, name, price):
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = BurgersData.INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock)
        assert (name == burger.ingredients[0].get_name() and
        price == burger.ingredients[0].get_price() and
        BurgersData.INGREDIENT_TYPE_SAUCE == burger.ingredients[0].get_type())
    @allure.title("Проверка добавления топпингов на соответствие названия,цены и типа")
    @pytest.mark.parametrize('name, price', [(BurgersData.protostomia_filling, BurgersData.protostomia_price),
                                             (BurgersData.beef_meteor_filling, BurgersData.beef_meteor_price),
                                             (BurgersData.magnoly_filling, BurgersData.magnoly_price),
                                             (BurgersData.luminescent_filling, BurgersData.luminescent_price),
                                             (BurgersData.crispy_ring_filling, BurgersData.crispy_ring_price),
                                             (BurgersData.fallen_tree_filling, BurgersData.fallen_tree_price),
                                             (BurgersData.alpha_filling, BurgersData.alpha_price),
                                             (BurgersData.mini_salad_filling, BurgersData.mini_salad_price),
                                             (BurgersData.cheese_filling, BurgersData.cheese_price)
                                             ])
    def test_add_ingredient_filling(self, burger, name, price):
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = BurgersData.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock)
        assert (name == burger.ingredients[0].get_name() and
        price == burger.ingredients[0].get_price() and
        BurgersData.INGREDIENT_TYPE_FILLING == burger.ingredients[0].get_type())
    @allure.title("Проверка удаления ингредиентов")        
    def test_remove_ingredient(self, burger):
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = BurgersData.protostomia_filling
        mock.get_price.return_value = BurgersData.protostomia_price
        mock.get_type.return_value = BurgersData.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []        
    @allure.title("Проверка перемещения ингредиентов на другую позицию")
    def test_move_ingredient(self, burger):
        mock_first_ing = Mock(spec=Ingredient)
        mock_first_ing.get_name.return_value = BurgersData.protostomia_filling
        mock_first_ing.get_price.return_value = BurgersData.protostomia_price
        mock_first_ing.get_type.return_value = BurgersData.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_first_ing)
        mock_second_ing = Mock(spec=Ingredient)
        mock_second_ing.get_name.return_value = BurgersData.beef_meteor_filling
        mock_second_ing.get_price.return_value = BurgersData.beef_meteor_price
        mock_second_ing.get_type.return_value = BurgersData.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_second_ing)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].get_name() == BurgersData.beef_meteor_filling   
    @allure.title("Проверка расчета итоговой стоимости")
    def test_get_price(self, burger):
        mock_first = Mock(spec=Bun)
        mock_first.get_name.return_value = BurgersData.fluorescent_bun
        mock_first.get_price.return_value = BurgersData.price_fluorescent_bun
        burger.set_buns(mock_first)
        mock_second = Mock(spec=Ingredient)
        mock_second.get_name.return_value = BurgersData.protostomia_filling
        mock_second.get_price.return_value = BurgersData.protostomia_price
        mock_second.get_type.return_value = BurgersData.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_second)
        assert burger.get_price() == BurgersData.price_fluorescent_bun*2 + BurgersData.protostomia_price       

    @allure.title("Проверка рецепта")
    def test_get_receipt_(self, burger):
        mock_first = Mock(spec=Bun)
        mock_first.get_name.return_value = BurgersData.fluorescent_bun
        mock_first.get_price.return_value = BurgersData.price_fluorescent_bun
        burger.set_buns(mock_first)
        mock_second = Mock(spec=Ingredient)
        mock_second.get_name.return_value = BurgersData.protostomia_filling
        mock_second.get_price.return_value = BurgersData.protostomia_price
        mock_second.get_type.return_value = BurgersData.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_second)
        expected_price = BurgersData.price_fluorescent_bun * 2 + BurgersData.protostomia_price
        expected_receipt = (
        f'(==== {BurgersData.fluorescent_bun} ====)\n'
        f'= {BurgersData.INGREDIENT_TYPE_FILLING.lower()} {BurgersData.protostomia_filling} =\n'
        f'(==== {BurgersData.fluorescent_bun} ====)\n\n'
        f'Price: {expected_price}'
        )
        assert burger.get_receipt() == expected_receipt