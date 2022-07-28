import re


def restring(char_digit):
    chars = re.findall(r'[a-zA-Z]+', char_digit)
    digit = re.findall(r'\d+', char_digit)

    string = [chars[i] * int(digit[i]) for i in range(len(chars))]
    return ''.join(string)

with open('dataset_3363_2.txt', 'r') as file:
    write_file = restring(file.readline())

with open('dataset_3363_2.txt', 'w') as file:
    file.write(write_file)
