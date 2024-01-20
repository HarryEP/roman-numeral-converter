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


def numeral_to_word(number: int) -> str:
    word = ''
    temp = abs(number)
    if number < 0:
        word += '-'
    while temp != 0:
        if temp // 1000 != 0:
            word = add_new_letter(word, 'M')
            temp -= 1000
        elif temp // 500 != 0:
            word += add_new_letter(word, 'D')
            temp -= 500
        elif temp // 100 != 0:
            word += add_new_letter(word, 'C')
            temp -= 100
        elif temp // 50 != 0:
            word += add_new_letter(word, 'L')
            temp -= 50
        elif temp // 10 != 0:
            word += add_new_letter(word, 'X')
            temp -= 10
        elif temp // 5 != 0:
            word += add_new_letter(word, 'V')
            temp -= 5
        elif temp // 1 != 0:
            word += add_new_letter(word, 'I')
            temp -= 1
    return word


def add_new_letter(roman: str, letter: str) -> str:
    if len(roman) >= 3:
        if roman[-3] == letter and roman[-2] == letter and roman[-1] == letter:
            raise Exception(
                "You cannot have 4 letters in a row for a roman numeral")
        else:
            roman += letter
    else:
        roman += letter
    return roman


if __name__ == "__main__":
    print(numeral_to_word(3123))
    print(word_to_numeral("IX"))
