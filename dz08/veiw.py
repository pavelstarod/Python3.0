# интерфейс- консоль, выводим и вводим инфо(взаимодействие с пользователем)
# print или input - могут быть только во вью

# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы


commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


def main_menu():
    print('Главное меню: ')
    # enumerate прив к виду ==> 1. Открыть файл
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choice = int(input('Выберите пункт меню: '))
    return choice


def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта. ')
    else:
        print('\t***************************************************')
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print('\t***************************************************')


def create_new_contact():
    name = input('Введите Имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите коментарий: ')
    # вернется кортеж данных
    return name, phone, comment

# def delete(contact: str):
#     result = input(f'Удалить контакт {contact}?(y/n)').lower()
#     if result == 'y':
#         return True
#     else:
#         return False


# def change_contact():


def find_contact():
    find = input('Поиск: ')
    return find


def input_error():
    print('Ошибка ввода.')


def select_contact(messege: str):
    contact = input(messege)
    return contact
