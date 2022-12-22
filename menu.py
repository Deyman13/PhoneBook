from function import init_dict, print_book, write_new_contact_list, write_new_contact_str, replace_contact_list, replace_contact_str, delete_contact_str, delete_contact_list, clear
from inputreplasechange import search


def print_hint():
    print('''\n                  
        |====================================================================|
        |           ===>> КОМАНДЫ ДЛЯ РАБОТЫ СО СПРАВОЧНИКОМ <<===           |
        |====================================================================|

        ||-*-*-*-*--------------------------------------------------*-*-*-*-||
        ||                                                                  ||
        ||     Выход из программы: 0 или Enter                             ||
        ||     Просмотр всех записей обоих справочников:  - 1              ||
        ||     Добавление новой записи в строковый справочник: - 2         ||
        ||     Добавление новой записи в списочный справочник: - 3         ||
        ||     Поиск необходимого контакта по параметрам - 4               ||
        ||     Изменение записи из строкового справочника по данным: - 5   ||
        ||     Изменение записи из списочного справочника по данным: - 6   ||
        ||     Удаление записи из строкового справочника по данным: - 7    ||
        ||     Удаление записи из списочного справочника по данным: - 8    ||
        ||     Очистка терминала - 9                                       ||
        ||                                                                  ||
        ||-*-*-*-*--------------------------------------------------*-*-*-*-||''')


def menu():
    print()
    print("ВНИМАНИЕ!!!")
    print("ПОЖАЛУЙСТА, РАСКРОЙТЕ ТЕРМИНАЛ ПОЛНОСТЬЮ ДЛЯ УДОБНОГО ПОЛЬЗОВАНИЯ НАШЕЙ ПРОГРАММОЙ!!!")
    flag = True
    while flag:
        print()
        ans = input("Вы раскрыли терминал? Введите ДА или НЕТ: ")
        print()
        if ans.lower() == "да":
            flag = False
            print("                 || ===---===---===---===---===---===---===---=== ||")
            print("                 |-|-|       ПРИЯТНОГО ПОЛЬЗОВАНИЯ!!! :)       |-|-|")
            print("                 || ===---===---===---===---===---===---===---=== ||")
            book_all = {}
            init_dict(book_all, "str")
            init_dict(book_all, "lst")
            dict_command = {'1': print_book, '2': write_new_contact_str,
                            '3': write_new_contact_list, '4': search, '5': replace_contact_str,
                            '6': replace_contact_list, '7': delete_contact_str, '8': delete_contact_list}
            print_hint()
            while True:
                print()
                print("===>> Введите help, чтобы вывести список команд, если вы забыли их! <<===")
                print("===>> Чтобы очистить терминал нажмите 9 <<===")
                command = input('Команда: > ')
                if command in dict_command:
                    dict_command[command](book_all)
                elif command == "0" or command == '':
                    print("| ---------------------------------------------------------- |")
                    print("|     ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ, НАДЕЕМСЯ ВАМ ПОНРАВИЛОСЬ!)      |")
                    print("|                                                            |")
                    print("|    Работа выполнена Шкляевым Даниилом, Лукашенок Борисом   |")
                    print("|                                                            |")
                    print("|    Даниил - Backend, Frontend                              |")
                    print("|    Борис - Backend, ProjectManager, MainLogic              |")
                    print("|    Все права защищены © Dec 22, 2022 DanBOR, Inc           |")
                    print("| ---------------------------------------------------------- |")
                    break
                elif command == "9":
                    clear()
                elif command.lower() == "help":
                    print_hint()
                else:
                    print('Команда не распознана, попробуйте снова')   
        elif ans.lower() == "нет":
            print()
            print("Тогда откройте его. Это важно!")
            print()
        else:
            print("Некорректный ввод! Программа будет завершена!")
            print()
            break
