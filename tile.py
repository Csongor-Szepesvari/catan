import pygame
import img_handling
BLACK = (0,0,0)
WHITE = (255,255,255)
(width, height) = pygame.Surface.get_size(img_handling.WOOD_img)
FONT_SIZE = int(width//2.5)
class Tile():
    def __init__(self, t_type, number, img, pos, coords, board=None):
        self.t_type = t_type
        self.number = number
        self.coords = coords
        self.vertices = []
        self.pos = pos
        self.img = img
        if self.number!=-1:
            self.num_disp = pygame.image.load("images/num" + str(self.number) + ".png")
            self.num_disp = pygame.transform.scale(self.num_disp, (FONT_SIZE, FONT_SIZE)).convert_alpha()
            self.fill_vertices(board)

    def draw_tile(self, screen):
        #outputs the tile to the screen with its number
        screen.blit(self.img, (self.pos))
        if self.number!=-1:
            screen.blit(self.num_disp, (int(self.pos[0]+width/2-FONT_SIZE/2), int(self.pos[1]+height/2-FONT_SIZE/2)))

    def name_breakdown(self):
        #breaks down the "coords" element from a string and returns all of the 6 vertices from it
        #takes the inbetween of the first 2 coords and matches it with either of the ends
        #takes the front and end of first 2 coords and matches it with either of the ones in between the last 2
        #for example "2 4 0 3" -> [[3,0],[3,3],[2,1],[2,2],[4,1],[4,2]]
        baseList = list(map(int,self.coords.split()))
        coordList = []
        coordList.append([baseList[0]+1, baseList[2]])
        coordList.append([baseList[0]+1, baseList[3]])
        coordList.append([baseList[0], baseList[2]+1])
        coordList.append([baseList[0], baseList[3]-1])
        coordList.append([baseList[1], baseList[2]+1])
        coordList.append([baseList[1], baseList[3]-1])
        return coordList

    def fill_vertices(self, board):
        #print("y len:", len(board),"x len:",len(board[0]))
        coordList = self.name_breakdown()
        for i in range(6):
            coord = coordList[i]
            #print(coord[0], coord[1])
            self.vertices.append(board[coord[0]][coord[1]])
        #print(board)

    def add_resources(self, o, r , b, w, deck):
        #is called once it is discovered that the number has been rolled, adds to the players hands the resource attached
        res = self.t_type.upper()
        for i in range(6):
            vertex = self.vertices[i]
            if vertex.colour != " ":
                if vertex.colour == "r":
                    if vertex.occ_by == "rv":
                        deck.draw_res(res, r)
                    else:
                        deck.draw_res(res, r)
                        deck.draw_res(res, r)
                elif vertex.colour == "b":
                    if vertex.occ_by == "bv":
                        deck.draw_res(res, b)
                    else:
                        deck.draw_res(res, b)
                        deck.draw_res(res, b)
                elif vertex.colour == "w":
                    if vertex.occ_by == "wv":
                        deck.draw_res(res, w)
                    else:
                        deck.draw_res(res, w)
                        deck.draw_res(res, w)
                elif vertex.colour == "o":
                    if vertex.occ_by == "ov":
                        deck.draw_res(res, o)
                    else:
                        deck.draw_res(res, o)
                        deck.draw_res(res, o)
