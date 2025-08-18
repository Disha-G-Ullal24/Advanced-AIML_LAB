board = [" "] * 9  


def show():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check winner
def check_winner(p):
    # All winning combinations
    wins = [(0,1,2), (3,4,5), (6,7,8),   # rows
            (0,3,6), (1,4,7), (2,5,8),   # columns
            (0,4,8), (2,4,6)]            # diagonals
    
    # Return True if any winning line is filled by player
    return any(all(board[i] == p for i in w) for w in wins)

# Start with player X
player = "X"

# Maximum 9 turns (since 9 cells)
for turn in range(9):
    show()  # Show current board
    move = int(input(f"Player {player}, choose position (0-8): "))

    if board[move] == " ":   # If cell is empty
        board[move] = player  # Place player's symbol

        if check_winner(player):   # Check if player wins
            show()
            print(f"🎉 Player {player} wins!")
            break
        
        # Switch player
        player = "O" if player == "X" else "X"
    else:
        print("Cell already taken! Try again.")

# If loop completes without break → draw
else:
    show()
    print("It's a draw!")
