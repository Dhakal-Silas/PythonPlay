import random

cols=3

def show_board(board):
    for i in range (cols):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2],"|")
        print("-------------")
    
    
    
    
def take_input():
    board = get_whole_board()
    players = ["player1","player2"]
    current_player=random.choice(players)
    

    while True:
        print(f"{current_player}'s turn")
        show_board(board)
        symbol = "X" if current_player == players[0] else "O"
        row = int(input("Enter row number (1, 2 or 3): ")) - 1
        col = int(input("Enter column number (1, 2 or 3): ")) -1
        if board[row][col] != ' ':
            print("Invalid move, please try again")
            continue
        board[row][col] = symbol

        if check_winnings(board, symbol):
            print(f"Player {current_player} wins!")
            break

        if all(box != ' ' for row in board for box in row):
            print("It's a tie!")
            break
        current_player = players[1] if current_player == players[0] else players[0]
    
def get_whole_board():
    board= []
    for _ in range(cols):
        column = [ ' ', ' ', ' '  ]
        board.append(column)
    return board

         
        

def check_winnings(board,symbol):
    for i in range(cols):
        if (board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol):
            return True
        if (board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol):
            return True
    if (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol):
        return True
    if (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
        return True
    return False



    
def main():
    while True:
        is_play_game= input("press enter to play the game and q to quit")
        if is_play_game == 'q':
            break
        else:
            take_input()
            
           
                
                
main()