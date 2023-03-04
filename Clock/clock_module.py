import pygame
import math
from datetime import datetime
import os
import alarm_module
from clock_hands import draw_clock_hands

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (42, 42, 42)
RED = (255, 0, 0)

class Clock:
    def __init__(self, font_size=30, screen_size=(400, 400), background_image='pictures/background.jpeg'):
        # Set up pygame
        pygame.init()
        pygame.display.init()

        # Set up the window with hardware acceleration
        self.screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Visual Clock")

        # Set up the font
        self.font = pygame.font.SysFont(None, font_size)

        # Load the background image
        self.background_image = pygame.image.load(background_image)
        self.background_image = pygame.transform.scale(self.background_image, screen_size)

        # Set up the clock
        self.clock = pygame.time.Clock()

        # Set up the alarm
        self.alarm = alarm_module.Alarm()

    def update_clock(self):
        # Get the current time
        now = datetime.now()
        time_text = self.font.render(now.strftime("%I:%M:%S %p"), True, WHITE)

        # Blit the background image onto the screen
        self.screen.blit(self.background_image, (0, 0))

        # Create a surface for the circle
        circle_surface = pygame.Surface((40, 40), pygame.SRCALPHA)

        # Draw the outer circle
        pygame.draw.circle(circle_surface, WHITE, (20, 20), 10, 3)

        # Draw the inner circle
        pygame.draw.circle(circle_surface, BLACK, (20, 20), 5)

        # Set the color key to make the middle transparent
        circle_surface.set_colorkey(BLACK)

        # Draw the circle on the screen
        self.screen.blit(circle_surface, (180, 180))

        # Draw the clock face
        pygame.draw.circle(self.screen, WHITE, (200, 200), 150, 3)

        # Draw the hands
        draw_clock_hands(self.screen, now)
        
        # Draw the hour markers
        for i in range(1, 13):
             angle = math.radians(i * 30 - 90)
             x = math.cos(angle) * 130 + 200
             y = math.sin(angle) * 130 + 200
             number_text = self.font.render(str(i), True, WHITE)  
             number_rect = number_text.get_rect(center=(x, y))
             self.screen.blit(number_text, number_rect)  


        # Draw the time text
        self.screen.blit(time_text, (10, 10))

        # Draw the alarm time on the screen
        self.alarm.draw_alarm_time(self.screen)

        # Update the screen
        pygame.display.flip()

        # Check if it's time for the alarm to go off
        alarm_time = self.alarm.get_alarm_time()  # Get alarm time from Alarm object
        if alarm_time and now.hour == alarm_time[0] and now.minute == alarm_time[1]:
                # Play the alarm sound
                self.alarm.play()  # Play alarm sound from