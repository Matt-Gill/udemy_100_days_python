import random
import my_module

print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 
                     'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 
                     'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine',
                     'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota',
                     'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota',
                     'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

print(states_of_america[0])
print(states_of_america[-1])
states_of_america[1] = 'Pencilvania'
states_of_america.append('Angeland')
states_of_america.extend(['Matt Gill Land', 'Jack Bauer Land'])
print(states_of_america)

print(len(states_of_america))
num_of_states = len(states_of_america)
print(states_of_america[49])
# print(states_of_america[53]) will give an IndexError: list index out of range
# print(states_of_america[num_of_states]) will give an IndexError: list index out of range
print(states_of_america[num_of_states - 1])

dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears',
              'Tomatoes', 'Celery', 'Potatoes']

fruits = ['Strawberries', 'Necratines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

dirty_dozen_new = [fruits, vegetables]
print(dirty_dozen_new)
