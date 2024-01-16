def word_to_numeral(roman: str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    conversions = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    length = len(roman)
    for i, letter in enumerate(roman):
        if i == length - 1:
            total += conversions[letter]
        else:
            if conversions[letter] < conversions[roman[i + 1]]:
                total -= conversions[letter]
            else:
                total += conversions[letter]
    return total


if __name__ == "__main__":
    pass
