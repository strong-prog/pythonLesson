"""
На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.
"""

split_string = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split(' ')
dup_letter_list = []
packing_letter = []

for i in range(len(split_string)):
    if not packing_letter:
        packing_letter.append(split_string[i])
    else:
        if split_string[i] == packing_letter[-1]:
            packing_letter.append(split_string[i])
        else:
            copy_packing_letter = packing_letter.copy()
            dup_letter_list.append(copy_packing_letter)
            packing_letter.clear()
            packing_letter.append(split_string[i])

if packing_letter:
    dup_letter_list.append(packing_letter)

print(dup_letter_list)
