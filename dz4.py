# исходные данные
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_owner_by_doc_number(doc_number: str) -> str:
    """Возвращает имя владельца по номеру документа или None, если не найден."""
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    return None

def get_shelf_by_doc_number(doc_number: str) -> str:
    """Возвращает номер полки, на которой хранится документ."""
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None

def main():
    while True:
        command = input("\nВведите команду (p - владелец, s - полка, q - выход): ").strip().lower()

        if command == 'q':
            print("Программа завершена.")
            break

        elif command == 'p':
            doc_number = input("Введите номер документа: ").strip()
            owner = get_owner_by_doc_number(doc_number)

            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Владелец документа: владелец не найден")

        elif command == 's':
            doc_number = input("Введите номер документа: ").strip()
            shelf = get_shelf_by_doc_number(doc_number)

            if shelf:
                print(f"Документ находится на полке: {shelf}")
            else:
                print("Документ с таким номером не найден.")
                

        else:
            print("Неизвестная команда. Повторите ввод.")


if __name__ == '__main__':
    main()
