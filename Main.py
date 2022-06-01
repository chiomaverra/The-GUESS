import random


def play():
    possible_action = ['R', 'P', 'S']
    computer = random.choice(possible_action)
    player = input('''Pick a weapon:\n 'R' for rock,\n 'P' for paper,\n 'S' for scissors ''').capitalize()

    while player not in possible_action:
          player = input(''' Invalid Input, Try again: Pick a weapon: 'R' for rock, 'P' for paper, S' for scissors ''').capitalize()

    if player == computer:
        print(f'player ({player}) : CPU ({computer})')
        print("Oops!! Its a tie !")
        print("Lets play again")
        return play()

    elif player == "R":
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("YOU LOSE")
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("YOU WIN !!")

    elif player == "S":
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("YOU LOSE")
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("YOU WIN !")

    elif player == "P":
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("YOU LOSE")
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("YOU WIN !") 
play()