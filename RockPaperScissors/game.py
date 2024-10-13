class Game:
    def __init__(self, id):
        self.p1Went = False # Player 1 has not made a move
        self.p2Went = False # Player 2 has not made a move
        self.ready = False # Game is not ready to start
        self.id = id # Game ID
        self.moves = [None, None] # Moves of both players
        self.wins = [0, 0] # Wins of both players
        self.ties = 0 # Ties

    # Get the move of a player
    def get_player_move(self, p):
        return self.moves[p]
    
    # Update the move of a player
    def player(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True # Player 1 has made a move
        else:
            self.p2Went = True # Player 2 has made a move

    # Check if the 2 players are connected
    def connected(self):
        return self.ready
    
    def bothWent(self):
        return self.p1Went and self.p2Went
    
    def winner(self):
        p1 = self.moves[0].upper()[0] # Get the first letter of the move of player 1
        p2 = self.moves[1].upper()[0] # Get the first letter of the move of player 2
        
        winner = -1
        if p1 == 'R' and p2 == 'S':
            winner = 0
        elif p1 == 'S' and p2 == 'R':
            winner = 1
        elif p1 == 'P' and p2 == 'R':
            winner = 0
        elif p1 == 'R' and p2 == 'P':
            winner = 1
        elif p1 == 'S' and p2 == 'P':
            winner = 0
        elif p1 == 'P' and p2 == 'S':
            winner = 1

        return winner
    
    def resetWent(self):
        self.p1Went = False
        self.p2Went = False