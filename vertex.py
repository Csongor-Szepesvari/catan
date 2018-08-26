import pygame as p
import img_handling as i
# from win32api import GetSystemMetrics
# (width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
import pygame
infoObject = pygame.display.Info()
(width, height) = (infoObject.current_w, infoObject.current_h)
BOARD_LEFT_POS = (width-height)//2
dim_tile = p.Surface.get_size(i.WOOD_img)
cons_shift = (height-4*dim_tile[0])//2
cons_down = dim_tile[1]
vert_dim = p.Surface.get_size(i.ut)
#We hard-code the acceptable values for real vertices in a global list!
acceptable = [[5,6],[3,4,7,8],[1,2,5,6,9,10],[0,3,4,7,8,11],[1,2,5,6,9,10],[0,3,4,7,8,11],[1,2,5,6,9,10],[0,3,4,7,8,11],[1,2,5,6,9,10],[3,4,7,8],[5,6]]
class Vertex():
    def __init__(self, pos):
        self.pos = pos#y, x
        self.display_pos = [0,0]
        if self.pos[1]%2==0:
            self.display_pos[0] = int(BOARD_LEFT_POS+self.pos[1]//2*0.75*dim_tile[0]+cons_shift-vert_dim[0]/2)
        else:
            self.display_pos[0] = int(BOARD_LEFT_POS+self.pos[1]//2*0.75*dim_tile[0]+cons_shift+0.25*dim_tile[0]-vert_dim[0]/2)
        if self.pos[0]%2==0:
            self.display_pos[1] = int(self.pos[0]//2*dim_tile[1]+cons_down-vert_dim[1]/2)
        else:
            self.display_pos[1] = int(self.pos[0]//2*dim_tile[1]+cons_down+0.5*dim_tile[1]-vert_dim[1]/2)
        self.edges = []#used to store the frozenset of edges around it
        if pos[1]==0 or pos[1]==2 or pos[1]==4 or pos[1]==6 or pos[1]==8 or pos[1]==10:
            if pos[1] == 0:
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]+1))))
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]-1))))
            elif (pos[1]==6 and pos[0]==0) or (pos[1]==8 and pos[0]==1) or (pos[1]==10 and pos[0]==2):
                self.edges.append(frozenset((pos,(pos[0],pos[1]-1))))
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]+1))))
            elif (pos[1]==6 and pos[0]==10) or (pos[1]==8 and pos[0]==9) or (pos[1]==10 and pos[0]==8):
                self.edges.append(frozenset((pos,(pos[0],pos[1]-1))))
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]-1))))
            else:
                self.edges.append(frozenset((pos,(pos[0],pos[1]-1))))
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]+1))))
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]-1))))
        else:
            if pos[1]==11:
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]-1))))
                self.edges.append(frozenset((pos,(pos[0]+1,pos[1]-1))))
            elif (pos[1]==4 and pos[0]==0) or (pos[1]==3 and pos[0]==1) or (pos[1]==1 and pos[0]==2):
                self.edges.append(frozenset((pos,(pos[0],pos[1]+1))))
                self.edges.append(frozenset((pos,(pos[0]+1,pos[1]-1))))
            elif (pos[1]==4 and pos[0]==0) or (pos[1]==3 and pos[0]==1) or (pos[1]==1 and pos[0]==2):
                self.edges.append(frozenset((pos,(pos[0],pos[1]+1))))
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]-1))))
            else:
                self.edges.append(frozenset((pos,(pos[0]-1,pos[1]-1))))
                self.edges.append(frozenset((pos,(pos[0]+1,pos[1]-1))))
                self.edges.append(frozenset((pos,(pos[0],pos[1]+1))))
        self.occ_by = " "
        self.colour = " "
        self.build = False
        self.disp_hover = (p.Surface.get_width(i.oc_h)-p.Surface.get_width(i.oc))//2

    def draw_vertex(self, screen):
        if self.occ_by == " ":
            screen.blit(i.ut, self.display_pos)
        elif self.colour == "o":
            if self.occ_by == "ov":
                if self.is_hovered():
                    screen.blit(i.ov_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.ov, self.display_pos)
            else:
                if self.is_hovered():
                    screen.blit(i.oc_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.oc, self.display_pos)
        elif self.colour == "b":
            if self.occ_by == "bv":
                if self.is_hovered():
                    screen.blit(i.bv_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.bv, self.display_pos)
            else:
                if self.is_hovered():
                    screen.blit(i.bc_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.bc, self.display_pos)
        elif self.colour == "r":
            if self.occ_by == "rv":
                if self.is_hovered():
                    screen.blit(i.rv_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.rv, self.display_pos)
            else:
                if self.is_hovered():
                    screen.blit(i.rc_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.rc, self.display_pos)
        else:
            if self.occ_by == "wv":
                if self.is_hovered():
                    screen.blit(i.wv_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.wv, self.display_pos)
            else:
                if self.is_hovered():
                    screen.blit(i.wc_h, (self.display_pos[0]-self.disp_hover, self.display_pos[1]-self.disp_hover))
                else:
                    screen.blit(i.wc, self.display_pos)

    def is_hovered(self):
        #if mouseposition is within the circle then it is hovered
        #if r^2 > (mousepos_x - circle_center_x)^2 + (mousepos_y - circle_center_y)^2 then inside circle
        mousepos = p.mouse.get_pos()
        r = vert_dim[0]//2
        return r**2 > (mousepos[0]-(self.display_pos[0]+vert_dim[0]//2))**2 + (mousepos[1]-(self.display_pos[1]+vert_dim[1]//2))**2

    #deprecated function should not work like this!
    def build_menu(self, cur_player, screen):
        if self.build:
            if cur_player == "o":
                screen.blit(i.ov, (self.display_pos[0]+vert_dim[0],self.display_pos[1]+vert_dim[0]))
                screen.blit(i.oc, (self.display_pos[0]-vert_dim[0],self.display_pos[1]+vert_dim[0]))
            elif cur_player == "r":
                screen.blit(i.rv, (self.display_pos[0]+vert_dim[0],self.display_pos[1]+vert_dim[0]))
                screen.blit(i.rc, (self.display_pos[0]-vert_dim[0],self.display_pos[1]+vert_dim[0]))
            elif cur_player == "b":
                screen.blit(i.bv, (self.display_pos[0]+vert_dim[0],self.display_pos[1]+vert_dim[0]))
                screen.blit(i.bc, (self.display_pos[0]-vert_dim[0],self.display_pos[1]+vert_dim[0]))
            else:
                screen.blit(i.wv, (self.display_pos[0]+vert_dim[0],self.display_pos[1]+vert_dim[0]))
                screen.blit(i.wc, (self.display_pos[0]-vert_dim[0],self.display_pos[1]+vert_dim[0]))

def make_vertex(pos):
    new_vert = Vertex(pos)
    return new_vert

def fresh():
    #generates a new board of vertices indexed by row and then column (y,x)
    board = []
    for i in range(11):
        board.append([])
        for j in range(12):
            if j in acceptable[i]:
                board[i].append(make_vertex((i,j)))
            else:
                board[i].append(None)
    return board
