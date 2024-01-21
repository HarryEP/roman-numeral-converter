import pytest
from main import word_to_numeral, add_new_letter, numeral_to_word


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


def test_negative_number_to_word_is_valid():
    number = -1161
    assert numeral_to_word(number) == "-MCLXI"


def test_four_repetitive_letters_is_invalid():
    word = "MCDCCXXX"
    with pytest.raises(Exception):
        add_new_letter(word, 'X')


def test_numbers_with_nines_in_them():
    number = 2999
    assert numeral_to_word(number) == 'MMCMXCIX'


def test_word_to_number_with_nines():
    word = 'MMCMXCIX'
    assert word_to_numeral(word) == 2999
