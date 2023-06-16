import pygame
class Cell:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = (255, 255, 255)  # white by default
        self.border_color = (0, 0, 0)  # black border by default
        self.border_width = 2  # 1 pixel border width by default

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
 # Define the grid size and cell size
grid_size = (10, 10)
cell_size = 50
 # Initialize Pygame
import pygame
 # Initialize Pygame
pygame.init()
 # Set up the window
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
 # Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     # Update the display
    pygame.display.flip()
 # Quit Pygame
pygame.quit()