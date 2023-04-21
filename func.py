def add_contact(contact):
    data = open('file.txt', 'a')
    data.writelines(contact)
    data.write('\n')
    data.close()


def search_contact():
    contact_list = open('file.txt', 'r')
    search = input('Введите фамилию или имя для поиска: ')
    for i in contact_list:
        if search.lower() in i.lower():
            print(i)
    contact_list.close()


def print_all():
    contact_list = open('file.txt', 'r')
    num = 1
    for i in contact_list:
        print(f'{num}. {i}')
        num += 1
    contact_list.close()


def change_contact():
    contact_list = open('file.txt', 'r')
    lines = contact_list.readlines()
    contact_list.close()
    change = input('Введите фамилию или имя для изменения контактных данных: ')
    found = False
    for i in range(len(lines)):
        if change.lower() in lines[i].lower():
            print(lines[i])
            new_data = input(
                'Введите новые данные в формате "Фамилия Имя Отчество Телефон": ')
            lines[i] = new_data + '\n'
            print('Данные контакта изменены')
            found = True
            break
    if not found:
        print('Контакт не найден')
    contact_list = open('file.txt', 'w')
    contact_list.writelines(lines)
    contact_list.close()


def del_contact():
    contact_list = open('file.txt', 'r')
    lines = contact_list.readlines()
    contact_list.close()
    contact_list = open('file.txt', 'w')
    search = input('Введите фамилию или имя для удаления данных: ')
    for line in lines:
        if search.lower() not in line.lower():
            contact_list.write(line)
        else:
            print(f"Контактные данные {line.strip()} удалены")
    contact_list.close()
