import pygame
import sys
import subprocess
import os

# Initialize Pygame
pygame.init()

# Window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Colors
PINK = (255, 182, 193)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Fonts
pygame.font.init()
TITLE_FONT = pygame.font.SysFont("Arial", 40, bold=True)
BUTTON_FONT = pygame.font.SysFont("Arial", 18, bold=True)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Menu")

# Button sizes
START_WIDTH, START_HEIGHT = 120, 50
EXIT_WIDTH, EXIT_HEIGHT = 50, 50
MARGIN = 20

# Button positions
start_rect = pygame.Rect((WINDOW_WIDTH - START_WIDTH)//2, WINDOW_HEIGHT - 100, START_WIDTH, START_HEIGHT)
exit_rect = pygame.Rect(WINDOW_WIDTH - EXIT_WIDTH - MARGIN, MARGIN, EXIT_WIDTH, EXIT_HEIGHT)

# Path to game script
folder = os.path.dirname(os.path.abspath(sys.argv[0]))
game_path = os.path.join(folder, "openworld3.py")

def start_game():
    if not os.path.isfile(game_path):
        print(f"Cannot find game: {game_path}")
        return
    try:
        # Start the game and wait for it to close
        process = subprocess.Popen([sys.executable, game_path])
        print("Game started, waiting for it to exit...")
        process.wait()  # This blocks until the game closes
        print("Game closed, returning to menu.")
    except Exception as e:
        print(f"Failed to start game: {e}")

# Main loop
running = True
while running:
    screen.fill(PINK)

    # Draw title
    title_surface = TITLE_FONT.render("Game", True, BLACK)
    title_rect = title_surface.get_rect(center=(WINDOW_WIDTH//2, 150))
    screen.blit(title_surface, title_rect)

    # Draw buttons
    mouse_pos = pygame.mouse.get_pos()
    
    # Start button
    start_color = DARK_GREEN if start_rect.collidepoint(mouse_pos) else GREEN
    pygame.draw.rect(screen, start_color, start_rect)
    start_text = BUTTON_FONT.render("Start", True, WHITE)
    start_text_rect = start_text.get_rect(center=start_rect.center)
    screen.blit(start_text, start_text_rect)
    
    # Exit button
    exit_color = DARK_RED if exit_rect.collidepoint(mouse_pos) else RED
    pygame.draw.rect(screen, exit_color, exit_rect)
    exit_text = BUTTON_FONT.render("X", True, WHITE)
    exit_text_rect = exit_text.get_rect(center=exit_rect.center)
    screen.blit(exit_text, exit_text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_rect.collidepoint(event.pos):
                start_game()  # Start game and wait
            elif exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    pygame.display.update()

