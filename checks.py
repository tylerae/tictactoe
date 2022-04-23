class Checkit:
    
    def place_marker(board, marker, position):
        board[position] = marker
        return board

    def full_board_check(board):
        return len([x for x in board if x =='#']) == 1

    def win_check(board, mark):
        if board[1] == board[2] == board[3] == mark: # Top row
            return True
        elif board[4] == board[5] == board[6] == mark: # Middle row
            return True
        elif board[7] == board[8] == board[9] == mark: # Bottom row
            return True
        elif board[1] == board[4] == board[7] == mark: # Left column 
            return True
        elif board[2] == board[5] == board[8] == mark: # Middle column
            return True
        elif board[3] == board[6] == board[9] == mark: # Right Column 
            return True
        elif board[1] == board[5] == board[9] == mark: # Diagonal 1
            return True
        elif board[3] == board[5] == board[7] == mark: # Diagonal 2
            return True
        else:
            return False