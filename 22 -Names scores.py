'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a 
name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

def names_extract(NAMES_FILE):
    with open(NAMES_FILE) as open_file:
        names = list(open_file.read().split(','))
    return sorted(names)


def letter_value(letter):
    return 'abcdefghijklmnopqrstuvwxyz'.index(letter.lower()) + 1


def alpha_value(name):
    value = 0
    for letter in name:
        value += letter_value(letter)
    return value


def main():

    NAMES_FILE = 'names.txt'
    print(f'Extracting names from {NAMES_FILE}\n')
    names = names_extract(NAMES_FILE)
    total = 0
    i = 1
    for name in names:
        total += (alpha_value(name.strip('"')) * i)
        i += 1

    print(f'\nThe total names score is: {total}')


if __name__ == "__main__":
    main()
