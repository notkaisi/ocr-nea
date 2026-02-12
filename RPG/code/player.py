#player
from settings import *
import pygame
class player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../images/player.png').convert_alpha() # add more images too
        self.rect = self.image.get_rect(center = pos)

        #movement
        self.direction = pygame.Vector2()
        self.speed = 300

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
   
    def move(self, dt):
        self.rect.center += self.direction*self.speed*dt

    def update(self, dt):
        self.input()
        self.move(dt)