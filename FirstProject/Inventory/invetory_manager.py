from utils.inventory_utils import load_inventory, save_inventory, display_inventory


def add_product(inventory):
    name = input("Ingrese el nombre del producto: ")
    quantity = int(input("Ingrese la cantidad disponible: "))
    price = float(input("Ingrese el precio unitario: "))

    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    save_inventory(inventory)
    print(f"Producto '{name}' añadido al inventario.")


def update_product(inventory):
    name = input("Ingrese el nombre del producto a actualizar: ")
    for product in inventory:
        if product['name'] == name:
            new_quantity = int(input("Ingrese la nueva cantidad: "))
            new_price = float(input("Ingrese el nuevo precio: "))
            product['quantity'] = new_quantity
            product['price'] = new_price
            save_inventory(inventory)
            print(f"Producto '{name}' actualizado.")
            return
    print(f"Producto '{name}' no encontrado.")


def delete_product(inventory):
    name = input("Ingrese el nombre del producto a eliminar: ")
    for product in inventory:
        if product['name'] == name:
            inventory.remove(product)
            save_inventory(inventory)
            print(f"Producto '{name}' eliminado del inventario.")
            return
    print(f"Producto '{name}' no encontrado.")


def main():
    inventory = load_inventory()

    while True:
        print("\nGestor de Inventario")
        print("1. Mostrar inventario")
        print("2. Añadir producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            update_product(inventory)
        elif choice == '4':
            delete_product(inventory)
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
