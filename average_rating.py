def avr_rating(txt):
    avr_list = []
    first_lesson = 0
    second_lesson = 0
    third_lesson = 0
    total_stud = 0
    for line in txt.readlines():
        info = line.strip().split(';')
        rating = [int(i) for i in info[1:]]
        avr = sum(rating) / len(rating)
        avr_list.append(avr)
        first_lesson += rating[0]
        second_lesson += rating[1]
        third_lesson += rating[2]
        total_stud += 1

    avr_first = str(first_lesson / total_stud)
    avr_second = str(second_lesson / total_stud)
    avr_third = str(third_lesson / total_stud)

    total_list = [avr_first, avr_second, avr_third]
    avr_list.append(' '.join(total_list))
    return avr_list


with open('dataset_3363_4.txt', 'r') as file:
    write_file = avr_rating(file)

with open('dataset_3363_4.txt', 'w') as file:
    for line in write_file:
        file.write(str(line) + '\n')
