"""
Даны по 10-балльной шкале оценки по математике трех учеников.
Напишите программу, которая выводит множество оценок,
имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.
"""

set_score1 = set('2 9 3 4 6 9'.split(' '))
set_score2 = set('2 3 4 5 2 10'.split(' '))
set_score3 = set('2 3 4 5 3 10'.split(' '))

total_set_score = (set_score1 | set_score2 | set_score3) - (set_score1 & set_score2 & set_score3)
sort_set_score = sorted({int(i) for i in total_set_score})
print(*sort_set_score)
