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


answer = input('Do you think your player will defeat the master? Yes or No :')


def total(character):
    my_total = 0
    for prop in character_properties[character]:
        my_total += character_properties[character][prop]

    my_total /= 4
    return int(my_total)


def game_round():
    if x > 10:
        print('choose one of these characters')
    for character in character_properties:
        print(character)

    player_choice = input('Enter character name')
    my_total = total(player_choice)
    return (my_total, player_choice)



if answer is "yes":
    average, character_name = game_round()
    if average > 70:
        print(character_name + ' win!')
    elif average == 70:
        print('Try again')
    else:
        print('You Loooooose')
else:
    print("Goodbye!")
