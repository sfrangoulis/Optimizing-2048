import random
from copy import deepcopy
class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_positions:
            i, j = random.choice(empty_positions)
            self.board[i][j] = 4 if random.randint(0, 9) == 0 else 2

    def move(self, direction):
        previous_state = [row[:] for row in self.board]
        if direction == 'w':
            self.move_up()
        elif direction == 's':
            self.move_down()
        elif direction == 'a':
            self.move_left()
        elif direction == 'd':
            self.move_right()
        else:
            print("Invalid direction! Use 'w', 'a', 's', or 'd'.")
        if self.board != previous_state:
            self.add_random_tile()
        

    def move_left(self):
        for row in range(4):
            self.compress_row(row)
            self.merge_row(row)
            self.compress_row(row)

    def move_right(self):
        for row in range(4):
            self.reverse_row(row)
            self.compress_row(row)
            self.merge_row(row)
            self.compress_row(row)
            self.reverse_row(row)

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def compress_row(self, row):
        new_row = [value for value in self.board[row] if value != 0]
        new_row += [0] * (4 - len(new_row))
        self.board[row] = new_row

    def merge_row(self, row):
        for col in range(3):
            if self.board[row][col] == self.board[row][col + 1] and self.board[row][col] != 0:
                self.board[row][col] *= 2
                self.board[row][col + 1] = 0
                



    def reverse_row(self, row):
        self.board[row] = self.board[row][::-1]

    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
                if i < 3 and self.board[i][j] == self.board[i + 1][j]:
                    return False
                if j < 3 and self.board[i][j] == self.board[i][j + 1]:
                    return False
        return True


    def is_state_unchanged(self, other):
        return self.board == other.board

    def non_zero_count(self):
        return sum(1 for row in self.board for value in row if value != 0)

    def high_score(self):
        return max(max(row) for row in self.board)

    def check_move(self, move):
        simulated_game=self.copy_state()
        simulated_game.move(move)
        return not simulated_game.is_state_unchanged(self)
    
    def copy_state(self):
        new_game = Game2048()
        new_game.board = deepcopy(self.board)
        return new_game

    def display_board(self):
        for row in self.board:
            print("\t".join(str(cell) if cell != 0 else "." for cell in row))
        print("-" * 20)
        
