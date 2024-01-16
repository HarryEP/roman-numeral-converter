from main import word_to_numeral


def test_nine_as_word_goes_numeral():
    word = "IX"
    assert word_to_numeral(word) == 9
