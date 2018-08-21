import os
import pygame
from win32api import GetSystemMetrics
(width, height) = (GetSystemMetrics(0),GetSystemMetrics(1))
MAKE_LARGER = 1.1
WOOD_img = pygame.image.load('images\Wood2.png').convert_alpha()
#Main menu
mm = pygame.image.load("images\Main_menu.png").convert_alpha()
s_mm = pygame.Surface.get_size(mm)
scale_mm = (height/(2*s_mm[0]), 2*height/(3*s_mm[1]))
mm = pygame.transform.scale(mm, (height//2, 2*height//3))
mm_shadow = pygame.image.load("images\mm_shadow.png").convert_alpha()
s_mms = pygame.Surface.get_size(mm_shadow)
print((int(s_mms[0]*scale_mm[0]), int(s_mms[1]*scale_mm[1])))
mm_shadow = pygame.transform.scale(mm_shadow, (int(s_mms[0]*scale_mm[0]), int(s_mms[1]*scale_mm[1])))
char1 = pygame.image.load("images\char1.png").convert_alpha()
char2 = pygame.image.load("images\char2.png").convert_alpha()
mt = pygame.image.load("images\main_title.png").convert_alpha()
size = pygame.Surface.get_size(mt)
factor = height/(2*size[0])
print(factor, height//2, int(factor*size[1]))
mt = pygame.transform.scale(mt, (height//2, int(factor*size[1])))
pg = pygame.image.load("images\pg.png").convert_alpha()
ps = pygame.Surface.get_size(pg)
p_s = height/(4*ps[0])
pg = pygame.transform.scale(pg, (int(p_s*ps[0]),int(p_s*ps[1])))
pg_hover = pygame.transform.scale(pg, (int(p_s*ps[0]*MAKE_LARGER),int(p_s*ps[1]*MAKE_LARGER))) #MAKE_LARGER is a float that controls how much larger the image is when hovered over
ng = pygame.image.load("images\\ng.png").convert_alpha()
ng = pygame.transform.scale(ng, (int(p_s*ps[0]),int(p_s*ps[1])))
ng_hover = pygame.transform.scale(ng, (int(p_s*ps[0]*MAKE_LARGER),int(p_s*ps[1]*MAKE_LARGER)))
qg = pygame.image.load("images\\qg.png").convert_alpha()
qg = pygame.transform.scale(qg, (int(p_s*ps[0]),int(p_s*ps[1])))
qg_hover = pygame.transform.scale(qg, (int(p_s*ps[0]*MAKE_LARGER),int(p_s*ps[1]*MAKE_LARGER)))

#board
scaledown = (height//7)/pygame.Surface.get_height(WOOD_img)
newWH = pygame.Surface.get_size(WOOD_img)
bg_img = pygame.image.load("images\\background.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height)).convert_alpha()
IRON_img = pygame.image.load("images\Stone2.png").convert_alpha()
CLAY_img = pygame.image.load("images\Clay2.png").convert_alpha()
WHEAT_img = pygame.image.load("images\Wheat2.png").convert_alpha()
SHEEP_img = pygame.image.load("images\Sheep2.png").convert_alpha()
WATER_img = pygame.image.load("images\Water2.png").convert_alpha()
SAND_img = pygame.image.load("images\Sand2.png").convert_alpha()
listOfHexes = [WOOD_img, IRON_img, CLAY_img, WHEAT_img, SHEEP_img, WATER_img, SAND_img]
newWH = (int(scaledown*newWH[0]), int(scaledown*newWH[1]))
WOOD_img = pygame.transform.scale(WOOD_img, newWH)
IRON_img = pygame.transform.scale(IRON_img, newWH)
CLAY_img = pygame.transform.scale(CLAY_img, newWH)
WHEAT_img = pygame.transform.scale(WHEAT_img, newWH)
SHEEP_img = pygame.transform.scale(SHEEP_img, newWH)
WATER_img = pygame.transform.scale(WATER_img, newWH)
SAND_img = pygame.transform.scale(SAND_img, newWH)
#print(newWH, pygame.Surface.get_size(WOOD_img))

tileSize = pygame.Surface.get_size(WOOD_img)
localSize = (tileSize[1]//3,tileSize[1]//3)
#base tile
ut = pygame.image.load("images\\ut.png").convert_alpha()
ut = pygame.transform.scale(ut, localSize)
ut_h = pygame.transform.scale(ut, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
#city tiles
wc = pygame.image.load("images\wc.png").convert_alpha()
wc = pygame.transform.scale(wc, localSize)
wc_h = pygame.transform.scale(wc, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
oc = pygame.image.load("images\oc.png").convert_alpha()
oc = pygame.transform.scale(oc, localSize)
oc_h = pygame.transform.scale(oc, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
rc = pygame.image.load("images\\rc.png").convert_alpha()
rc = pygame.transform.scale(rc, localSize)
rc_h = pygame.transform.scale(rc, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
bc = pygame.image.load("images\\bc.png").convert_alpha()
bc = pygame.transform.scale(bc, localSize)
bc_h = pygame.transform.scale(bc, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
#village tiles
wv = pygame.image.load("images\wv.png").convert_alpha()
wv = pygame.transform.scale(wv, localSize)
wv_h = pygame.transform.scale(wv, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
ov = pygame.image.load("images\ov.png").convert_alpha()
ov = pygame.transform.scale(ov, localSize)
ov_h = pygame.transform.scale(ov, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
rv = pygame.image.load("images\\rv.png").convert_alpha()
rv = pygame.transform.scale(rv, localSize)
rv_h = pygame.transform.scale(rv, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))
bv = pygame.image.load("images\\bv.png").convert_alpha()
bv = pygame.transform.scale(bv, localSize)
bv_h = pygame.transform.scale(bv, (int(localSize[0]*MAKE_LARGER), int(localSize[1]*MAKE_LARGER)))

#roads
w_r_lr = pygame.image.load("images\w_r_lr.png").convert_alpha()
lrScale = (tileSize[0]//2)/pygame.Surface.get_width(w_r_lr)
lrResize = (tileSize[0]//2,int(lrScale*pygame.Surface.get_height(w_r_lr)))
w_r_lr = pygame.transform.scale(w_r_lr, lrResize)
w_r_ru = pygame.transform.rotate(w_r_lr, 120)
w_r_rd = pygame.transform.rotate(w_r_lr, 60)
orlr = pygame.image.load("images\o_r_lr.png").convert_alpha()
orlr = pygame.transform.scale(orlr, lrResize)
orru = pygame.transform.rotate(orlr, 120)
orrd = pygame.transform.rotate(orlr, 60)
brlr = pygame.image.load("images\\b_r_lr.png").convert_alpha()
brlr = pygame.transform.scale(brlr, lrResize)
brru = pygame.transform.rotate(brlr, 120)
brrd = pygame.transform.rotate(brlr, 60)
rrlr = pygame.image.load("images\\r_r_lr.png").convert_alpha()
rrlr = pygame.transform.scale(rrlr, lrResize)
rrru = pygame.transform.rotate(rrlr, 120)
rrrd = pygame.transform.rotate(rrlr, 60)
#cards
cWood = pygame.image.load("images\cWood.png").convert_alpha()
size_Cards = pygame.Surface.get_size(cWood)
scaleCard = width/(15*size_Cards[0])
newCard = (int(scaleCard*size_Cards[0]), int(scaleCard*size_Cards[1]))
cWood = pygame.transform.scale(cWood, newCard)

cSheep = pygame.image.load("images\cSheep.png").convert_alpha()
cSheep = pygame.transform.scale(cSheep, newCard)

cClay = pygame.image.load("images\cClay.png").convert_alpha()
cClay = pygame.transform.scale(cClay, newCard)

cStone = pygame.image.load("images\cStone.png").convert_alpha()
cStone = pygame.transform.scale(cStone, newCard)

cWheat = pygame.image.load("images\cWheat.png").convert_alpha()
cWheat = pygame.transform.scale(cWheat, newCard)

knight = pygame.image.load("images\knight.png").convert_alpha()
knight = pygame.transform.scale(knight, newCard)

monopoly = pygame.image.load("images\monopoly.png").convert_alpha()
monopoly = pygame.transform.scale(monopoly, newCard)

year_of_plenty = pygame.image.load("images\year_of_plenty.png").convert_alpha()
yop = pygame.transform.scale(year_of_plenty, newCard)

road_building = pygame.image.load("images\\road_building.png").convert_alpha()
road_building = pygame.transform.scale(road_building, newCard)

cathedral = pygame.image.load("images\cathedral.png").convert_alpha()
cathedral = pygame.transform.scale(cathedral, newCard)

uni = pygame.image.load("images\\uni.png").convert_alpha()
uni = pygame.transform.scale(uni, newCard)

forum = pygame.image.load("images\\forum.png").convert_alpha()
forum = pygame.transform.scale(forum, newCard)

library = pygame.image.load("images\library.png").convert_alpha()
library = pygame.transform.scale(library, newCard)

great_hall = pygame.image.load("images\great_hall.png").convert_alpha()
great_hall = pygame.transform.scale(great_hall, newCard)

cBack = pygame.image.load("images\cBack.png").convert_alpha()
cBack = pygame.transform.scale(cBack, newCard)

dev_back = pygame.image.load("images\dev_back.png").convert_alpha()
dev_back = pygame.transform.scale(dev_back, newCard)

next_turn = pygame.image.load("images\\next_turn.png").convert_alpha()
scale = (height//7)/pygame.Surface.get_width(next_turn)
next_turn = pygame.transform.scale(next_turn, (int(scale*pygame.Surface.get_width(next_turn)), int(scale*pygame.Surface.get_height(next_turn))))

build_menu = pygame.image.load("images\\build_menu.png").convert_alpha()
b_m_s = (width/4.25)/pygame.Surface.get_width(build_menu)
build_menu = pygame.transform.scale(build_menu, (int(b_m_s*pygame.Surface.get_width(build_menu)), int(b_m_s*pygame.Surface.get_height(build_menu))))

arrow = pygame.image.load("images\\arrow.png").convert_alpha()
a_s = 20/pygame.Surface.get_height(arrow)
arrow = pygame.transform.scale(arrow, (int(a_s*pygame.Surface.get_width(arrow)), int(a_s*pygame.Surface.get_height(arrow))))
                                    




