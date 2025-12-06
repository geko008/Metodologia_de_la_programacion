"""
Universidad Politécnica de Victoria
Materia: Metodología de la Programación
Grupo: IM-03
Alumno: Guillen Segura Africa Citlali
Matrícula: 2530275
Proyecto: CRUD en Python :)
Fecha: 5 de diciembre del 2025
Profesor: Carlos Antonio Tovar García
"""

EXIT_OPTION = 0
CREATE_OPTION = 1
READ_OPTION = 2
UPDATE_OPTION = 3
DELETE_OPTION = 4
LIST_OPTION = 5

def create_item(data_store, item_id, name, price, quantity):
    if not str(item_id).strip():
        print("Error: invalid input")
        return False
    if item_id in data_store:
        print("Error: invalid input")
        return False
    try:
        price_val = float(price)
        quantity_val = int(quantity)
        if price_val < 0 or quantity_val < 0:
            print("Error: invalid input")
            return False
    except Exception:
        print("Error: invalid input")
        return False
    data_store[item_id] = {"name": str(name), "price": price_val, "quantity": quantity_val}
    print("Item created")
    return True

def read_item(data_store, item_id):
    if not str(item_id).strip():
        print("Error: invalid input")
        return None
    item = data_store.get(item_id)
    if item is None:
        print("Item not found")
        return None
    print("Items list:")
    print(f"ID: {item_id} | Name: {item['name']} | Price: {item['price']} | Quantity: {item['quantity']}")
    return item

def update_item(data_store, item_id, new_name, new_price, new_quantity):
    if not str(item_id).strip():
        print("Error: invalid input")
        return False
    if item_id not in data_store:
        print("Item not found")
        return False
    try:
        price_val = float(new_price)
        quantity_val = int(new_quantity)
        if price_val < 0 or quantity_val < 0:
            print("Error: invalid input")
            return False
    except Exception:
        print("Error: invalid input")
        return False
    data_store[item_id] = {"name": str(new_name), "price": price_val, "quantity": quantity_val}
    print("Item updated")
    return True

def delete_item(data_store, item_id):
    if not str(item_id).strip():
        print("Error: invalid input")
        return False
    if item_id not in data_store:
        print("Item not found")
        return False
    del data_store[item_id]
    print("Item deleted")
    return True

def list_items(data_store):
    print("Items list:")
    if not data_store:
        print("(no items)")
        return []
    for k, v in data_store.items():
        print(f"ID: {k} | Name: {v['name']} | Price: {v['price']} | Quantity: {v['quantity']}")
    return list(data_store.items())

def print_menu():
    print("\n--- Inventory CRUD Menu ---")
    print(f"{CREATE_OPTION}) Create item")
    print(f"{READ_OPTION}) Read item by id")
    print(f"{UPDATE_OPTION}) Update item by id")
    print(f"{DELETE_OPTION}) Delete item by id")
    print(f"{LIST_OPTION}) List all items")
    print(f"{EXIT_OPTION}) Exit")

def get_non_empty_input(prompt):
    value = input(prompt).strip()
    if not value:
        return None
    return value

def main():
    data_store = {}
    while True:
        print_menu()
        option_raw = input("Select option: ").strip()
        if not option_raw.isdigit():
            print("Error: invalid input")
            continue
        option = int(option_raw)
        if option not in {EXIT_OPTION, CREATE_OPTION, READ_OPTION, UPDATE_OPTION, DELETE_OPTION, LIST_OPTION}:
            print("Error: invalid input")
            continue

        if option == EXIT_OPTION:
            print("Exiting...")
            break

        if option == CREATE_OPTION:
            item_id = get_non_empty_input("Enter id: ")
            if item_id is None:
                print("Error: invalid input")
                continue
            name = get_non_empty_input("Enter name: ")
            if name is None:
                print("Error: invalid input")
                continue
            price = input("Enter price: ").strip()
            quantity = input("Enter quantity: ").strip()
            create_item(data_store, item_id, name, price, quantity)

        elif option == READ_OPTION:
            item_id = get_non_empty_input("Enter id to read: ")
            if item_id is None:
                print("Error: invalid input")
                continue
            read_item(data_store, item_id)

        elif option == UPDATE_OPTION:
            item_id = get_non_empty_input("Enter id to update: ")
            if item_id is None:
                print("Error: invalid input")
                continue
            if item_id not in data_store:
                print("Item not found")
                continue
            name = get_non_empty_input("Enter new name: ")
            if name is None:
                print("Error: invalid input")
                continue
            price = input("Enter new price: ").strip()
            quantity = input("Enter new quantity: ").strip()
            update_item(data_store, item_id, name, price, quantity)

        elif option == DELETE_OPTION:
            item_id = get_non_empty_input("Enter id to delete: ")
            if item_id is None:
                print("Error: invalid input")
                continue
            delete_item(data_store, item_id)

        elif option == LIST_OPTION:
            list_items(data_store)

if __name__ == "__main__":
    main()
