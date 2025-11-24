new_inventory = []

# Añadir producto.
def add_product():
    flag_temp = True
    flag_initial = True
    while flag_initial:
        while flag_temp:
            name = input("\nEnter the product name -> ")
            if not name.isalnum():
                print("\nInvalid input, Please enter the correct product.")
                continue
            elif any(product["name"].lower() == name.lower() for product in new_inventory):
                print("\nThis product is already registered.")
                continue
            elif name.isalnum():
                break
            else:
                print("\nInlavid input, please enter valid product.")
                continue
        while flag_temp:
            price = input("\nEnter the product price -> ")
            if not price.isnumeric():
                print("\nInvalid input, please enter valid price.")
                continue
            price = float(price)
            if price > 0:
                break
            else:
                print("\nIncorrect price, try again.")
                continue
        while flag_temp:
            quantity = input("\nEnter the quantity products -> ")
            if not quantity.isnumeric():
                print("\nInvalid input, please enter the quantity.")
                continue
            quantity = int(quantity)
            if quantity > 0:
                break
            else:
                print("\nEnter a valid quantity.")
                continue
        new_product = {"name" : name, "price" : price, "quantity" : quantity}
        new_inventory.append(new_product)
        while True:
            again = input("\nAdd more products?\n\n1. Yes.\n2. No.\n\nChoose one option -> ")
            if again == "1":
                break
            elif again == "2":
                flag_initial = False
                break
            elif "2" != again != "1":
                print("\nPlease choose one option.")
                continue
    return new_inventory

# Mostrar inventario.
def print_inventory():
    for product in new_inventory:
        print(f"""
{"=" * 25}
Product: {product["name"].capitalize()}
Price: ${product["price"]:.0f}
quantity: {product["quantity"]:.0f}
{"=" * 25}
""")

# Encontrar producto.
def find_product():
    search_product = input("\nEnter the product name to search -> ")
    for product in new_inventory:
        if product["name"].lower() == search_product.lower():
            print(f"""
{"=" * 25}
The prodct {product["name"].capitalize()} is in the inventory.
{"=" * 25}""")
        else:
            print("\nProduct not found.")

# Actualizar producto.
def update_product():
        while True:
            update_name = input("\nEnter the product name to update -> ")
            if not update_name.isalnum():
                print("\nInvalid input, Please enter the correct product name.")
                continue
            elif update_name.isalnum():
                break
            else:
                print("\nInlavid input, please enter valid product name.")
                continue
        for product in new_inventory:
            while True:
                if product["name"].lower() == update_name.lower():
                    while True:
                        new_price = input("\nEnter the new price -> ")
                        if not new_price.isnumeric():
                            print("\nInvalid input, please enter valid price.")
                            continue
                        new_price = float(new_price)
                        if new_price > 0:
                            product["price"] = new_price
                            break
                        else:
                            print("\nIncorrect price, try again.")
                            continue
                    while True:
                        new_quantity = input("\nEnter the new quantity -> ")
                        if not new_quantity.isnumeric():
                            print("\nInvalid input, please enter valid quantity.")
                            continue
                        new_quantity = int(new_quantity)
                        if new_quantity > 0:
                            product["quantity"] = new_quantity
                            break
                        else:
                            print("\nIncorrect quantity, try again.")
                            continue
                    print(f"\nThe product {update_name.capitalize()} has been updated.")
                    break
                else:
                    print("\nProduct not found.")
                    continue
            break

# Eliminar producto.
def remove_product():
    attemps = 0
    flag_0 = True
    while flag_0:
        remove_name = input("\nEnter the product name to remove -> ")
        flag_1 = False
        for product in new_inventory:
                if product["name"].lower() == remove_name.lower():
                    new_inventory.remove(product)
                    print(f"{"=" * 60}\nThe product '{remove_name.capitalize()}' has been removed from the inventory.\n{"=" * 60}")
                    flag_1 = True
                    break
        if flag_1:
            while True:
                again = input("\nDo you want to remove another product?\n\n1. Yes.\n2. No.\n\nChoose one option -> ")
                if again == "1":
                    break
                elif again == "2":
                    flag_0 = False
                    break
                elif "2" != again != "1":
                    print("\nInvalid option, please choose one option.")
                    continue
        else:
            attemps += 1
            print("\nProduct not found.")
            if attemps >= 2:
                while True:
                    option = input("\nMybe the product is not in the inventory. Try again?\n\n1. Yes.\n2. No.\n\nChoose one option -> ")
                    if option == "1":
                        attemps = 0
                        break
                    elif option == "2":
                        flag_0 = False
                        break
                    else:
                        print("\nPlease choose one option.")
                        continue
    return new_inventory

# Estadísticas del inventario.
def stats_inventory():
    if not new_inventory:
        print("\nInvntory empty, please charge any product.")
    else:
        quantity_list = [product["quantity"] for product in new_inventory]
        sum_quantity = sum(quantity_list)
        prices_list = [product["price"] for product in new_inventory]
        sum_prices = sum(prices_list)
        most_expensive = max(new_inventory, key=lambda p: p["price"])
        max_stock = max(new_inventory, key=lambda q: q["quantity"])
        print(f"""
{("=" * 70)}
Total quantity products: {sum_quantity}.
Total value inventory: ${sum_prices:.0f}.
Most expensive product: {most_expensive["name"].capitalize()} at ${most_expensive["price"]:.0f}.
Max product stock: {max_stock["name"].capitalize()} with {max_stock["quantity"]} units.
{("=" * 70)}
""")

add_product()
stats_inventory()
