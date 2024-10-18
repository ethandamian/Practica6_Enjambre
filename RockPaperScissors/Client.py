import pygame
from network import Network
import pickle
pygame.font.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    # Draw the button
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    # Check if the button is clicked
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]

        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win,game, p):
    win.fill((182, 149, 192)) # Fill the window with a color
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("Waiting for Player...", 1, (255,0,0))
        win.blit(text, (width/2 - text.get_width()/2, height/3 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Your Move", 1, (0,0,0))
        win.blit(text, (80, 200))

        text = font.render("IA", 1, (0,0,0))
        win.blit(text, (280, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0,0,0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0,0,0))
            else:
                text1 = font.render("Waiting...", 1, (0,0,0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0,0,0))
            else:
                text2 = font.render("Waiting...", 1, (0,0,0))

        if p == 1:
            win.blit(text2, (100, 250))
            win.blit(text1, (280, 250))
        else:
            win.blit(text1, (100, 250))
            win.blit(text2, (280, 250))

    for button in buttons:
        button.draw(win)

    pygame.display.update()


buttons = [Button("Rock", 20, 370, (0,0,0)), Button("Scissors", 180, 370, (255,0,0)), Button("Paper", 340, 370, (0,255,0))]




def main():
    run = True
    clock = pygame.time.Clock() # To control the frame rate of the game
    n = Network()
    print("Player: ", n.getP()) 
    player = int(n.getP()) # Get the id of the player
    print("You are player", player)
    while run:
        clock.tick(60) # 60 frames per second
        try:
            game = n.send("get") # Get the game from the server
        except: # The game doesn't exist
            run = False
            print("Couldn't get the game")
            break

        if game.bothWent(): # If both players have made a move
            redrawWindow(win, game, player)
            pygame.time.delay(500) # Delay of 500 milliseconds
            try:
                game = n.send("reset") # Reset the game
            except:
                run = False
                print("Couldn't get the game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (255,0,0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255,0,0))
            else:
                text = font.render("You Lost...", 1, (255,0,0))

            win.blit(text, (round(width/2) - round(text.get_width()/2), round(height/2) - round(text.get_height()/2)))
            pygame.display.update()
            pygame.time.delay(2000) # Delay of 2000 milliseconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(button.text)
                        else:
                            if not game.p2Went:
                                n.send(button.text)

        redrawWindow(win, game, player)

main()