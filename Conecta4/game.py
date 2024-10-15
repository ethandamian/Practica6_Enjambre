import random


class Game:
    ROWS = 6
    COLS = 7
    SIMULATIONS = 500

    def __init__(self, id):
        self.board = [["" for _ in range(Game.COLS)] for _ in range(
            Game.ROWS)]  # 7x6 grid for Connect 4
        self.winner = None
        self.id = id
        self.turn = 0  # 0 for human, 1 for AI (yellow)

    def get_board(self):
        return self.board

    def available_moves(self, board=None):
        if not board:
            board = self.board
        # Return a list of columns where a move is still possible
        return [c for c in range(Game.COLS) if board[0][c] == ""]

    def make_move(self, player, col):
        # Drop a piece into the selected column
        for row in range(Game.ROWS - 1, -1, -1):
            if self.board[row][col] == "":
                self.board[row][col] = "R" if player == 0 else "AI"
                return True
        return False

    def check_winner(self, board=None):
        if not board:
            board = self.board
        # Check for four in a row (horizontally, vertically, or diagonally)

        def check_direction(start_row, start_col, d_row, d_col):
            piece = self.board[start_row][start_col]
            if piece == "":
                return False
            for i in range(1, 4):
                row = start_row + d_row * i
                col = start_col + d_col * i
                if row < 0 or row >= Game.ROWS or col < 0 or col >= Game.COLS or board[row][col] != piece:
                    return False
            return True

        # Check all grid positions
        for r in range(Game.ROWS):
            for c in range(Game.COLS):
                if (check_direction(r, c, 0, 1) or  # Horizontal
                    check_direction(r, c, 1, 0) or  # Vertical
                    check_direction(r, c, 1, 1) or  # Diagonal right-down
                        check_direction(r, c, 1, -1)):  # Diagonal left-down
                    self.winner = self.board[r][c]
                    return True

        # Check for a tie (board is full)
        if all(self.board[0][c] != "" for c in range(Game.COLS)):
            self.winner = "Tie"
            return True
        return False

    def montecarlo_simulation(self, first_move):
        """
        Given a board state, simulates a game to the end using random moves, and returns 1 if the AI wins, 0 otherwise.
        """
        board = [row[:] for row in self.board]
        turn = self.turn
        winner = None

        # First move
        for row in range(Game.ROWS - 1, -1, -1):
            if board[row][first_move] == "":
                board[row][first_move] = "R" if turn == 0 else "AI"
                turn = 1 if turn == 0 else 0
                break

        if self.check_winner(board):
            winner = self.winner

        while not winner:
            possible_moves = self.available_moves(board)
            if not possible_moves:
                break

            move = random.choice(possible_moves)
            for row in range(Game.ROWS - 1, -1, -1):
                if board[row][move] == "":
                    board[row][move] = "R" if turn == 0 else "AI"
                    turn = 1 if turn == 0 else 0
                    break

            if self.check_winner(board):
                winner = self.winner
                break

        if winner == "AI":
            return 1
        return 0

    def best_move(self):
        """
        Returns the best move for the AI using the MonteCarlo algorithm
        """
        possible_moves = self.available_moves()
        wins = {possible_move: 0 for possible_move in possible_moves}

        for _ in range(self.SIMULATIONS):
            move = random.choice(possible_moves)
            sim_win = self.montecarlo_simulation(move)
            if sim_win:
                wins[move] += 1

        best_move = max(wins, key=wins.get)
        return best_move

    def reset(self):
        self.board = [["" for _ in range(Game.COLS)] for _ in range(Game.ROWS)]
        self.winner = None
        self.turn = 0
