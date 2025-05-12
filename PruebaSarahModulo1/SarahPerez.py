print("\n===  Bienvenido al registro de inventario  ===")
print("\nPara iniciar debes ingresar como minimo 5 productos al inventario: \n")

inventory = {}


product1 = input("1. Ingrese el nombre del primer producto:\n>")
price1 = int(input(f"Ingrese el precio de {product1}\n>"))
amount1 = int(input(f"Ingrese la cantidad de {product1}:\n>"))

inventory[product1] = (price1, amount1)

product2 = input("\n2. Ingrese el nombre del segundo producto:\n>")
price2 = int(input(f"Ingrese el precio de {product2}\n>"))
amount2 = int(input(f"Ingrese la cantidad de {product2}:\n>"))

inventory[product2] = (price2, amount2)

product3 = input("\n3. Ingrese el nombre del tercer producto:\n>")
price3 = int(input(f"Ingrese el precio de {product3}\n>"))
amount3 = int(input(f"Ingrese la cantidad de {product3}:\n>"))

inventory[product3] = (price3, amount3)

product4 = input("\n4. Ingrese el nombre del cuarto producto:\n>")
price4 = int(input(f"Ingrese el precio de {product4}\n>"))
amount4 = int(input(f"Ingrese la cantidad de {product4}:\n>"))

inventory[product4] = (price4, amount4)

product5 = input("\n5. Ingrese el nombre del quinto producto:\n>")
price5 = int(input(f"Ingrese el precio de {product5}\n>"))
amount5 = int(input(f"Ingrese la cantidad de {product5}:\n>"))

inventory[product5] = (price5, amount5)

products = product1, product2, product3, product4, product5
prices = product1, product2, product3, product4, product5
quantities = product1, product2, product3, product4, product5



def add_product():
    product_name = input("\n-Ingrese el nombre del producto:\n>").lower()
    if product_name in inventory:
        print("El producto ingresado ya existe, intente nuevamente\n")
        return

    try:

        product_price = float(input(f"Ingrese el precio de {product_name}:\n>"))
        amount_product = int(input(f"Ingrese la cantidad de {product_name}:\n>"))
    except ValueError:
        print("\nDato ingresado no valido, debe ingresar solo numeros\n")
        return

    print(f"\nEl producto {product_name} fue añadido con exito al inventario\n")

    inventory [product_name] = (product_price, amount_product)
    


def product_search():
    product_name = input("Ingrese el nombre del producto que desea buscar:\n>")
    product = inventory.get(product_name)

    if product:
        print(f"Precio del producto: {product[0]}")
        print(f"Cantidad del producto: {product[1]}\n")
    else:
        print("\nEl producto consultado no existe en el inventario, intente nuevamente\n")



def update_product_price():
    product_name = input("Ingrese el nombre del producto a actualizar:\n>").lower()

    if product_name in inventory:
        try:
            new_price = int(input(f"Ingrese el nuevo precio de {product_name}:\n>"))
            print("\nEl precio del producto fue actualizado con exito\n")
        except ValueError:
            print("\nDato ingresado no valido, debe ingresar solo numeros\n")
            return
        
        _,product_quantity = inventory[product_name]
        inventory[product_name] = [new_price]
    else:
        print("\nEl nombre del producto ingresado no existe en el inventario, intente nuevamente\n")



def delete_product():
    product_name = input("Ingrese el nombre del producto que desea eliminar del inventario:\n>")

    if product_name in inventory:
        del inventory[product_name]
        print(f"\nEl producto {product_name}, fue eliminado del inventario con exito\n")
    else:
        print("\nEl nombre del producto ingresado no existe en el inventario, intente nuevamente\n")



def calculate_total_value():
    calculate =  lambda inv: sum(product_price * product_quantity for product_price, product_quantity in inv.values())
    result = calculate(inventory)
    print(f"El valor total del inventario es: {result}")



def menu():
    while True:
        print("\nMenu de opciones a consultar\n")
        print("1. Añadir más productos al inventario")
        print("2. Buscar producto en el inventario")
        print("3. Actualizar precio de producto en el inventario")
        print("4. Eliminar producto del inventario")
        print("5. Calcular valor total del inventario")
        print("6. Ver inventario completo")
        print("7. Salir del programa\n")
    
    
        option = input("Seleccione la opcion que desea consultar o implementar:\n>")

        if option == "1":
            add_product()
        elif option == "2":
            product_search()
        elif option == "3":
            update_product_price()
        elif option == "4":
            delete_product()
        elif option == "5":
            calculate_total_value()
        elif option == "6":
            print("Inventario")
            for product, data in inventory.items():
                print(f"{product}, precio: {data[0]}, cantidad: {data[1]} ")
        elif option == "7":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion ingresada no valida, intente nuevamente\n")



menu()
