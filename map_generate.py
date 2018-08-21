import img_handling
import pygame
import random as r
import tile
from win32api import GetSystemMetrics
(width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
BOARD_LEFT_POS = (width-height)//2
BUFFER_SPACE = 0

def gen_map(board):
    numTile = [[0,3],[1,3],[2,4],[3,4],[4,4]] #Stone, Clay, Wood, Wheat, Sheep
    numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    dim_tile = pygame.Surface.get_size(img_handling.WOOD_img)
    coords = ["2 4 0 3","4 6 0 3","6 8 0 3","1 3 2 5","3 5 2 5","5 7 2 5","7 9 2 5","0 2 4 7","2 4 4 7","4 6 4 7","6 8 4 7","8 10 4 7","1 3 6 9","3 5 6 9","5 7 6 9","7 9 6 9","2 4 8 11","4 6 8 11","6 8 8 11"]
    nth = 0
    tileBoard = []
    for j in range(7):
        for i in range(7):
            cons_shift = (height-5.5*dim_tile[0])//2
            shift_left = int(j*(dim_tile[0]*(3/4)+BUFFER_SPACE))
            shift_down = i*(dim_tile[1]+BUFFER_SPACE)
            constant_shift = dim_tile[1]//2
            if j%2==0:
                pos = (BOARD_LEFT_POS+shift_left+cons_shift, shift_down+constant_shift)
            else:
                pos = (BOARD_LEFT_POS+shift_left+cons_shift, shift_down) 
                       
            if ((j == 0 or j == 6) and i>=1 and i<=4) or ((j==1 or j==5) and (i==1 or i==5)) or ((j==2 or j==4) and (i==0 or i==5)) or (j==3 and (i==0 or i==6)):
                tileBoard.append(tile.Tile("Water", -1, img_handling.WATER_img, pos, 0))
            elif ((j==1 or j==5) and i>1 and i<5) or ((j==2 or j==4) and i>0 and i<5) or (j==3 and i>0 and i<6):
                if j==3 and i==3:
                    tileBoard.append(tile.Tile("Sand", -1, img_handling.SAND_img, pos, coords[nth], board))
                    nth+=1
                    #print(numbers, nth-1, i, j, "SAND TILE", pos)
                else:
                    select = r.randrange(len(numTile))
                    while numTile[select][1]==0:
                        numTile.pop(select)
                        select = r.randrange(len(numTile))
                        #print(select, len(numTile), numTile)
                    numTile[select][1] -= 1
                    newSel = numTile[select][0]
                    if newSel == 0:
                        num = r.randrange(len(numbers))
                        tileBoard.append(tile.Tile("Stone", numbers[num], img_handling.IRON_img, pos, coords[nth], board))
                        numbers.pop(num)
                        nth+=1
                    elif newSel == 1:
                        num = r.randrange(len(numbers))
                        tileBoard.append(tile.Tile("Clay", numbers[num], img_handling.CLAY_img, pos, coords[nth], board))
                        numbers.pop(num)                            
                        nth+=1
                    elif newSel == 2:
                        num = r.randrange(len(numbers))
                        tileBoard.append(tile.Tile("Wood", numbers[num], img_handling.WOOD_img, pos, coords[nth], board))
                        numbers.pop(num)                            
                        nth+=1
                    elif newSel == 3:
                        num = r.randrange(len(numbers))
                        tileBoard.append(tile.Tile("Wheat", numbers[num], img_handling.WHEAT_img, pos, coords[nth], board))
                        numbers.pop(num)                            
                        nth+=1
                    elif newSel == 4:
                        num = r.randrange(len(numbers))
                        tileBoard.append(tile.Tile("Sheep", numbers[num], img_handling.SHEEP_img, pos, coords[nth], board))
                        numbers.pop(num)
                        nth+=1
                    #print(numbers, nth-1, i, j, pos)
    #for i in range(len(tileBoard)):
        #print(tileBoard[i].t_type)
    return tileBoard
