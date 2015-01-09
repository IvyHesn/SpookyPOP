import pygame
from pygame.locals import *

#界面
screen_size = (screen_width, screen_height) = (454, 648)
bg_botton = pygame.image.load("res/scene/desktop.png")
grass = pygame.image.load("res/scene/grass.png")
chooseframe = pygame.image.load("res/scene/chooseframe.png")
#元素
ele0 = pygame.image.load("res/element/0.png")
ele1 = pygame.image.load("res/element/1.png")
ele2 = pygame.image.load("res/element/2.png")
ele3 = pygame.image.load("res/element/3.png")
ele4 = pygame.image.load("res/element/4.png")
ele5 = pygame.image.load("res/element/5.png")
#
load_images=[ele0,ele1,ele2,ele3,ele4,ele5,]
level_ele=[1,2,1,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,]
#需要初始化
posX,posY=[0,0]
mousePos=[None,None]

