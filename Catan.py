#Welcome to my Catan Boardgame simulation!! This is meant as an example of what you can do with coding
#Here, we simulate the boardgame Catan, albeit with low quality graphics!
import pygame
# from win32api import GetSystemMetrics
import os
import ctypes
import random as r
from roads import ROADS
import random as r
import time as t


#Optimize for
# (width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
pygame.init()
infoObject = pygame.display.Info()
width, height = (infoObject.current_w, infoObject.current_h)
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
# width, height = (800, 600)
# screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
import img_handling
import map_generate
import tile
import vertex
import player
import deck
import die
import draw

# myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
icon = pygame.image.load("images/board2.png").convert_alpha()
pygame.display.set_icon(icon)
#GAMEPLAY CONSTANTS
VILLAGE = "village"
CITY = "city"
ROBBER = "robber"
BOARD_LEFT_POS = (width-height)//2
BUFFER_SPACE = 2

#COLOURS
bgcolour = (255,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


#a global variable which keeps track of the current player
players = ["o", "b", "r", "w"]
tracker = 0
current_player = players[tracker]
playerDict = {}

def draw_card(screen, name, pos):
    player.draw_card(screen, name, pos)

def chooseRoad(s):
    es = []
    for e in s:
        es.append(next(iter(s)))
    if es[0][0] < es[1][0]:
        if es[0][1] > es[1][1]:
            return "ru"
        else:
            return "rd"
    elif es[0][0] > es[1][0]:
        if es[0][1] > es[1][1]:
            return "rd"
        else:
            return "ru"
    else:
        return "lr"

class Board():
    def __init__(self):
        self.board = vertex.fresh() #a two dimensional board with [y][x]
        self.tileBoard = map_generate.gen_map(self.board) #the hex tiles that populate the board
    def gen_new_map(self):
        self.board = vertex.fresh()
        self.tileBoard = map_generate.gen_map(self.board)

    def print_board(self):
        for i in range(12):
            stringOut = ""
            for j in range(11):
                stringOut += self.board[i][j].colour
            print(stringOut)

    def draw_board(self):
        for i in range(len(self.tileBoard)):
            self.tileBoard[i].draw_tile(screen)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != None:
                    self.board[i][j].draw_vertex(screen)




#intialize classes
board = Board()
deck = deck.Deck()
orange = player.Player("o")
blue = player.Player("b")
white = player.Player("w")
red = player.Player("r")
playerDict["o"] = orange
playerDict["r"] = red
playerDict["w"] = white
playerDict["b"] = blue



#ACTUAL GAMEPLAY CORE
running = True
state = 0
main_left = int(width/2-((width/2-BOARD_LEFT_POS)/2))
menu_left = main_left + height//8
mt_h = height//6+20
pg_h = mt_h + pygame.Surface.get_height(img_handling.mt) + 10
ng_h = pg_h + pygame.Surface.get_height(img_handling.pg) + 10
qg_h = ng_h + pygame.Surface.get_height(img_handling.qg) + 10
disp_hover_w = (pygame.Surface.get_width(img_handling.pg_hover)-pygame.Surface.get_width(img_handling.pg))//2
disp_hover_h = (pygame.Surface.get_height(img_handling.pg_hover)-pygame.Surface.get_height(img_handling.pg))//2
size = (height//15,height//15)
n_button_left = BOARD_LEFT_POS+height-pygame.Surface.get_width(img_handling.next_turn)
n_hovered = False


die1 = die.Die((BOARD_LEFT_POS+10,0), size)
die2 = die.Die((BOARD_LEFT_POS+size[0]+10,0), size)

hover_build_menu = 0
bm_hover_left = int(0.1*pygame.Surface.get_width(img_handling.build_menu))
bm_hover_right = pygame.Surface.get_width(img_handling.build_menu)-int(0.1*pygame.Surface.get_width(img_handling.build_menu))
r_hover = (height-pygame.Surface.get_height(img_handling.build_menu))//2 + int(0.13*pygame.Surface.get_height(img_handling.build_menu))
c_hover = r_hover + int(0.19*pygame.Surface.get_height(img_handling.build_menu))
v_hover = c_hover + int(0.16*pygame.Surface.get_height(img_handling.build_menu))
dev_hover = v_hover + int(0.15*pygame.Surface.get_height(img_handling.build_menu))
b_hover = dev_hover + int(0.23*pygame.Surface.get_height(img_handling.build_menu))

while running:
    hover_build_menu = 0
    hovered = 0
    n_hovered = False
    mousepos = pygame.mouse.get_pos()
    #print(mousepos)
    if state == 0 and mousepos[0] >= menu_left and mousepos[0] <= menu_left+pygame.Surface.get_width(img_handling.pg) and mousepos[1]>=pg_h and mousepos[1]<=pg_h+pygame.Surface.get_height(img_handling.pg):
        hovered = 1
    elif state == 0 and mousepos[0] >= menu_left and mousepos[0] <= menu_left+pygame.Surface.get_width(img_handling.pg) and mousepos[1]>=ng_h and mousepos[1]<=ng_h+pygame.Surface.get_height(img_handling.ng):
        hovered = 2
    elif state == 0 and mousepos[0] >= menu_left and mousepos[0] <= menu_left+pygame.Surface.get_width(img_handling.pg) and mousepos[1]>=qg_h and mousepos[1]<=qg_h+pygame.Surface.get_height(img_handling.ng):
        hovered = 3
    elif state == 1 and mousepos[0] >= n_button_left and mousepos[0] <= BOARD_LEFT_POS+height and mousepos[1] >= 0 and mousepos[1] <= pygame.Surface.get_height(img_handling.next_turn):
        n_hovered = True
    elif state == 1 and mousepos[0] >= bm_hover_left and mousepos[0] <= bm_hover_right and mousepos[1] >= r_hover and mousepos[1] <= c_hover:
        hover_build_menu = 1
    elif state == 1 and mousepos[0] >= bm_hover_left and mousepos[0] <= bm_hover_right and mousepos[1] >= c_hover and mousepos[1] <= v_hover:
        hover_build_menu = 2
    elif state == 1 and mousepos[0] >= bm_hover_left and mousepos[0] <= bm_hover_right and mousepos[1] >= v_hover and mousepos[1] <= dev_hover:
        hover_build_menu = 3
    elif state == 1 and mousepos[0] >= bm_hover_left and mousepos[0] <= bm_hover_right and mousepos[1] >= dev_hover and mousepos[1] <= b_hover:
        hover_build_menu = 4
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #elif event.type == pygame.MOUSEMOTION:
            #print("mouse at (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #for i in range(len(board.board)):
                #    for j in range(len(board.board[i])):
                #        if board.board[i][j]!=None and board.board[i][j].is_hovered() and state == 1:
                #            board.board[i][j].build = True

                if state==0 and event.pos[0] >= menu_left and event.pos[0] <= menu_left+pygame.Surface.get_width(img_handling.pg) and event.pos[1]<=qg_h+pygame.Surface.get_height(img_handling.qg) and event.pos[1] >= qg_h:
                    running = False
                elif state == 0 and event.pos[0] >= menu_left and event.pos[0] <= menu_left+pygame.Surface.get_width(img_handling.pg) and event.pos[1]>=pg_h and event.pos[1]<=pg_h+pygame.Surface.get_height(img_handling.pg):
                    state = 1
                elif state == 0 and mousepos[0] >= menu_left and mousepos[0] <= menu_left+pygame.Surface.get_width(img_handling.pg) and mousepos[1]>=ng_h and mousepos[1]<=ng_h+pygame.Surface.get_height(img_handling.ng):
                    state = 1
                    board.__init__()
                elif state == 1 and mousepos[0] >= n_button_left and mousepos[0] <= BOARD_LEFT_POS+height and mousepos[1] >= 0 and mousepos[1] <= pygame.Surface.get_height(img_handling.next_turn):
                    tracker = (tracker+1)%4
                    current_player = players[tracker]
                    draw.draw_hands(players, playerDict, screen, current_player)
                    die.roll_dice_simultaneously([die1, die2], screen)
                    rolled_num = die1.number + die2.number
                    for i in range(len(board.tileBoard)):
                        if board.tileBoard[i].number==rolled_num:
                            board.tileBoard[i].add_resources(orange, red, blue, white, deck)

            #if event.button == 3:
            #    for i in range(len(board.board)):
            #        for j in range(len(board.board[i])):
            #            if board.board[i][j]!=None and board.board[i][j].build:
            #                board.board[i][j].build = False

        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_r:
                board.gen_new_map()

                print("generate map")
            elif key == pygame.K_m:
                state = 0
                print("main menu", state)
            elif key == pygame.K_l:
                state = 1
                print("launch game", state)
            elif key == pygame.K_ESCAPE:
                running = False
            elif key == pygame.K_UP:
                board.board[5][4].colour = "o"
                board.board[5][4].occ_by = "ov"
            elif key == pygame.K_LEFT:
                board.board[5][4].colour = "o"
                board.board[5][4].occ_by = "oc"
            elif key == pygame.K_RIGHT:
                tracker = (tracker+1)%4
                current_player = players[tracker]
            elif key == pygame.K_a:
                playerDict[current_player].add_res("WOOD")

    screen.blit(img_handling.bg_img, (0,0))
    draw.draw_game_board(state, hovered, screen, board, deck, current_player, players, playerDict, die1, die2, n_hovered, hover_build_menu)
    pygame.display.flip()
