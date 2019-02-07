player = input('Enter a player name')

print('Hey, ' + player)

player_age = input("what is your age")
x = int(player_age)

if x < 10:
    print('not eligible')
else:
    print('welcome')

character_name = ['Batman', 'Superman', 'Ironman']
character_properties = {
    'Batman': {
        'Strength': 100,
        'Weakness': 50,
        'Health': 80,
        'Fatality': 90
    },
    'Superman': {
        'Strength': 100,
        'Weakness': 80,
        'Health': 90,
        'Fatality': 90
    },
    'Ironman': {
        'Strength': 100,
        'Weakness': 95,
        'Health': 70,
        'Fatality': 85
    }
}

if x > 10:
    print('choose one of these characters')

for 