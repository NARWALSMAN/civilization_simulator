import pygame

class Case:
    def __init__(self, x, y, width, height, color, border_color=(0, 0, 0), border_width=1):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.border_color = border_color
        self.border_width = border_width
    def draw(self, surface):
        pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)
        pygame.draw.rect(surface, self.color, self.rect.inflate(-self.border_width*2, -self.border_width*2))
