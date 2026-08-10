import pytest
from string_utils import StringUtils

@pytest.mark.parametrize("text, result",
[("Skypro", "Skypro"),
("skypro", "Skypro"),
("my skypro", "My skypro"),
(" ", " "),
("кот Василий", "Кот Василий"),
("23skypro", "23skypro"),
(".", ".")])
def test_string_capitalize(text, result):
    string_utils = StringUtils()
    assert string_utils.capitalize(text) == result

@pytest.mark.parametrize("text, result",
[("Skypro", "Skypro"),
(" skypro", "skypro"),
(" skypro ", "skypro "),
(" s k y p r o ", "s k y p r o "),
("_skypro", "_skypro"),
("  ", "")])
def test_string_trim(text, result):
    string_utils = StringUtils()
    assert string_utils.trim(text) == result

@pytest.mark.parametrize("string, symbol, result",
[("Skypro", "S", True),
("Skypro", "s", False),
("Skypro", "g", False),
("Skypro ", " ", True),
("Skypro is Great", " is ", True),
("Skypro", "Skypro", True)])
def test_string_contains(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.contains(string, symbol) == result

@pytest.mark.parametrize("string, symbol, result",
[("Skypro", "S", "kypro"),
("Skypro", "Skypro", ""),
("Skypro", "", "Skypro"),
("Skypro", "u", "Skypro"),
("SkyPro", "Pro", "Sky")])
def test_string_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result