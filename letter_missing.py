import string
letters = string.ascii_lowercase
# Define the function letter_missing


def letter_missing(letters_given):
    l = len(letters_given)
    start = letters.index(letters_given[0])
    for letter in letters[start:l]:
        if letter not in letters_given:
            return letter
    return ('No letter missing')


print(letter_missing('abcd'))
print(letter_missing('abcdf'))
