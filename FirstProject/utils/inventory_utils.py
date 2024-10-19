import json
import os

inventory_file = '../datos/inventory.json'

def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as file:
            return json.load(file)
    return []

def save_inventory(inventory):
    with open(inventory_file, 'w') as file:
        json.dump(inventory, file, indent=4)

def display_inventory(inventory):
    if not inventory:
        print("El inventario está vacío.")
    else:
        print("Inventario de productos:")
        for product in inventory:
            print(f"Nombre: {product['name']}, Cantidad: {product['quantity']}, Precio: {product['price']:.2f}")
