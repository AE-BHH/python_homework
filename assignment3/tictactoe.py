class TictactoeException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        rows = []

        for row in self.board_array:
            rows.append(" | ".join(row))
        return "\n---------\n".join(rows)
    
    def move(self, move_string):
        move_mapping = {
            "upper left": (0, 0),
            "upper center": (0, 1),
            "upper right": (0, 2),
            "middle left": (1, 0),
            "center": (1, 1),
            "middle right": (1, 2),
            "lower left": (2, 0),
            "lower center": (2, 1),
            "lower right": (2, 2),
        }

        if move_string not in move_mapping:
           raise TictactoeException("That's not a valid move.")
        row, col = move_mapping[move_string]

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        
        self.board_array[row][col] = self.turn
        self.last_move = (row, col)
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        lines = []

        for i in range(3):
            lines.append(self.board_array[i])
            lines.append([self.board_array[0][i],
                          [self.board_array[1][i]],
                          [self.board_array[2][i]]])
        lines.append([self.board_array[0][0], self.board_array[1][1], self.board_array[2][2]])
        lines.append([self.board_array[0][2], self.board_array[1][1], self.board_array[2][0]])

        for line in lines:
            if line == ["X", "X", "X"]:
                return (True, "X won!")
            elif line == ["O", "O", "O"]:
                return (True, "O won!")
            
        full = all(cell != " " for row in self.board_array for cell in row)
        if full:
            return (True, "Cat's Game")
        return (False, f"{self.turn}'s turn")
            

print(Board.valid_moves)    
board = Board()

while True:
    print("\nCurrent board:")
    print(board)
        
        # Check game state
    game_over, status = board.whats_next()
    if game_over:
        print("\nGame over!")
        print(status)
        break
    else:
        print(f"\n{status}")

    move_input = input("Enter your move: ").strip().lower()

    try:
        board.move(move_input)
    except TictactoeException as e:
        print(f"Error: {e.message}")


