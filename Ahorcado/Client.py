import pygame
from network import Network
from Button import Button


pygame.font.init()

# Dimensiones de la ventana
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ahorcado")

game_over = False
reset = Button((0, 255, 0), 300, 400, 200, 50, "Reiniciar")

# Dibujar el estado actual del juego
def redraw_window(win, game_data):
    win.fill((235, 222, 207)) 
    
    font = pygame.font.SysFont("comicsans", 30)
    
    # Mostrar la palabra oculta
    word_display = " ".join(game_data['word_display'])
    word_text = font.render(word_display, 1, (0, 0, 0))
    win.blit(word_text, (400 - word_text.get_width() // 2, 200))
    
    # Mostrar letras incorrectas
    incorrect_text = font.render(f"Letras incorrectas: {', '.join(game_data['incorrect_letters'])}", 1, (0, 0, 255))
    win.blit(incorrect_text, (50, 500))
    
    # Mostrar intentos restantes
    tries_text = font.render(f"Intentos: {game_data['tries_left']}", 1, (0, 0, 0))
    win.blit(tries_text, (600, 50))

    if game_data['terminated']:
        if game_data['won']:
            result_text = font.render("Ganaste!", 1, (45,106,79))
        else:
            result_text = font.render("Perdiste!", 1, (255, 0, 0))
            result_text2 = font.render("Palabra correcta: " + game_data['word'], 1, (255, 0, 0))
            win.blit(result_text2, (400 - result_text2.get_width() // 2, 350))

        win.blit(result_text, (400 - result_text.get_width() // 2, 300))
        
        global game_over
        game_over = True

        reset.draw(win, (0, 0, 0))

    pygame.display.update()



def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    global game_over

    while run:
        clock.tick(60)
        try:
            game_data = n.send("get")
        except:
            print("No se pudo obtener el estado del juego.")
            run = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and not game_over:
                letter = pygame.key.name(event.key)
                if len(letter) == 1 and letter.isalpha():  # Verificar que solo sea una letra
                    n.send(letter)  # Enviar la letra al servidor

            

            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                pos = pygame.mouse.get_pos()
                if reset.is_over(pos):
                    n.send("reset")
            
            game_over = False
            print(game_over)

        
        redraw_window(win, game_data)

main()
