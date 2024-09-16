from typing import List
import re

def get_names_from_file(file_name :str) -> List[str]:
    """Функция выбирает имена из файла, игнорируя знаки препинания и числовые значения,
    и возвращает список имен"""
    with open(('data/' + file_name), "r", encoding='UTF-8') as file:
        names_list = re.split(r"\n|[0-9]| |,", file.read())
        pure_names_list = []
        for item in names_list:
            pure_name = ""
            for symbol in item:
                if symbol.isalpha():
                    pure_name += symbol
            if pure_name.isalpha():
                pure_names_list.append(cleared_name)
    return pure_names_list

names_list = get_names_from_file('names.txt')
for name in names_list:
    print(name)
