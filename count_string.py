def count_str(string):
    string_list = sorted(string.strip().lower().split(' '))
    count_dict = dict()

    for char in string_list:
        if char not in count_dict:
            count_dict[char] = string_list.count(char)

    list_dict = [el for el in count_dict.items()]
    max_ = list_dict[0]
    
    for el in list_dict:
        if el[1] > max_[1]:
            max_ = el

    return ' '.join([str(i) for i in max_])


with open('dataset_3363_3.txt', 'r') as file:
    write_file = count_str(file.read())

with open('dataset_3363_3.txt', 'w') as file:
    file.write(write_file)
