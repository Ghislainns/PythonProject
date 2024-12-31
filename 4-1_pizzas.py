pizzas = ['quattro stagioni', 'margarita','mozzarella']

for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')

print('I really love pizzas')

friend_pizzas = pizzas[:]
pizzas.append('peperoni')
friend_pizzas.append('hawai')

print(pizzas)
print(friend_pizzas)