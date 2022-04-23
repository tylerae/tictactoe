import json

def display_board(board):
    blankboard="""
    ___________________
    |     |     |     |
    |  1  |  2  |  3  |            
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    """
    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankboard = blankboard.replace(str(i), board[i])
        else:
            blankboard = blankboard.replace(str(i), ' ')
    print(blankboard)
    
def save_it(board):
    out_file = open("saved_game.json", "w") 
    
    json.dump(board, out_file, indent = 6) 
    
    out_file.close()

def display_sample():
    sample_board="""
    ___________________
    |     |     |     |
    |  1  |  2  |  3  |            
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    """
    print(sample_board)