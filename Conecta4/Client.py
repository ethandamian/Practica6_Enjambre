import pygame
from network import Network
from Button import Button

pygame.font.init()

width = 700  # Adjusted for Connect 4 grid (7 columns)
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect 4")
reiniciar_activado = False
reset = Button("Reiniciar", 285, 520, (128, 128, 0), 120, 50, 10)


def redraw_window(win, game):
    win.fill((255, 255, 255))

    board = game.get_board()

    # Draw Connect 4 grid
    for r in range(6):
        for c in range(7):
            color = (0, 0, 0)  # Default empty color
            if board[r][c] == "R":
                color = (255, 0, 0)  # Red player
            elif board[r][c] == "AI":
                color = (0, 0, 255)  # Yellow AI
            pygame.draw.circle(win, color, (c * 100 + 50, r * 100 + 50), 40)

    # Display winner
    if game.check_winner():
        font = pygame.font.SysFont("comicsans", 40)
        if game.winner == "Tie":
            text = font.render("Empate!", 1, (0, 0, 0))
        else:
            text = font.render("Ganador: " + game.winner, 1, (0, 0, 0))

        win.blit(text, (width / 2 - text.get_width() /
                 2, height / 2 - text.get_height() / 2))

        global reiniciar_activado
        reset.draw(win, 30)
        reiniciar_activado = True

        pygame.display.update()
        pygame.time.delay(2000)
    else:
        reiniciar_activado = False

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = n.getP()  # Player color (R for red, Y for yellow)
    print("You are player", player)

    while run:
        clock.tick(60)

        try:
            game = n.send("get")  # Get the latest game state
        except:
            run = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # Get the (x, y) position of the mouse click
                # We're only interested in the x-coordinate for columns
                x = pos[0]
                column = x // 100  # Assuming each column is 100 pixels wide
                # Make sure the column is valid (0 to 6)
                if column >= 0 and column < 7:
                    n.send(str(column))  # Send the column index to the server

            if reiniciar_activado:
                pos = pygame.mouse.get_pos()
                if reset.click(pos):
                    n.send("reset")  # Reset the game if clicked

        redraw_window(win, game)


main()
