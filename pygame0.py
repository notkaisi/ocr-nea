#PYGAME
print('starting')
import pygame
print('pygame imported')
pygame.init()

window_width, window_height = 1200, 720
screen = pygame.display.set_mode((window_width,window_height))

running = True

# Colors
pink = (255, 182, 193)
black = (0, 0, 0)
green = (0, 200, 0)
dgreen = (0, 150, 0)
red = (255, 0, 0)
dred = (200, 0, 0)
white = (255, 255, 255)

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    #background
    screen.fill(pink)
    pygame.display.update()

pygame.quit()