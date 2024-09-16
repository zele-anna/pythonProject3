from typing import List
import re

def get_names_from_file(file_name :str) -> List[str]:
    """ Функция выбирает имена из файла, игнорируя знаки препинания и числовые значения,
    и возвращает список имен. """
    with open(('data/' + file_name), "r", encoding='UTF-8') as file:
        names_list = re.split(r"\n|[0-9]| |,", file.read())
        pure_names_list = []
        for item in names_list:
            pure_name = ""
            for symbol in item:
                if symbol.isalpha():
                    pure_name += symbol
            if pure_name.isalpha():
                pure_names_list.append(pure_name)
    return pure_names_list


def is_cyrillic(name_item: str) -> bool:
    """ Проверка на вхождение кириллицы в строку. """
    return bool(re.search('[а-яА-я]', name_item))


def filter_russian_names(names_list: str) -> list:
    """ Фильтрация русских имен. """
    russian_names_list = []
    for name_item in names_list:
        if is_cyrillic(name_item):
            russian_names_list.append(name_item)
    return russian_names_list


def filter_english_names(names_list: str) -> list:
    """ Фильтрация русских имен. """
    english_names_list = []
    for name_item in names_list:
        if not is_cyrillic(name_item):
            english_names_list.append(name_item)
    return english_names_list


def save_to_file(file_name: str, data: str) -> None:
    """ Сохраняет данные в файл. """
    with open('data/' + file_name, 'w') as names_file:
        names_file.write(data)

names_list = get_names_from_file('names.txt')
russian_names = filter_russian_names(names_list)
english_names = filter_english_names(names_list)

save_to_file(
    'russian_names.txt',
    '\n'.join(russian_names)
)

save_to_file(
    'english_names.txt',
    '\n'.join(english_names)
)

# for name in russian_names:
#     print(name)
