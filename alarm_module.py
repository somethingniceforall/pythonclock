import pygame
import os

class Alarm:
    def __init__(self, hour=5, minute=28):
        # Set up the alarm sound
        self.alarm_sound = pygame.mixer.Sound('sounds/ringsound.wav')

        # Set the default alarm time
        self.alarm_time = (hour, minute)

        # Set up the font
        self.font = pygame.font.SysFont(None, 30)

        # Set up the input mode flag
        self.input_mode = False

    def set_alarm(self, hour, minute):
        # Set the alarm time
        self.alarm_time = (hour, minute)

    def cancel_alarm(self):
        # Cancel the alarm
        self.alarm_time = None

    def play(self):
        # Play the alarm sound
        self.alarm_sound.play()

    def stop(self):
        # Stop the alarm sound
        self.alarm_sound.stop()

    def get_alarm_time(self):
        # Return the current alarm time
        return self.alarm_time

    def draw_alarm_time(self, screen):
        # Draw the current alarm time in the top right corner of the screen
        alarm_time_text = self.font.render(f"Alarm: {self.alarm_time[0]:02d}:{self.alarm_time[1]:02d}", True, (255, 255, 255))
        alarm_time_rect = alarm_time_text.get_rect(topright=(screen.get_width() - 10, 10))
        screen.blit(alarm_time_text, alarm_time_rect)

        