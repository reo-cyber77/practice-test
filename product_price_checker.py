products = {'Apple': 20, 'banana': 20, 'orange':15}
product_name = input('Enter product: ')
if product_name in products:
    print(f'Price: {products[product_name]}')
else:
    print('Product not exists')