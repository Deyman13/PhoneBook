from readandwrite import add_contact_str, add_contact_list, readfile_str, readfile_list
from printdist import print_list, print_str
from inputreplasechange import input_contakt, change_contact, delete_contact

file_book_str = 'Book1.txt'
file_book_list = 'Book2.txt'


def init_dict():
    book = {}
    book['lst'] = readfile_list(file_book_list)
    book['str'] = readfile_str(file_book_str)
    return book


def print_book(data):
    print_list(data['lst'])
    print()
    print_str(data["str"])


def write_new_contact_str(book):
    add_contact_str(file_book_str, input_contakt())
    book['str'] = readfile_str(file_book_str)


def write_new_contact_list(book):
    add_contact_list(file_book_list, input_contakt())
    book['lst'] = readfile_list(file_book_list)


def replace_contact_str(book):
    repl = change_contact(book['str'])
    if repl[1] != '':
        with open(file_book_str, "r", encoding="utf_8") as r:
            allfile = r.read()
        with open(file_book_str, "w", encoding="utf_8") as s:
            s.write(allfile.replace(repl[1], ', '.join(repl[0],).title()))
        book['str'] = readfile_str(file_book_str)


def replace_contact_list(book):
    repl = change_contact(book['lst'])
    if repl[1] != '':
        with open(file_book_list, "r", encoding="utf_8") as s:
            allfile = s.read()
        with open(file_book_list, "w", encoding="utf_8") as s:
            s.write(allfile.replace(
                '\n'.join(repl[1].split(', ')), '\n'.join(repl[0])).title())
        book['lst'] = readfile_list(file_book_list)


def delete_contact_str(book):
    repl = delete_contact(book['str'])
    if repl != '':
        with open(file_book_str, "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace((repl+'\n'), '')
        with open(file_book_str, "w", encoding="utf_8") as s:
            s.write(allfile)
        book['str'] = readfile_str(file_book_str)


def delete_contact_list(book):
    repl = delete_contact(book['lst'])
    if repl != '':
        with open(file_book_list, "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace('\n'.join(repl.split(', '))+'\n\n', '')
        with open(file_book_list, "w", encoding="utf_8") as s:
            s.write(allfile)
        book['lst'] = readfile_list(file_book_list)
