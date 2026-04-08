from data import *
from praktikum.bun import Bun
import pytest
import allure
class TestBun:
    @allure.title("Проверка получения названия булки")
    @pytest.mark.parametrize('name, price', [(BurgersData.fluorescent_bun, BurgersData.price_fluorescent_bun),
                                             (BurgersData.kratornaya_bun, BurgersData.price_kratornaya_bun),
                                             
                                             ])
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
    @allure.title("Проверка получения цены булки")
    @pytest.mark.parametrize('name, price', [(BurgersData.fluorescent_bun, BurgersData.price_fluorescent_bun),
                                             (BurgersData.kratornaya_bun, BurgersData.price_kratornaya_bun),
                                             
                                             ])
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price