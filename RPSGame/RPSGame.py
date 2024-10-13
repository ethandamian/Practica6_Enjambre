class RPSGame:
    def __init__(self,id):
        self.player1Moved = False
        self.player2Moved = False
        self.ready = False
        self.id = id
        self.moves = [None,None]
        self.wins = [0,0]
        self.ties = 0
    
    def get_move(self,player):
        """
        Get the move of a player
        :param player: Int of the player to get the move of 
        :return: The move of the player
        """
        return self.moves[player]


    def play(self,player,move):
        self.moves[player] = move
        if player == 0:
            self.player1Moved = True
        else:
            self.player2Moved = True

    def connected(self):
        return self.ready
    
    def both_moved(self):
        return self.player1Moved and self.player2Moved
    
    def winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        

    def reset_moves(self):
        self.player1Moved = False
        self.player2Moved = False