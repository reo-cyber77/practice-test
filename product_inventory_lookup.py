inventories = (("P001", "Keyboard", 850),
               ("P002", "Mouse", 450),
               ("P003", "Monitor", 7000))

choose = (input('Enter Product ID:'))
found = False

for product in inventories:
    p_id, name, price = product
    if choose == p_id:
        print('\nProduct Found:')
        print(f'Name: {name}')
        print(f'Price: {price}')
        found = True
        break

if not found:
    print('Product Not Found.')