import pygame
import time

# Initialize pygame
pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Key Control for Ball Movement")

# Font settings
try:
    # Try to load a font that supports Chinese characters (replace this with an appropriate font file)
    font = pygame.font.Font("simhei.ttf", 48)  # Use your own font file that supports Chinese characters
    text_font = pygame.font.Font("simhei.ttf", 24)
except FileNotFoundError:
    # If the font file is not found, fallback to default system font
    font = pygame.font.SysFont(None, 48)
    text_font = pygame.font.SysFont(None, 24)

# Color settings
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Initial ball position
ball_x = 300
ball_y = 200

# Key pressed message
current_key = ""

# Ball movement actions based on key press
def ball_action(key):
    global ball_x, ball_y, current_key  # Declare as global so it can be modified outside
    if key == '1':  # ALT+1: Up
        ball_y -= 10
    elif key == '2':  # ALT+2: Down
        ball_y += 10
    elif key == '3':  # ALT+3: Left
        ball_x -= 10
    elif key == '4':  # ALT+4: Right
        ball_x += 10
    elif key == 'f':  # ALT+F: Diagonal up-right
        ball_x += 10
        ball_y -= 10
    elif key == 'd':  # ALT+D: Diagonal down-right
        ball_x += 10
        ball_y += 10
    elif key == 's':  # ALT+S: Diagonal down-left
        ball_x -= 10
        ball_y += 10
    elif key == 'a':  # ALT+A: Diagonal up-left
        ball_x -= 10
        ball_y -= 10

    # Limit the ball to stay within screen boundaries
    ball_x = max(30, min(ball_x, 570))  # Prevent ball from going off the left/right edges
    ball_y = max(30, min(ball_y, 370))  # Prevent ball from going off the top/bottom edges

    current_key = key  # Store the key combination for display

# Function to display text
def show_text(text, color, y_offset=0, font=text_font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(300, 100 + y_offset))  # Display text at the top
    screen.blit(text_surface, text_rect)

# Function to display key combination on the ball
def show_key_on_ball(key):
    text_surface = font.render(key, True, BLACK)
    text_rect = text_surface.get_rect(center=(ball_x, ball_y))  # Place text at the center of the ball
    screen.blit(text_surface, text_rect)

# Main program
def main():
    global ball_x, ball_y, current_key  # Declare as global to modify across the program
    clock = pygame.time.Clock()
    running = True

    # Flag to check if ALT key is pressed
    alt_pressed = False

    # Draw a static ball initially
    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, (ball_x, ball_y), 30)
    pygame.display.update()

    # Instruction texts
    instructions = [
        "Key Controls for Ball Movement:",
        "ALT+1: Up",
        "ALT+2: Down",
        "ALT+3: Left",
        "ALT+4: Right",
        "ALT+F: Diagonal Up-Right",
        "ALT+D: Diagonal Down-Right",
        "ALT+S: Diagonal Down-Left",
        "ALT+A: Diagonal Up-Left"
    ]

    # Scrolling mechanism setup
    scroll_offset = 0
    scroll_speed = 2  # How fast the text scrolls

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                    alt_pressed = True  # ALT key pressed

                if alt_pressed:
                    if event.key == pygame.K_1:  # ALT + 1: Up
                        ball_action('1')
                    elif event.key == pygame.K_2:  # ALT + 2: Down
                        ball_action('2')
                    elif event.key == pygame.K_3:  # ALT + 3: Left
                        ball_action('3')
                    elif event.key == pygame.K_4:  # ALT + 4: Right
                        ball_action('4')
                    elif event.key == pygame.K_f:  # ALT + F: Diagonal Up-Right
                        ball_action('f')
                    elif event.key == pygame.K_d:  # ALT + D: Diagonal Down-Right
                        ball_action('d')
                    elif event.key == pygame.K_s:  # ALT + S: Diagonal Down-Left
                        ball_action('s')
                    elif event.key == pygame.K_a:  # ALT + A: Diagonal Up-Left
                        ball_action('a')

                # Release ALT key
                if event.type == pygame.KEYUP and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
                    alt_pressed = False

        # Update screen after key press and redraw the ball
        screen.fill(WHITE)  # Clear the screen
        pygame.draw.circle(screen, YELLOW, (ball_x, ball_y), 30)  # Redraw the ball

        # Display the key pressed on the ball
        show_key_on_ball(current_key)

        # Scroll the instruction text
        if scroll_offset < -len(instructions) * 40:
            scroll_offset = 0  # Reset scrolling when all text has scrolled
        else:
            scroll_offset -= scroll_speed  # Scroll upwards

        # Display the instructions (scrolling)
        for i, instruction in enumerate(instructions):
            show_text(instruction, BLACK, i * 40 + scroll_offset)

        pygame.display.update()

        clock.tick(60)  # Set frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
