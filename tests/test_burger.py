import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:

    def test_burger_initial_state(self):
         "Проверка начального состояния бургера"
         burger = Burger()
         assert burger.bun is None
         assert burger.ingredients == []
         assert len(burger.ingredients) == 0

    def test_set_buns(self):
        "Проверка установки булочки"
        burger = Burger()
        bun = Bun("Sesame Bun", 50)
        burger.set_buns(bun)
        assert burger.bun is bun
        assert burger.bun.get_name() == "Sesame Bun"
        assert burger.bun.get_price() == 50

    def test_set_buns_with_mock(self):
        "Проверка установки булочки с моком"
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Mock Bun"
        mock_bun.get_price.return_value = 175
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    @pytest.mark.parametrize("bun_name,bun_price", [
        ("Sesame Bun", 50),
        ("Black Bun", 100),
        ("Red Bun", 300),
        ("White Bun", 200),
    ])
    def test_set_installing_different_buns(self, bun_name, bun_price):
        "Установка различных булочек"
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    def test_set_buns_replace(self):
        "Проверка замены булочки"
        burger = Burger()
        bun1 = Bun("White Bun", 200)
        bun2 = Bun("Black Bun", 100)
        burger.set_buns(bun1)
        assert burger.bun.get_name() == "White Bun"
        burger.set_buns(bun2)
        assert burger.bun.get_name() == "Black Bun"
        assert burger.bun.get_price() == 100

    def test_add_ingredient(self):
        "Проверка добавления ингредиента"
        burger = Burger()
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        ingredient = Ingredient("FILLING", "dinosaur", 200)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ingredient
        assert burger.ingredients[0].get_name() == "dinosaur"

    def test_add_ingredient_with_mock(self):
        "Проверка добавления ингредиента с моком"
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "Mock Ingredient"
        mock_ingredient.get_price.return_value = 275
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is mock_ingredient