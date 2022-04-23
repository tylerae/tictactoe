import sys
class Input: 

    def __init__(self) -> None:
        pass
        
    def player_input():
        player1 = input("Please pick a marker: 'X' or 'O' ")
        while True:
            if player1.upper() == 'X':
                player2='O'
                print("You've chosen " + player1 + ". Player 2 will be " + player2)
                return player1.upper(),player2
            elif player1.upper() == 'O':
                player2='X'
                print("You've chosen " + player1 + ". Player 2 will be " + player2)
                return player1.upper(),player2
            else:
                player1 = input("Please pick a marker: 'X' or 'O' ")

    def player_choice(board):
        choice = input("Please select an empty space between 1 and 9 : ") 
        possible_choices = ['1' , '2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ]
        
        if choice == "q":
            Input.end_game(choice)
        
        if choice not in possible_choices:
            choice = input("This space isn't valid. Please choose a space between 1 and 9 : ")

        return choice

    def end_game(choice):
        return sys.exit("game save status: ACTIVATED")   
        

    def place_marker(board, marker, position):
        board[position] = marker
        return board

    def space_check(board, position):
        return board[position] == '#'