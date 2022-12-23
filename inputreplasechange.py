def input_contact_ru():
    return input('Введитe фамилию, имя, телефон, описание(15 символов) через пробел.\n').title().split()

def input_contact_eng():
    return input('Enter last name, first name, phone number, description (15 characters) separated by a space.\n').title().split()


def find_string_ru(book):
    result = []
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя:\n")
    for line in book:
        if ans.lower() in line.lower():
            result.append(line)
    return result

def find_string_eng(book):
    result = []
    ans = input(
        "Enter something indicating a specific contact. Phone number, last name or first name:\n")
    for line in book:
        if ans.lower() in line.lower():
            result.append(line)
    return result

def print_contact(line):
    print("-" * len(line))
    print(line)
    print("-" * len(line))


def search_ru(book):
    temp = book['str'] + book['lst']
    ser = find_string_ru(temp)
    for i in set(ser):
        if i != -1:
            print_contact(i)

def search_eng(book):
    temp = book['str'] + book['lst']
    ser = find_string_eng(temp)
    for i in set(ser):
        if i != -1:
            print_contact(i)

def find_ru(book):
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя:\n")
    for line in book:
        if ans.lower() in line.lower():
            return book.index(line)
    print()
    print('===>> Такой записи еще нет, если хотите добавить новую, то нажмите 2 или 3! <<===')
    print()
    return -1

def find_eng(book):
    ans = input(
        "Enter something indicating a specific contact. Phone number, last name or first name:\n")
    for line in book:
        if ans.lower() in line.lower():
            return book.index(line)
    print()
    print('===>> There is no such entry yet, if you want to add a new one, then press 2 or 3! <<===')
    print()
    return -1

def delete_contact_ru(book):
    index = find_ru(book)
    if index != -1:
        print_contact(book[index])
        if input('Этот контакт будет удален!!! 1 - Да, 2 - Нет\n') == '1':
            print()
            print("Контакт успешно удален!")
            print()
            return book[index]
        else:
            print()
            print("Контакт не будет удален!")
            print()
            return ""
    else:
        return ''

def delete_contact_eng(book):
    index = find_eng(book)
    if index != -1:
        print_contact(book[index])
        if input('This contact will be deleted!!! 1 - Yes, 2 - No\n') == '1':
            print()
            print("Contact successfully deleted!")
            print()
            return book[index]
        else:
            print()
            print("The contact will not be deleted!")
            print()
            return ""
    else:
        return ''

def change_contact_ru(book):
    index = find_ru(book)
    if index != -1:
        print_contact(book[index])
        if input('Этот контакт будет изменен!!! 1 - Да, 2 - Нет\n') == '1':
            old_result = book[index]
            result = book[index].split(", ")
            change = input("Что именно вы хотите изменить? Введите 'Имя', 'Фамилия', 'Номер', 'Комментарий':\n ")
            name = result[0]
            secondname = result[1]
            number = result[2]
            comment = result[3]
            change_to = input("На что менять?: ")
            if change.lower() == "имя":
                result.remove(name)
                result.insert(0, change_to)
            elif change.lower() == "фамилия":
                result.remove(secondname)
                result.insert(1, change_to)
            elif change.lower() == "номер":
                result.remove(number)
                result.insert(2, change_to)
            elif change.lower() == "комментарий":
                result.remove(comment)
                result.insert(3, change_to)
            else:
                print("Некорректный ввод!!!")
            print_contact(result)
            print()
            print("Контакт успешно изменен!")
            return result, old_result
        else:
            print()
            print("Контакт не будет изменен!")
            return "", ""
    else:
        return '', ''

def change_contact_eng(book):
    index = find_eng(book)
    if index != -1:
        print_contact(book[index])
        if input('This contact will be changed!!! 1 - Yes, 2 - No\n') == '1':
            old_result = book[index]
            result = book[index].split(", ")
            change = input("What exactly do you want to change? Enter 'First Name', 'Last Name', 'Number', 'Comment':\n ")
            name = result[0]
            secondname = result[1]
            number = result[2]
            comment = result[3]
            change_to = input("What to change?: ")
            if change.lower() == "first name":
                result.remove(name)
                result.insert(0, change_to)
            elif change.lower() == "last name":
                result.remove(secondname)
                result.insert(1, change_to)
            elif change.lower() == "number":
                result.remove(number)
                result.insert(2, change_to)
            elif change.lower() == "comment":
                result.remove(comment)
                result.insert(3, change_to)
            else:
                print("Incorrect input!!!")
            print_contact(result)
            print()
            print("The contact has been successfully changed!")
            return result, old_result
        else:
            print()
            print("The contact will not be changed!")
            return "", ""
    else:
        return '', ''
