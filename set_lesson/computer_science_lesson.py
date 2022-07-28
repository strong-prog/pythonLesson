"""
Даны по 1010-балльной шкале оценки по информатике трех учеников.
Напишите программу, которая выводит множество оценок, которые есть и у первого и у второго учеников,
но которых нет у третьего ученика.
"""

student1_set = set('4 2 5 10 6 2'.split(' '))
student2_set = set('10 4 7 6 3 10'.split(' '))
student3_set = set('1 2 1 5 9 5'.split(' '))

total_set = (student1_set & student2_set) - student3_set
total_set = {int(i) for i in total_set}
sort_total_set = sorted(total_set, reverse=True)
print(*sort_total_set)
