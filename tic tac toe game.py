__name__ = 'tic_tac_toe_game'
import math
from IPython.core.display_functions import clear_output


def display_board(argss):
    """
    Displays gaming board

    Args: Board position

    Returns:
        gaming board
    """

    row_1 = [argss[0], argss[1], argss[2]]
    row_2 = [argss[3], argss[4], argss[5]]
    row_3 = [argss[6], argss[7], argss[8]]
    print(row_1)
    print(row_2)
    print(row_3)

def user_choice():
    """
    Takes users input
    :return: tic tac toe coordinates
    """
    choice_x = 'Wrong'
    choice_y = 'Haha'
    choice_str = False

    while choice_str == False:
        choice_x = input('Please specify x position 0-2 ')
        choice_y = input('Please specify y position 0-2 ')
        if choice_x.isdigit() == False:
            return print('Please specify correct number x position between 0-2')
        if choice_y.isdigit() == False:
            return print('Please specify correct number y position between 0-2')
        if choice_x.isdigit() == True and choice_y.isdigit() == True:
            if int(choice_x) not in range(-1, 3):
                return print('Please specify correct position between 0-2')
            if int(choice_y) not in range(-1, 3):
                return print('Please specify correct y position')
            if int(choice_x) in range(-1, 3) and int(choice_y) in range(-1, 3):
                choice_str = True
            else:
                choice_str = False
    print('x: ', choice_x, 'y: ', choice_y)
    return int(choice_x), int(choice_y)



def game(x):
    if i % 2 == 0:
        if x[0] == 0:
            argss[x[1]] = 'X'

        if x[0] == 1:
            argss[x[1]+4] = 'X'

        if x[0] == 2:
            argss[x[1]+6] = 'X'
        return argss

    if i % 2 != int:
        if x[0] == 0:
            argss[x[1]] = 'O'

        if x[0] == 1:
            argss[x[1]+4] = 'O'

        if x[0] == 2:
            argss[x[1]+6] = 'O'
        return argss





#game_on = True

#coordinates = (user_choice())
#print(coordinates)
#while game_on == True:
argss = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
i = 0
game_on = True
while game_on == True:
    i += 1
    coordinates_of_iser = []
    clear_output()
    display_board(argss)
    coordinates_of_iser = user_choice()
    argss = game(coordinates_of_iser)


