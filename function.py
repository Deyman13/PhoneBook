import os
from readandwrite import add_contact_str, add_contact_list, readfile_str, readfile_list
from printdist import print_list, print_str
from inputreplasechange import input_contact_ru, input_contact_eng, change_contact_ru, delete_contact_ru, change_contact_eng, delete_contact_eng

file_book_ru = {"str": 'Book1.txt', "lst": 'Book2.txt'}
file_book_eng = {'str': 'Book3.txt', 'lst': 'Book4.txt'}


def init_dict_ru(book, key):
    if key == "lst":
        book[key] = readfile_list(file_book_ru[key])
    else:
        book[key] = readfile_str(file_book_ru[key])


def init_dict_eng(book, key):
    if key == "lst":
        book[key] = readfile_list(file_book_eng[key])
    else:
        book[key] = readfile_str(file_book_eng[key])


def print_book(data):
    print_list(data['lst'])
    print()
    print_str(data["str"])


def write_new_contact_str_ru(book):
    add_contact_str(file_book_ru['str'], input_contact_ru())
    init_dict_ru(book, 'str')
    print()
    print("Контакт успешно добавлен!")


def write_new_contact_str_eng(book):
    add_contact_str(file_book_eng['str'], input_contact_eng())
    init_dict_eng(book, 'str')
    print()
    print("Contact successfully added!")


def write_new_contact_list_ru(book):
    add_contact_list(file_book_ru['lst'], input_contact_ru())
    init_dict_ru(book, 'lst')
    print()
    print("Контакт успешно добавлен!")


def write_new_contact_list_eng(book):
    add_contact_list(file_book_eng['lst'], input_contact_eng())
    init_dict_eng(book, 'lst')
    print()
    print("Contact successfully added!")


def replace_contact_str_ru(book):
    repl = change_contact_ru(book['str'])
    if repl[1] != '':
        with open(file_book_ru['str'], "r", encoding="utf_8") as r:
            allfile = r.read()
        with open(file_book_ru['str'], "w", encoding="utf_8") as s:
            s.write(allfile.replace(repl[1], ', '.join(repl[0],).title()))
        init_dict_ru(book, 'str')


def replace_contact_str_eng(book):
    repl = change_contact_eng(book['str'])
    if repl[1] != '':
        with open(file_book_eng['str'], "r", encoding="utf_8") as r:
            allfile = r.read()
        with open(file_book_eng['str'], "w", encoding="utf_8") as s:
            s.write(allfile.replace(repl[1], ', '.join(repl[0],).title()))
        init_dict_eng(book, 'str')


def replace_contact_list_ru(book):
    repl = change_contact_ru(book['lst'])
    if repl[1] != '':
        with open(file_book_ru['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        with open(file_book_ru['lst'], "w", encoding="utf_8") as s:
            s.write(allfile.replace(
                '\n'.join(repl[1].split(', ')), '\n'.join(repl[0])).title())
        book['lst'] = readfile_list(file_book_ru['lst'])


def replace_contact_list_eng(book):
    repl = change_contact_eng(book['lst'])
    if repl[1] != '':
        with open(file_book_eng['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        with open(file_book_eng['lst'], "w", encoding="utf_8") as s:
            s.write(allfile.replace(
                '\n'.join(repl[1].split(', ')), '\n'.join(repl[0])).title())
        book['lst'] = readfile_list(file_book_eng['lst'])


def delete_contact_str_ru(book):
    repl = delete_contact_ru(book['str'])
    if repl != '':
        with open(file_book_ru["str"], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace((repl+'\n'), '')
        with open(file_book_ru['str'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict_ru(book, 'str')


def delete_contact_str_eng(book):
    repl = delete_contact_eng(book['str'])
    if repl != '':
        with open(file_book_eng["str"], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace((repl+'\n'), '')
        with open(file_book_eng['str'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict_eng(book, 'str')


def delete_contact_list_ru(book):
    repl = delete_contact_ru(book['lst'])
    if repl != '':
        with open(file_book_ru['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace('\n'.join(repl.split(', '))+'\n\n', '')
        with open(file_book_ru['lst'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict_ru(book, 'lst')


def delete_contact_list_eng(book):
    repl = delete_contact_eng(book['lst'])
    if repl != '':
        with open(file_book_eng['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace('\n'.join(repl.split(', '))+'\n\n', '')
        with open(file_book_eng['lst'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict_eng(book, 'lst')


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
