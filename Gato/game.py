class Game:
    def __init__(self, id):
        self.board = [""] * 9  # Representación del tablero 3x3
        self.winner = None
        self.id = id
        self.turn = 0  # 0 para el jugador humano, 1 para la IA

    def get_board(self):
        return self.board

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ""]

    def make_move(self, player, pos):
        if self.board[pos] == "":
            self.board[pos] = "X" if player == 0 else "O"
            return True
        return False

    def check_winner(self):
        # Todas las combinaciones ganadoras
        winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "":
                self.winner = self.board[combo[0]]
                return True
        if "" not in self.board:
            self.winner = "Tie"
            return True
        return False

    def minimax(self, is_maximizing):
        if self.check_winner(): # Si hay un ganador
            if self.winner == "O":
                return 1 # La IA gana
            elif self.winner == "X":
                return -1 # El humano gana
            else:
                return 0 # Empate

        if is_maximizing: # Si se está maximizando (turno de la IA) 
            best_score = -float('inf') # Inicializar el mejor puntaje con el peor puntaje posible
            for move in self.available_moves():
                self.board[move] = "O" # Hacer el movimiento
                score = self.minimax(False) # Llamar recursivamente minimax con el turno del humano
                self.board[move] = "" # Deshacer el movimiento
                best_score = max(score, best_score) # Actualizar el mejor puntaje
            return best_score
        else:
            best_score = float('inf') # Inicializar el mejor puntaje con el peor puntaje posible
            for move in self.available_moves():
                self.board[move] = "X"
                score = self.minimax(True)
                self.board[move] = ""
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = -1
        for i in self.available_moves():
            self.board[i] = "O"
            score = self.minimax(False) # Llamar minimax con el turno del humano
            self.board[i] = ""
            if score > best_score:
                best_score = score
                move = i
        return move
    
    def reset(self):
        self.board = [""] * 9
        self.winner = None
        self.turn = 0
