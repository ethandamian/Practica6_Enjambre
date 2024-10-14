import pygame
from network import Network
from Button import Button

pygame.font.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gato")
reiniciar_activado = False
reset = Button("Reiniciar", 185, 420, (128, 128, 0), 120, 50, 10)

def redraw_window(win, game):
    win.fill((255, 255, 255))

    board = game.get_board()

    for i, button in enumerate(buttons):
        button.text = board[i]
        button.draw(win)

    if game.check_winner():
        font = pygame.font.SysFont("comicsans", 40)
        if game.winner == "Tie":
            text = font.render("Empate!", 1, (0, 0, 0))
        else:
            text = font.render("Ganador: " + game.winner, 1, (0, 0, 0))

        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))

        global reiniciar_activado
        reset.draw(win, 30)
        reiniciar_activado = True

        pygame.display.update()
        pygame.time.delay(2000)
    else:
        reiniciar_activado = False

    pygame.display.update()

buttons = [Button("", i % 3 * 100 + 100 + ((10 * i) % 3), i // 3 * 100 + 100+ (2*(i//3)), (182, 149, 192)) for i in range(9)]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = n.getP()
    print("You are player", player)
    while run:
        clock.tick(60)
        
        try:
            game = n.send("get")
        except:
            run = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, button in enumerate(buttons):
                    if button.click(pos) and game.board[i] == "":
                        n.send(str(i))  # Enviar la posición al servidor

            if reiniciar_activado:
                pos = pygame.mouse.get_pos()
                if reset.x <= pos[0] <= reset.x + reset.width and reset.y <= pos[1] <= reset.y + reset.height:
                    n.send("reset")

        redraw_window(win, game)

main()
