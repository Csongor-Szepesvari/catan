import logging
import pygame
import time
import random as r
import threading
# from win32api import GetSystemMetrics
# (width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
infoObject = pygame.display.Info()
width, height = (infoObject.current_w, infoObject.current_h)


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class Die(object):
    """A single die that can be rolled!"""

    def __init__(self, pos, size):
        self.pos = pos
        self.number = 1
        dim = size
        self.one = pygame.image.load("images/d1.png").convert_alpha()
        self.one = pygame.transform.scale(self.one, dim)
        self.two = pygame.image.load("images/d2.png").convert_alpha()
        self.two = pygame.transform.scale(self.two, dim)
        self.three = pygame.image.load("images/d3.png").convert_alpha()
        self.three = pygame.transform.scale(self.three, dim)
        self.four = pygame.image.load("images/d4.png").convert_alpha()
        self.four = pygame.transform.scale(self.four, dim)
        self.five = pygame.image.load("images/d5.png").convert_alpha()
        self.five = pygame.transform.scale(self.five, dim)
        self.six = pygame.image.load("images/d6.png").convert_alpha()
        self.six = pygame.transform.scale(self.six, dim)

    def roll_once(self):
        """Assign new random value. No screen update."""
        self.number = r.randrange(1, 7)

    def roll(self, done_rolling, num_rolls=10, initial_time_delay=100):
        """Assign new random value intermittently. No screen update."""
        self.number = r.randrange(1, 7)
        time_delay = initial_time_delay  # in ms
        for i in range(num_rolls):
            self.roll_once()
            logging.debug("Roll %d, new value %d.", i, self.number)
            time.sleep(time_delay/1000)
            time_delay += r.randrange(10, 50)
        self.roll_once()
        done_rolling.set()

    def draw_die(self, screen):
        if self.number == 1:
            screen.blit(self.one, self.pos)
        elif self.number == 2:
            screen.blit(self.two, self.pos)
        elif self.number == 3:
            screen.blit(self.three, self.pos)
        elif self.number == 4:
            screen.blit(self.four, self.pos)
        elif self.number == 5:
            screen.blit(self.five, self.pos)
        else:
            screen.blit(self.six, self.pos)


def roll_dice_simultaneously(dice, screen, num_rolls=9, initial_delay=100):
    """Roll (and animate the simultaneous rolling of) the list of dice."""
    events = []
    threads = []
    for die in dice:
        finished = threading.Event()
        thread = threading.Thread(target=die.roll, args=(finished, num_rolls, initial_delay))
        thread.start()
        threads.append(thread)
        events.append(finished)

    # Keep drawing until all rolls are finished.
    while not all([event.isSet() for event in events]):
        logging.debug("Drawing dice onto internal thingy.")
        for die in dice:
            die.draw_die(screen)
        logging.debug("Showing on screen.")
        pygame.display.flip()
        time.sleep(0.05)

    for thread in threads:
        thread.join()
