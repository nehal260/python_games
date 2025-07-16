# Tic Tac Toe Game

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]):
            return True, [(i, j) for j in range(3)]
    
    for j in range(3):
        if all(board[i][j] == symbol for i in range(3)):
            return True, [(i, j) for i in range(3)]
   
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True, [(i, i) for i in range(3)]
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True, [(0,2), (1,1), (2,0)]
    return False, []

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!\n")

    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")

    players = { "X": player1, "O": player2 }
    current_symbol = "X"

    while True:
        print_board(board)
        print(f"{players[current_symbol]}'s Turn ({current_symbol})")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = current_symbol
                won, combo = check_winner(board, current_symbol)
                if won:
                    print_board(board)
                    print(f"🎉 {players[current_symbol]} wins!")
                    print(f"Winning combination: {combo}")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_symbol = "O" if current_symbol == "X" else "X"
            else:
                print("Cell already filled. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column between 0 and 2.")

if __name__ == "__main__":
    play_game()