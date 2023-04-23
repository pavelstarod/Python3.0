# объеденяет veiw и model(в вью данные вводим, в контроллер их обработали, в модель записали в бд\\ или наоборот из модел берем список контактов- передаем во вью, и из вью переводим в консоль)
# связующее звено

import veiw
import model


def start():
    choice = ''
    while choice != 8:
        choice = veiw.main_menu()
        print(choice)

        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                pb = model.get_phone_book()
                veiw.show_contacts(pb)
            case 4:
                new_contact = list(veiw.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                pass
            case 6:
                pass
            case 7:
                find = veiw.find_contact()
                result = model.search_contact(find)
                veiw.show_contacts(result)
            case 8:
                print('Выход из программы. ')
            case _:
                veiw.input_error()
