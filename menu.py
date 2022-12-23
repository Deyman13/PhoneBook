from function import init_dict_ru, init_dict_eng, print_book, write_new_contact_list_ru, write_new_contact_str_ru, replace_contact_list_ru 
from function import replace_contact_str_ru, delete_contact_str_ru, delete_contact_list_ru, clear
from function import write_new_contact_str_eng, write_new_contact_list_eng, replace_contact_list_eng, replace_contact_str_eng
from function import delete_contact_str_eng, delete_contact_list_eng
from inputreplasechange import search_ru, search_eng


def print_hint_ru():
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

def print_hint_eng():
    print('''\n                  
        |====================================================================|
        |         ===>> COMMANDS FOR WORKING WITH THE DIRECTORY <<===        |
        |====================================================================|

        ||-*-*-*-*--------------------------------------------------*-*-*-*-||
        ||                                                                  ||
        ||     Exiting the program: 0 or Enter                             ||
        ||     View all entries of both directories:  - 1                  ||
        ||     Adding a new entry to the string directory: - 2             ||
        ||     Adding a new entry to the list directory: - 3               ||
        ||     Search for the necessary contact by parameters - 4          ||
        ||     Changing an entry from a string directory by data: - 5      ||
        ||     Changing an entry from the list directory by data: - 6      ||
        ||     Deleting an entry from a string data reference: - 7         ||
        ||     Deleting an entry from a list data reference: - 8           ||
        ||     Clearing the terminal - 9                                   ||
        ||                                                                  ||
        ||-*-*-*-*--------------------------------------------------*-*-*-*-||''')


def menu():
    language = input("Выберите язык / Select a language: RU or ENG: ")
    if language.lower() == "ru":
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
                init_dict_ru(book_all, "str")
                init_dict_ru(book_all, "lst")
                dict_command = {'1': print_book, '2': write_new_contact_str_ru,
                                '3': write_new_contact_list_ru, '4': search_ru, '5': replace_contact_str_ru,
                                '6': replace_contact_list_ru, '7': delete_contact_str_ru, '8': delete_contact_list_ru}
                print_hint_ru()
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
                        print_hint_ru()
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
    elif language.lower() == "eng":
        print()
        print("ATTENTION!!!")
        print("PLEASE OPEN THE TERMINAL COMPLETELY FOR CONVENIENT USE OF OUR PROGRAM!!!")
        flag = True
        while flag:
            print()
            ans = input("Have you opened the terminal? Enter YES or NO: ")
            print()
            if ans.lower() == "yes":
                flag = False
                print("                 || ===---===---===---===---===---===---===---=== ||")
                print("                 |-|-|            ENJOY YOUR USE!!! :)         |-|-|")
                print("                 || ===---===---===---===---===---===---===---=== ||")
                book_all = {}
                init_dict_eng(book_all, "str")
                init_dict_eng(book_all, "lst")
                dict_command = {'1': print_book, '2': write_new_contact_str_eng,
                                '3': write_new_contact_list_eng, '4': search_eng, '5': replace_contact_str_eng,
                                '6': replace_contact_list_eng, '7': delete_contact_str_eng, '8': delete_contact_list_eng}
                print_hint_eng()
                while True:
                    print()
                    print("===>> Type help to list commands if you forgot them! <<===")
                    print("===>> To clear the terminal, press 9 <<===")
                    command = input('Command: > ')
                    if command in dict_command:
                        dict_command[command](book_all)
                    elif command == "0" or command == '':
                        print("| ---------------------------------------------------------- |")
                        print("|     YOU HAVE LEFT THE PROGRAM, WE HOPE YOU ENJOYED IT!)    |")
                        print("|                                                            |")
                        print("|    The work was done by Daniel Shklyaev, Boris Lukashenok  |")
                        print("|                                                            |")
                        print("|    Daniel - Backend, Frontend                              |")
                        print("|    Boris - Backend, ProjectManager, MainLogic              |")
                        print("|    All rights reserved © Dec 22, 2022 DanBOR, Inc          |")
                        print("| ---------------------------------------------------------- |")
                        break
                    elif command == "9":
                        clear()
                    elif command.lower() == "help":
                        print_hint_eng()
                    else:
                        print('The command is not recognized, try again')   
            elif ans.lower() == "no":
                print()
                print("Then open it. It is important!")
                print()
            else:
                print("Incorrect input! The program will be completed!")
                print()
                break


