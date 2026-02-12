import pygame
import os
from os import walk
print('starting')
print('pygame imported')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Working directory:", os.getcwd())
(os.path.abspath(__file__))

window_width, window_height = 1200, 720
tile_size=64

# colors
pink = (255, 182, 193)
black = (0, 0, 0)
green = (0, 200, 0)
darkgreen = (0, 150, 0)
red = (255, 0, 0)
darkred = (200, 0, 0)
white = (255, 255, 255)

