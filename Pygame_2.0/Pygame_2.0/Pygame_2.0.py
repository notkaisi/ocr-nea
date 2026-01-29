#PYGAME
import os
print('starting')
import pygame
print('pygame imported')
pygame.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Working directory:", os.getcwd())
(os.path.abspath(__file__))

window_width, window_height = 1200, 720
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('game')

# Colors
pink = (255, 182, 193)
black = (0, 0, 0)
green = (0, 200, 0)
dgreen = (0, 150, 0)
red = (255, 0, 0)
dred = (200, 0, 0)
white = (255, 255, 255)

#plain surface
surf = pygame.Surface((100,200))
surf.fill(white)
x=100
y=150


#importing an image
sprite = pygame.image.load('../image_files/player.png').convert_alpha()

running = True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    #background
    screen.fill(pink)
    x+= 0.1
    screen.blit(sprite, (x,y))
    pygame.display.update()

pygame.quit()
