def print_str(data):
    print("                          ВТОРОЙ СПРАВОЧНИК")
    print("-" * 73)
    for i, v in enumerate(data, 1):
        print(f"|   ||     {i}. {v}" + " " * (60 - len(v) - 7) + "||   |")
    print("-" * 73)


def print_list(data):
    print("  ПЕРВЫЙ СПРАВОЧНИК")
    print("-" * 22)
    for i in data:
        if i != '':
            for j in i.split(', '):
                print(f'|| {j}' + " " * (22 - len(j) - 5) + "||")
            print("-" * 22)
            print("-" * 22)
