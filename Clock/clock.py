import pygame
import sys
from clock_module import Clock

def main():
    # Create a clock object
    clock = Clock()

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the clock
        clock.update_clock()

        # Tick the clock
        clock.clock.tick(60)

if __name__ == '__main__':
    main()