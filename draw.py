import pygame
import img_handling
from win32api import GetSystemMetrics
(width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
BOARD_LEFT_POS = (width-height)//2
main_left = int(width/2-((width/2-BOARD_LEFT_POS)/2))
menu_left = main_left + height//8
mt_h = height//6+20
pg_h = mt_h + pygame.Surface.get_height(img_handling.mt) + 10
ng_h = pg_h + pygame.Surface.get_height(img_handling.pg) + 10
qg_h = ng_h + pygame.Surface.get_height(img_handling.qg) + 10
disp_hover_w = (pygame.Surface.get_width(img_handling.pg_hover)-pygame.Surface.get_width(img_handling.pg))//2
disp_hover_h = (pygame.Surface.get_height(img_handling.pg_hover)-pygame.Surface.get_height(img_handling.pg))//2

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

r_hover = (height-pygame.Surface.get_height(img_handling.build_menu))//2 + int(0.19*pygame.Surface.get_height(img_handling.build_menu))
c_hover = r_hover + int(0.18*pygame.Surface.get_height(img_handling.build_menu))
v_hover = c_hover + int(0.16*pygame.Surface.get_height(img_handling.build_menu))
dev_hover = v_hover + int(0.19*pygame.Surface.get_height(img_handling.build_menu))
b_hover = dev_hover + int(0.30*pygame.Surface.get_height(img_handling.build_menu))
bm_hover_right = pygame.Surface.get_width(img_handling.build_menu)-int(0.05*pygame.Surface.get_width(img_handling.build_menu))

def draw_win(colour):
    if colour == "b":
        print("BLUE HAS WON THE GAME")
    elif colour == "w":
        print("WHITE HAS WON THE GAME")
    elif colour == "r":
        print("RED HAS WON THE GAME")
    else:
        print("ORANGE HAS WON THE GAME")
        
def draw_invalid_move():
    print("That is an invalid move, please make a valid move!")

def draw_hands(players, playerDict, screen, current_player):
    for letter in players:
        playerDict[letter].draw_hand(screen, current_player)
    
def draw_game_board(state, hovered, screen, board, deck, current_player, players, playerDict, die1, die2, n_hovered, hovered_build_menu): #the hovered number tells you which aspect of the menu is hovered over
    if state==0: #Launch Screen
        #Main Menu background
        screen.blit(img_handling.mm, (main_left, height//6))
        screen.blit(img_handling.mm_shadow, (main_left-int(10*img_handling.scale_mm[0]), height//6-int(10*img_handling.scale_mm[1])))
        #Main title
        screen.blit(img_handling.mt, (main_left, mt_h))
        #Two characters on the side
        screen.blit(img_handling.char2, (int(main_left+height/2-pygame.Surface.get_width(img_handling.char2)/3), height-pygame.Surface.get_height(img_handling.char2)))
        screen.blit(img_handling.char1, (int(main_left-pygame.Surface.get_width(img_handling.char1)/2), height-pygame.Surface.get_height(img_handling.char1)))
        #Menu
        if hovered == 0:
            #display all as normal
            screen.blit(img_handling.pg, (menu_left, pg_h))
            screen.blit(img_handling.ng, (menu_left, ng_h))
            screen.blit(img_handling.qg, (menu_left, qg_h))
        elif hovered == 1:
            screen.blit(img_handling.pg_hover, (menu_left-disp_hover_w, pg_h-disp_hover_h))
            screen.blit(img_handling.ng, (menu_left, ng_h))
            screen.blit(img_handling.qg, (menu_left, qg_h))
        elif hovered == 2:
            screen.blit(img_handling.pg, (menu_left, pg_h))
            screen.blit(img_handling.ng_hover, (menu_left-disp_hover_w, ng_h-disp_hover_h))
            screen.blit(img_handling.qg, (menu_left, qg_h))
        elif hovered == 3:
            screen.blit(img_handling.pg, (menu_left, pg_h))
            screen.blit(img_handling.ng, (menu_left, ng_h))
            screen.blit(img_handling.qg_hover, (menu_left-disp_hover_w, qg_h-disp_hover_h))            
    elif state==1:
        #a big rectangle designating the actual board portion of the screen!
        pygame.draw.rect(screen, WHITE, ((width-height)//2, 0, height, height))
        board.draw_board()
        #for i in range(len(board.board)):
        #    for j in range(len(board.board[i])):
        #        if board.board[i][j]!=None and board.board[i][j].build:
        #            board.board[i][j].build_menu(current_player, screen)
        deck.draw_decks(screen)
        die1.draw_die(screen)
        die2.draw_die(screen)
        screen.blit(img_handling.build_menu, (0, (height-pygame.Surface.get_height(img_handling.build_menu))//2))
        if hovered_build_menu == 1:
            screen.blit(img_handling.arrow, (bm_hover_right,r_hover))
        elif hovered_build_menu == 2:
            screen.blit(img_handling.arrow, (bm_hover_right,c_hover))
        elif hovered_build_menu == 3:
            screen.blit(img_handling.arrow, (bm_hover_right,v_hover))
        elif hovered_build_menu == 4:
            screen.blit(img_handling.arrow, (bm_hover_right,dev_hover))
        next_turn = img_handling.next_turn
        if n_hovered:
            n_pos = (BOARD_LEFT_POS+height-int(1.1*pygame.Surface.get_width(next_turn)),0)
            screen.blit(pygame.transform.scale(next_turn, (int(1.1*pygame.Surface.get_width(next_turn)),int(1.1*pygame.Surface.get_height(next_turn)))), n_pos)
        else:
            screen.blit(next_turn, (BOARD_LEFT_POS+height-pygame.Surface.get_width(next_turn), 0))
        draw_hands(players, playerDict, screen, current_player)
        
