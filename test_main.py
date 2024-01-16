import pytest
from main import word_to_numeral, check_valid_roman_numeral


def test_nine_as_word_goes_numeral():
    word = "IX"
    assert word_to_numeral(word) == 9


def test_word_too_high_is_invalid():
    word = "MMMMMXVI"
    with pytest.raises(Exception):
        word_to_numeral(word)


def test_negative_number_is_valid():
    word = "-MCLXI"
    assert word_to_numeral(word) == -1161


def test_four_repetitive_letters_is_invalid():
    word = "MCDCCXXXXVI"
    with pytest.raises(Exception):
        check_valid_roman_numeral(word)
