import pygame
import time as t
import random as r
from win32api import GetSystemMetrics
(width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))

#A single die that can be rolled!
class Die():
    def __init__(self, pos, size):
        self.pos = pos
        self.number = 1
        dim = size
        self.one = pygame.image.load("images\d1.png").convert_alpha()
        self.one = pygame.transform.scale(self.one, dim)
        self.two = pygame.image.load("images\d2.png").convert_alpha()
        self.two = pygame.transform.scale(self.two, dim)
        self.three = pygame.image.load("images\d3.png").convert_alpha()
        self.three = pygame.transform.scale(self.three, dim)
        self.four = pygame.image.load("images\d4.png").convert_alpha()
        self.four = pygame.transform.scale(self.four, dim)
        self.five = pygame.image.load("images\d5.png").convert_alpha()
        self.five = pygame.transform.scale(self.five, dim)
        self.six = pygame.image.load("images\d6.png").convert_alpha()
        self.six = pygame.transform.scale(self.six, dim)

    def roll_die(self, screen):
        
        num_rolls = 10
        time_delay = 100 #in ms
        for i in range(num_rolls):
            #print("why is this broken")
            self.number = r.randrange(1,7)
            self.draw_die(screen)
            pygame.display.flip()
            t.sleep(time_delay/1000)
            time_delay+=15
        self.number = r.randrange(1,7)
        self.draw_die(screen)
        
        

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
