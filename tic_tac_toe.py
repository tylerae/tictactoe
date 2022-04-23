from display import display_board , save_it , display_sample
from handle_input import Input
from checks import Checkit
import json
import sys

def main():
    print('Welcome to Tic Tac Toe!\n')
    resume = input("Would you like to resume a previous game?(y/n): ").lower()
    i = 1
    players = Input.player_input()
    if resume == 'y':
        data = open('saved_game.json')
        board = json.load(data)
    else:
        board = ['#'] * 10
    
   
    while True:
        game_on = Checkit.full_board_check(board)
        print('\nEnter \'q\' to suspend your game. Otherwise, enter a number from 1 to 9 \nwhere the following numbers correspond to the locations on the grid:')
        display_sample()
        display_board(board) 
        while not game_on:
            position = Input.player_choice(board)

            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]

            Input.place_marker(board, marker, int(position))

            display_board(board) 
            save_it(board)

            i += 1
            if Checkit.win_check(board, marker):
                print('You won!')
                with open('saved_game.json', 'w') as data:
                    json.dump('', data, indent=1)
                    print("Previous game data erased")
                break
            game_on = Checkit.full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            players = Input.player_input()
            board = ['#'] * 10 


def replay():
    playagain = input("Do you want to play again (Yes or no)? ")
    if playagain.lower() == "yes":
        return True
    if playagain.lower() == "no":
        return False


main()