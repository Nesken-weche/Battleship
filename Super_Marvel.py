player = input('Enter a player name')

print('Hey, ' + player)

player_age = input("what is your age")
x = int(player_age)

if x < 10:
    print('not eligible')
else:
    print('welcome')

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

answer = input('Do you think your player will defeat the master? Yes or No :')

def total():
    my_total = 0
    for property in character_properties[player_choice]:
        my_total += character_properties[player_choice][property]

    my_total /= 4
    return int(my_total)

if answer is "yes":
    if total() > 70:
        print(player_choice + ' win!')
    elif total() == 70:
        print('Try again')
    else:
        print('You Loooooose')
else:
    print("Goodbye!")
