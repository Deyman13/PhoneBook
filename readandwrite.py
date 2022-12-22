

def readfile_str(file_book):
    with open(file_book, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ''), s.readlines()))


def readfile_list(file_book):
    with open(file_book, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ', '), s.read().split('\n\n')))


def add_contact_str(file_book, contact):
    with open(file_book, "a", encoding="utf_8") as s:
        s.write(", ".join(contact).title()+"\n")


def add_contact_list(file_book, contact):
    with open(file_book, "a", encoding="utf_8") as s:
        s.write(str("\n".join(contact).title()+'\n\n'))
