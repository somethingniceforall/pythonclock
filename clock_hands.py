import pygame
import math       

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (42, 42, 42)
RED = (255, 0, 0)


def draw_clock_hands(screen, now):

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
    second_x = math.cos(second_angle) * 120 + 200
    second_y = math.sin(second_angle) * 120 + 200
    if -90 <= second_angle <= 90:
        pygame.draw.line(screen, SECOND_SHADOW_COLOR, (second_x2 + 1, second_y2 + 1), (second_x + 1, second_y + 1), 2)
        pygame.draw.line(screen, SECOND_COLOR, (second_x2, second_y2), (second_x, second_y), 2)
    else:
        pygame.draw.line(screen, SECOND_COLOR, (second_x2 + 1, second_y2 + 1), (second_x + 1, second_y + 1), 2)
        pygame.draw.line(screen, SECOND_SHADOW_COLOR, (second_x2, second_y2), (second_x, second_y), 2)