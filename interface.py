def hello():
    print("Добро пожаловать!\n1. Для добавления контакта введите 1" +
          "\n2. Для поиска контакта введите 2\n3. Для просмотра справочника введите 3\n4. Для изменения данных введите 4" +
          "\n5. Для удаления данных введите 5\n6. Для выхода из программы введите 0")
    a = input()
    return a


def get_contact():
    return [input('Введите фамилию: ')+" ", input('Введите имя: ')+" ", input('Введите отчество: ')+" ", input('Введите телефон: ')]


# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
