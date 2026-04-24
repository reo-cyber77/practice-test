inventory = ['Rice', 'Sugar', 'Milk']
print(f'Inventory: {inventory}')
search = input('Search: ')
if search in inventory:
    print('Available')
else:
    print('Not Available')