"""
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
"""


def letter_dict(word):
    char_dict = {}
    for let in word:
        if let in '.,!?:;- ':
            continue
        elif let not in char_dict:
            char_dict[let.lower()] = 1
        else:
            char_dict[let] += 1
    return char_dict


dict1 = letter_dict(input().lower())
dict2 = letter_dict(input().lower())

if dict1 == dict2:
    print('YES')
else:
    print('NO')
