#DECK has 14 knights 2 monopolies, 2 year of plenties, 2 road building and 5 point cards
#19 of each resource in the deck
import random as r
import img_handling
import pygame
# from win32api import GetSystemMetrics
# (width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
infoObject = pygame.display.Info()
(width, height) = (infoObject.current_w, infoObject.current_h)

BOARD_LEFT_POS = (width-height)//2
class Deck():
    def __init__(self):
        self.res_deck = {"SHEEP":19, "WHEAT":19, "CLAY":19, "STONE":19, "WOOD":19}
        self.dev_deck = []
        og_deck = []
        for i in range(14):
            og_deck.append("KNIGHT")
        for i in range(6):
            if i<2:
                og_deck.append("MONOPOLY")
            elif i<4:
                og_deck.append("ROAD_BUILDING")
            else:
                og_deck.append("YEAR_OF_PLENTY")
        og_deck.append("UNI")
        og_deck.append("FORUM")
        og_deck.append("GREAT_HALL")
        og_deck.append("LIBRARY")
        og_deck.append("CATHEDRAL")
        for i in range(25):
            num = r.randrange(len(og_deck))
            self.dev_deck.append(og_deck.pop(num))
        self.cardSize = pygame.Surface.get_size(img_handling.cWood)
        self.baseShift = 50

    def draw_res(self, res, player):
        if self.res_deck[res] > 0:
            self.res_deck[res] -= 1
            player.add_res(res)
        else:
            print("Sorry! There are no more available "+res.lower()+"!")

    def draw_dev(self, player):
        if len(self.dev_deck)>0:
            player.special_cards.append(self.dev_deck.pop())
        else:
            print("Sorry! There are no more available development cards!")

    def draw_decks(self, screen):
        if self.res_deck["WOOD"] > 0:
            screen.blit(img_handling.cWood,(BOARD_LEFT_POS-self.cardSize[0]//2, self.baseShift))
        if self.res_deck["SHEEP"] > 0:
            screen.blit(img_handling.cSheep,(BOARD_LEFT_POS+height-self.cardSize[0]//2, int(height/3)))
        if self.res_deck["WHEAT"] > 0:
            screen.blit(img_handling.cWheat,(BOARD_LEFT_POS-self.cardSize[0]//2, int(height-self.baseShift-self.cardSize[1])))
        if self.res_deck["CLAY"] > 0:
            screen.blit(img_handling.cClay,(BOARD_LEFT_POS+height-self.cardSize[0]//2, self.baseShift))
        if self.res_deck["STONE"] > 0:
            screen.blit(img_handling.cStone,(BOARD_LEFT_POS+height-self.cardSize[0]//2, int(2*height/3-self.cardSize[1])))
        if len(self.dev_deck) > 0:
            screen.blit(img_handling.dev_back,(BOARD_LEFT_POS+height-self.cardSize[0]//2, int(height-self.baseShift-self.cardSize[1])))
