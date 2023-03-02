import pygame
import math
from datetime import datetime

# Set up pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Visual Clock")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (42, 42, 42)
RED = (255, 0, 0)

# Define font
font = pygame.font.SysFont(None, 200)

# Load the background image
background_image = pygame.image.load('pictures/background.jpeg')
background_image = pygame.transform.scale(background_image, (400, 400))



def update_clock(font, background_image):
    
    # Get the current time
    now = datetime.now()
    time_text = font.render(now.strftime("%I:%M:%S %p"), True, WHITE)

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Create a surface for the circle
    circle_surface = pygame.Surface((40, 40), pygame.SRCALPHA)

    # Draw the outer circle
    pygame.draw.circle(circle_surface, WHITE, (20, 20), 10, 3)

    # Draw the inner circle
    pygame.draw.circle(circle_surface, BLACK, (20, 20), 5)

    # Set the color key to make the middle transparent
    circle_surface.set_colorkey(BLACK)

    # Draw the circle on the screen
    screen.blit(circle_surface, (180, 180))

    # Draw the clock face
    pygame.draw.circle(screen, WHITE, (200, 200), 150, 3)

    

    # Define colors for the hands and shadows
    HOUR_COLOR = WHITE
    HOUR_SHADOW_COLOR = GRAY
    MINUTE_COLOR = WHITE
    MINUTE_SHADOW_COLOR = GRAY
    SECOND_COLOR = RED
    SECOND_SHADOW_COLOR = GRAY

    # Draw the hour hand
    hour_angle = math.radians(now.hour * 30 + now.minute * 0.5 - 90)
    hour_x2 = math.cos(hour_angle) * 10 + 200
    hour_y2 = math.sin(hour_angle) * 10 + 200
    hour_x = math.cos(hour_angle) * 70 + 200
    hour_y = math.sin(hour_angle) * 70 + 200
    if -90 <= hour_angle <= 90:
        pygame.draw.line(screen, HOUR_SHADOW_COLOR, (hour_x2 + 1, hour_y2 + 1), (hour_x + 1, hour_y + 1), 10)
        pygame.draw.line(screen, HOUR_COLOR, (hour_x2, hour_y2), (hour_x, hour_y), 10)
    else:
        pygame.draw.line(screen, HOUR_COLOR, (hour_x2 + 1, hour_y2 + 1), (hour_x + 1, hour_y + 1), 10)
        pygame.draw.line(screen, HOUR_SHADOW_COLOR, (hour_x2, hour_y2), (hour_x, hour_y), 10)

    # Draw the minute hand
    minute_angle = math.radians(now.minute * 6 - 90)
    minute_x2 = math.cos(minute_angle) * 10 + 200
    minute_y2 = math.sin(minute_angle) * 10 + 200
    minute_x = math.cos(minute_angle) * 90 + 200
    minute_y = math.sin(minute_angle) * 90 + 200
    if -90 <= minute_angle <= 90:
        pygame.draw.line(screen, MINUTE_SHADOW_COLOR, (minute_x2 + 1, minute_y2 + 1), (minute_x + 1, minute_y + 1), 5)
        pygame.draw.line(screen, MINUTE_COLOR, (minute_x2, minute_y2), (minute_x, minute_y), 5)
    else:
        pygame.draw.line(screen, MINUTE_COLOR, (minute_x2 + 1, minute_y2 + 1), (minute_x + 1, minute_y + 1), 5)
        pygame.draw.line(screen, MINUTE_SHADOW_COLOR, (minute_x2, minute_y2), (minute_x, minute_y), 5)

    # Draw the second hand
    second_angle = math.radians(now.second * 6 - 90)
    second_x2 = math.cos(second_angle) * 10 + 200
    second_y2 = math.sin(second_angle) * 10 + 200
    second_x = math.cos(second_angle) * 110 + 200
    second_y = math.sin(second_angle) * 110 + 200
    if -90 <= second_angle <= 90:
        pygame.draw.line(screen, SECOND_SHADOW_COLOR, (second_x2 + 1, second_y2 + 1), (second_x + 1, second_y + 1), 2)
        pygame.draw.line(screen, SECOND_COLOR, (second_x2, second_y2), (second_x, second_y), 2)
    else:
        pygame.draw.line(screen, SECOND_COLOR, (second_x2 + 1, second_y2 + 1), (second_x + 1, second_y + 1), 2)
        pygame.draw.line(screen, SECOND_SHADOW_COLOR, (second_x2, second_y2), (second_x, second_y), 2)

    # Draw the clock face
    pygame.draw.circle(screen, WHITE, (200, 200), 150, 3)

    # Draw the hour markers
    for i in range(1, 13):
      angle = math.radians(i * 30 - 90)
      x = math.cos(angle) * 130 + 200
      y = math.sin(angle) * 130 + 200
      number_text = font.render(str(i), True, WHITE)
      number_rect = number_text.get_rect(center=(x, y))
      screen.blit(number_text, number_rect)

    # Draw the time text
    screen.blit(time_text, (10, 10))

    # Update the screen
    pygame.display.flip()
    
    


def main():
    # Set up pygame
    pygame.init()

    # Set up the window
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Visual Clock")

    # Set up the font
    font = pygame.font.SysFont(None, 30)

    # Load the background image
    background_image = pygame.image.load('pictures/background.jpeg')
    background_image = pygame.transform.scale(background_image, (400, 400))

    # Set up the clock
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update the clock display
        update_clock(font, background_image)

        # Update the screen
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)



if __name__ == '__main__':
    main()
