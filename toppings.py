
requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni', 'green peppers']
available_toppings = ['mushrooms', 'extra cheese','pepperoni']

if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f'Adding {topping}...')
        else:
            print(f"We don't have {topping}")
            
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
