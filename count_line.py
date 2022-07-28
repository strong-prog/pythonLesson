import requests


def count_line(link):
    info = requests.get(link.strip())
    return len(info.text.splitlines())


with open('dataset_3378_2.txt', 'r') as file:
    write_file = count_line(file.read())

with open('dataset_3378_2.txt', 'w') as file:
    file.write(str(write_file))