# база данных со всей инфой, и функции работы с этой базой
# храним только телефонную книгу и методы работы с ней

# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы


phone_book = []

path = 'data.txt'


def get_phone_book():
    global phone_book
    return phone_book


def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))
    print(phone_book)


def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))


def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)


def search_contact(find: str):
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result


def delete_contact(contact: list):
    global phone_book
    phone_book.remove(contact)
