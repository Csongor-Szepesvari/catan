import pygame
import img_handling
from win32api import GetSystemMetrics
(width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
BORDERSHIFT = 5
class Player():
    def __init__(self, colour):
        self.colour = colour
        self.res = {"WOOD":0,"SHEEP":0,"CLAY":0,"STONE":0,"WHEAT":0}
        self.res_name = ["WOOD", "SHEEP", "CLAY", "STONE", "WHEAT"]
        self.special_cards = []
        self.points = 0
        self.resources = 0
        
        
    def add_res(self, resource):
        self.res[resource] += 1
        self.resources += 1
    
    def build_city(self, x, y, board):
        if board.board[y][x].occ_by == self.colour+"v" and self.res[self.WHEAT] == 2 and self.res[IRON] == 3:
            board.board[y][x].occ_by = self.colour+"c"
            self.points += 1
        else:
            draw_invalid_move()
    
    def check_win(self):
        if self.points == 10:
            draw_win(self.colour)
    
    def draw_hand(self, screen, turn_colour):
        cardSize = img_handling.newCard
        
        base_location = [0,0]
        if self.colour == "o":
            base_location = [0,0]
        elif self.colour == "b":
            base_location = [1,0]
        elif self.colour == "r":
            base_location = [0,1]
        elif self.colour == "w":
            base_location = [1,1]
        
        if turn_colour == self.colour:
            num = 0
            for name in self.res_name:
                for i in range(self.res[name]):
                    if base_location[0] == 1:
                        left_pos = width - (num+1)*(cardSize[0]//4+BORDERSHIFT) - 3*cardSize[0]//4
                    else:
                        left_pos = BORDERSHIFT + num*(cardSize[0]//4+BORDERSHIFT)
                        
                    if base_location[1] == 1:
                        top_pos = height - (cardSize[1]+BORDERSHIFT)
                    else:
                        top_pos = BORDERSHIFT
                        
                    draw_card(screen, name, (left_pos, top_pos))
                    num += 1
            for i in range(len(self.special_cards)):
                if base_location[0] == 1:
                    left_pos = width - (num+1)*(cardSize[0]+BORDERSHIFT)
                else:
                    left_pos = BORDERSHIFT + num*(cardSize[0]+BORDERSHIFT)
                    
                if base_location[1] == 1:
                    top_pos = height - (cardSize[1]+BORDERSHIFT)
                else:
                    top_pos = BORDERSHIFT
                    
                draw_card(screen, self.special_cards[i], (left_pos, top_pos))
                num += 1
        
        else:
            num = 0
            for i in range(self.resources):
                if base_location[0] == 1:
                    left_pos = width - (num+1)*(cardSize[0]//6+BORDERSHIFT) - 5*cardSize[0]//6
                else:
                    left_pos = BORDERSHIFT + num*(cardSize[0]//6+BORDERSHIFT)
                    
                if base_location[1] == 1:
                    top_pos = height - (cardSize[1]+BORDERSHIFT)
                else:
                    top_pos = BORDERSHIFT
                    
                draw_card(screen, "RES_BACK", (left_pos, top_pos))
                num += 1
                
            for i in range(len(self.special_cards)):
                if base_location[0] == 1:
                    left_pos = width - (num+1)*(cardSize[0]//6+BORDERSHIFT) - 5*cardSize[0]//6
                else:
                    left_pos = BORDERSHIFT + num*(cardSize[0]//6+BORDERSHIFT)
                    
                if base_location[1] == 1:
                    top_pos = height - (cardSize[1]+BORDERSHIFT)
                else:
                    top_pos = BORDERSHIFT
                    
                draw_card(screen, "SPEC_BACK", (left_pos, top_pos))
                num += 1            


def draw_card(screen, name, pos):
    if name == "WOOD":
        screen.blit(img_handling.cWood, pos)
    elif name == "SHEEP":
        screen.blit(img_handling.cSheep, pos)
    elif name == "CLAY":
        screen.blit(img_handling.cClay, pos)
    elif name == "STONE":
        screen.blit(img_handling.cStone, pos)
    elif name == "WHEAT":
        screen.blit(img_handling.cWheat, pos)
    elif name == "KNIGHT":
        screen.blit(img_handling.knight, pos)
    elif name == "RES_BACK":
        screen.blit(img_handling.cBack, pos)
    elif name == "UNI":
        screen.blit(img_handling.uni, pos)
    elif name == "LIBRARY":
        screen.blit(img_handling.library, pos)
    elif name == "FORUM":
        screen.blit(img_handling.forum, pos)
    elif name == "CATHEDRAL":
        screen.blit(img_handling.cathedral, pos)
    elif name == "GREAT_HALL":
        screen.blit(img_handling.great_hall, pos)
    elif name == "YOP":
        screen.blit(img_handling.yop, pos)
    elif name == "MONOPOLY":
        screen.blit(img_handling.monopoly, pos)
    elif name == "ROAD_BUILDING":
        screen.blit(img_handling.road_building, pos)
    else:
        screen.blit(img_handling.dev_back, pos)
