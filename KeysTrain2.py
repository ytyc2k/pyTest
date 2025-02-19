import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Key Matching with Ball")

# Color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font settings
font = pygame.font.SysFont(None, 48)

# Available keys for matching
available_keys = ['1', '2', '3', 'f', 'a', 'b', 'c']

# Initial key to be displayed
current_key = ''

# Function to pick a new random key for matching
def new_random_key():
    return random.choice(available_keys)

# Function to draw the red ball and display the key inside it
def draw_ball_and_key(key):
    # Draw a red ball in the center of the screen
    pygame.draw.circle(screen, RED, (300, 150), 50)  # Center at (300, 150) with radius 50
    # Render the key inside the ball
    text_surface = font.render(key, True, WHITE)  # White color for the text inside the ball
    text_rect = text_surface.get_rect(center=(300, 150))  # Center the text inside the ball
    screen.blit(text_surface, text_rect)

# Function to handle key match checking
def key_match(key, alt_pressed):
    global current_key
    if alt_pressed and key == current_key:
        print("Correct!")
    else:
        print("Incorrect!")
    # Pick a new random key for the next round
    current_key = new_random_key()

# Main program
def main():
    global current_key
    clock = pygame.time.Clock()
    running = True
    alt_pressed = False

    # Pick a random initial key
    current_key = new_random_key()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                    alt_pressed = True  # ALT key pressed

                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_f, pygame.K_a, pygame.K_b, pygame.K_c]:
                    # Check if ALT + key is pressed
                    key_match(chr(event.key), alt_pressed)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                    alt_pressed = False  # Release ALT key

        # Update the screen
        screen.fill(WHITE)
        draw_ball_and_key(current_key)  # Draw the ball with the current key inside it

        pygame.display.update()

        clock.tick(60)  # Set frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
