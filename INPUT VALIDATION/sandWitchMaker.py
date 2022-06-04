import pyinputplus

prices = {'white': 5.0, 'wheat': 4.0, 'sourdough': 3.0,
          'chicken': 2.0, 'turkey': 2.3, 'hum': 1.0, 'tofu': 3.0,
          'cheddar': 0.5, 'swiss': 0.2, 'mozzarella': 0.4,
          'mayo': 0.5, 'mustard': 0.4, 'lettuce': 0.3, 'Tomato': 0.5}
order = []
total = 0

response = pyinputplus.inputMenu(['white', 'wheat', 'sourdough'], numbered=True, prompt='Choose bread type:\n')
if response is not None:
    order.append(response)
    response = pyinputplus.inputMenu(['chicken', 'turkey', 'hum', 'tofu'], numbered=True, prompt='Choose protein '
                                                                                                 'type: \n')
    if response is not None:
        order.append(response)
        option = pyinputplus.inputYesNo('Do you want Cheese: ')
        if option == 'yes':
            response = pyinputplus.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True, prompt='Choose cheese '
                                                                                                       'type: \n')
            order.append(response)
        option = pyinputplus.inputYesNo('Do you want mayo, mustard, lettuce or tomato?')
        if option == 'yes':
            response = pyinputplus.inputMenu(['mayo', 'mustard', 'lettuce', 'Tomato'], numbered=True, prompt='Choose '
                                                                                                             'one: \n')
            order.append(response)
        amount = pyinputplus.inputInt('How many Sandwitches do you want? ', min=1)

        for i in order:
            total = total + prices[i]

        total = total * amount

        print(f'You will pay {total}$ for {amount} sandwitches which contain {order}.')

else:
    print('An error Occured')

"""
Write a program that asks users for their sandwich preferences. The
program should use PyInputPlus to ensure that they enter valid input,
such as:Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or
mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or
tomato.
Using inputInt() to ask how many sandwiches they want. Make sure
this number is 1 or more.
Come up with prices for each of these options, and have your
program display a total cost after the user enters their selection
"""
