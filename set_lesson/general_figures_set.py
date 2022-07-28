"""
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
"""

num_count = int(input())
general_set = set(input())

for _ in range(num_count - 1):
    general_set.intersection_update(input())

sorted_general_set = sorted(general_set)
print(*sorted_general_set)
