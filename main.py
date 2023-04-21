# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

# 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import interface
import func


def main_prog():
    flag = True
    while flag:
        a = interface.hello()
        if a == '1':
            func.add_contact(interface.get_contact())
        elif a == '2':
            func.search_contact()
        elif a == '3':
            func.print_all()
        elif a == '4':
            func.change_contact()
        elif a == '5':
            func.del_contact()
        else:
            flag = False


if __name__ == "__main__":
    main_prog()
