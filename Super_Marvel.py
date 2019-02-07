player = input('Enter a player name')

print('Hey, ' + player)

player_age = input("what is your age")
x = int(player_age)

if x < 10:
    print('not eligible')
else:
    print('welcome')

#character_name = ['Batman', 'Superman', 'Ironman']
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
for character in character_properties:
    print(character)

player_choice = input('Enter character name ')

def total():
    x = 0
    x = x + character_properties[player_choice]['Strength']
    x = x + character_properties[player_choice]['Weakness']
    x = x + character_properties[player_choice]['Health']
    x = x + character_properties[player_choice]['Fatality']
    x = x / 4
    return x


if total() > 400:
    print('You win!')
elif total() == 400:
    print('Try again')
else:
    print('You Loooooose')
