import pygame

class Button:
    def __init__(self, text, x, y, color, width=100, height=100, radius=0):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.radius = radius

    def draw(self, win, font_size=60):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), border_radius=self.radius)
        font = pygame.font.SysFont("comicsans", font_size)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        return self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height
