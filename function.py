from readandwrite import add_contact_str, add_contact_list, readfile_str, readfile_list
from printdist import print_list, print_str
from inputreplasechange import input_contakt, change_contact, delete_contact

file_book = {"str":'Book1.txt', "lst":'Book2.txt'}


def init_dict(book,key):
    if key == "lst":
        book[key] = readfile_list(file_book[key])
    else:
        book[key] = readfile_str(file_book[key])



def print_book(data):
    print_list(data['lst'])
    print()
    print_str(data["str"])


def write_new_contact_str(book):
    add_contact_str(file_book['str'], input_contakt())
    init_dict(book,'str')
    print()
    print("Контакт успешно добавлен!")


def write_new_contact_list(book):
    add_contact_list(file_book['lst'], input_contakt())
    init_dict(book,'lst')
    print()
    print("Контакт успешно добавлен!")


def replace_contact_str(book):
    repl = change_contact(book['str'])
    if repl[1] != '':
        with open(file_book['str'], "r", encoding="utf_8") as r:
            allfile = r.read()
        with open(file_book['str'], "w", encoding="utf_8") as s:
            s.write(allfile.replace(repl[1], ', '.join(repl[0],).title()))
        init_dict(book,'str')


def replace_contact_list(book):
    repl = change_contact(book['lst'])
    if repl[1] != '':
        with open(file_book['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        with open(file_book['lst'], "w", encoding="utf_8") as s:
            s.write(allfile.replace(
                '\n'.join(repl[1].split(', ')), '\n'.join(repl[0])).title())
        book['lst'] = readfile_list(file_book['lst'])


def delete_contact_str(book):
    repl = delete_contact(book['str'])
    if repl != '':
        with open(file_book["str"], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace((repl+'\n'), '')
        with open(file_book['str'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict(book,'str')


def delete_contact_list(book):
    repl = delete_contact(book['lst'])
    if repl != '':
        with open(file_book['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace('\n'.join(repl.split(', '))+'\n\n', '')
        with open(file_book['lst'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict(book,'lst')


def translate_str(book):
    dictionary = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
              'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
              'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
              'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
              'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
              'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
              'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}


    def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщыьэъюя')):
        return not alphabet.isdisjoint(text.lower())

    boo = book["str"]

    for word in boo:
        for v in word:
            if v.isalpha() and match(v) is True:
                print(dictionary.get(v), end="")
            elif not v.isalpha() or match(v) is False:
                print(v, end="")
        print()

def translate_list(book):
    dictionary = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
              'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
              'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
              'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
              'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
              'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
              'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}


    def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщыьэъюя')):
        return not alphabet.isdisjoint(text.lower())

    boo = book["lst"]

    for word in boo:
        for v in word:
            if v.isalpha() and match(v) is True:
                print(dictionary.get(v), end="")
            elif not v.isalpha() or match(v) is False:
                print(v, end="")
        print()  


import os
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')