groceries = []
for i in range(3):
    products = input(f'{i+1}. ')
    groceries.append(products)

delete = input('\nRemoved: ')
if delete in groceries:
    groceries.remove(delete)
else:
    print("This item isn't in your cart")