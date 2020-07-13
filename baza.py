products_file = open('shopping_list.txt', encoding='windows-1251')
products = products_file.read()
products = products.replace('сало\n', '').title()
products_file.close()

new_shopping_list = open('new_shopping_list.txt', 'w')
new_shopping_list.write(products)
new_shopping_list.close()
