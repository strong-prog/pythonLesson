"""
На вход программе подаются две строки, на одной символы,
на другой число n. Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков указанной длины.
"""


def chunked(string_symbol, number):
    split_symbol = string_symbol.split(' ')
    chunks_list = []
    chunk_form = []

    for symbol in split_symbol:
        chunk_form.append(symbol)
        if len(chunk_form) == number:
            copy_chunk_form = chunk_form.copy()
            chunks_list.append(copy_chunk_form)
            chunk_form.clear()

    if chunk_form:
        chunks_list.append(chunk_form)

    return chunks_list


input_symbol = 'a b c d e f'
input_number = 3

print(chunked(input_symbol, input_number))
