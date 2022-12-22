def input_contakt():
    return input('Введитe фамилию, имя, телефон, описание(15 символов) через пробел.\n').title().split()


def find(book):
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя:\n")
    for line in book:
        if ans.lower() in line.lower():
            return book.index(line)
    print()
    print('===>> Такой записи еще нет, если хотите добавить новую, то нажмите 2 или 3! <<===')
    print()
    return -1


def print_contact(line):
    print("-" * len(line))
    print(line)
    print("-" * len(line))


def search(book):
    temp = book['str']+book['lst']
    index = find(temp)
    if index != -1:
        print_contact(temp[index])


def delete_contact(book):
    index = find(book)
    if index != -1:
        print_contact(book[index])
        if input('Этот контакт будет удален!!! 1 - Да, 2 - Нет\n') == '1':
            print()
            print("Контакт успешно удален!")
            print()
            return book[index]
        print()
        print("Контакт не будет удален")
        print()
        return ''


def change_contact(book):
    index = find(book)
    if index != -1:
        print_contact(book[index])
        if input('Этот контакт будет изменен!!! 1 - Да, 2 - Нет\n') == '1':
            old_result = book[index]
            result = book[index].split(", ")
            change = input(
                "Что именно вы хотите изменить? Введите 'Имя', 'Фамилия', 'Номер', 'Комментарий':\n ")
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
            return result, old_result
        else:
            return '', ''
