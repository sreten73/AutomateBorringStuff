def display_game(game_list):
    print('Here is the current game list')
    print(game_list)

def gameon_choice():
    # This first choice value can be anything that isn't Y or N
    choice = 'wrong'

    #while choice is not a Y or N, keep asking for input
    while choice not in ['Y','N']:

        # Ask if gamer want to keep playing
        choice = input('Would you like to keep playing? Y or N ')

        if choice not in ['Y', 'N', 'n', 'y']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

        if choice.upper() == 'Y':
            return True
        elif choice.upper() in ['N']:
            return False

def position_choice():
    # This first choice value can be anything that isn't Y or N
    choice = 'wrong'

    # while choice is not a Y or N, keep asking for input
    while choice not in ['0', '1','2']:

        # Ask if gamer want to keep playing
        choice = input('Please, pick a position to replace (0,1,2):  ')

        if choice not in ['0', '1', '2']:
            print("Sorry, but you didn't choose a valid position (0,1,2). Try again.")

    return int(choice)

def replacement_choice(game_list, position):

    user_placement = input(f'Type a string to place at the position {position} in game list: ')
    game_list[position] = user_placement

    return game_list


##MAIN PROGRAM
# Variable to keep game playing
game_on = True

# First Game List
game_list = [0,1,2]

while game_on:

    #Show current game list
    display_game(game_list)

    # Player should choose position
    position = position_choice()

    # Rewrite that position and update game list
    game_list = replacement_choice(game_list, position)

    # Display again update game list
    display_game(game_list)

    # Ask if gamer want to keep playing
    game_on = gameon_choice()