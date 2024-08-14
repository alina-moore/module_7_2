import io
from pprint import pprint

def custom_write(file_name, strings):
    strings_x = {}
    line_counter = 1

    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        x = file.tell()
        file.write(string + '\n')
        strings_x[line_counter, x] = string
        line_counter += 1

    file.close()
    return strings_x


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
