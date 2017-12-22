cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_min = 18
age_max = 26
age = 21

if age >= age_min and age <= age_max:
    print('ok')

age = 30
msg = ''
if age >= age_min and age <= age_max:
    msg = 'student'
elif age < age_min:
    msg = 'teenager'
else:
    msg = 'worker'

print(msg)

if 'audi' in cars:
    print('audi is there')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding: ' + requested_topping)
    else:
        print('Sorry, ' + requested_topping + ' is not available')

