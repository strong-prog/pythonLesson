"""
Даны по 10-балльной шкале оценки по физике трех учеников.
Напишите программу, которая выводит множество оценок третьего ученика,
которые не встречаются ни у первого, ни у второго ученика.
"""

set_score1 = set('1 5 4 2 5 6 6 2 3 3 5 2'.split(' '))
set_score2 = set('2 3 5 1 2 1 2 6 7 1 1 6'.split(' '))
set_score3 = set('1 4 6 9 8 7 0 9 0 9 8 10'.split(' '))

total_set_score = (set_score1 | set_score2) - set_score3
sort_set_score = sorted({int(i) for i in total_set_score})
print(*sort_set_score)
