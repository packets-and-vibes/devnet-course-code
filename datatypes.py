favorite_cars = [
    {
        'make': 'Tesla',
        'model': 'Model S',
        'year': 2022, # Number (int)
        'price': 79999.99, # Float
        'features': ['Autopilot', 'Electric', 'All-Wheel Drive'], # List
        'is_electric': True, #Boolean
        'owner': None # None
    },
    {
        'make': 'Porsche',
        'model': '911 Carrera',
        'year': 2023, # Number (int)
        'price': 106500.00, #float
        'features': ['Sport Mode', 'Rear-Wheel Drive', 'Turbocharged'], # List
        'is_electric': False, #Boolean
        'owner': None # None
    }    
]

if favorite_cars == []:
    print("This list is empty")
    print('Please add some items to the list\nThank you')
elif favorite_cars[1]['make'] == 'Porsche':
    print('The second iem is a Porsche')
    print(favorite_cars[1]['make'] + ' ' + favorite_cars[1]['model'])
else:
    print('This list is not empty')
    print(favorite_cars[1]['make'] + ' ' + favorite_cars[1]['model'])