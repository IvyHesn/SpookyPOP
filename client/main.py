# 1 - Import library
import pygame
from pygame.locals import *
from sanxiaoLogic import *

# 2 - Initialize the game
pygame.init()
screen_width, screen_height = 454, 648
screen=pygame.display.set_mode((screen_width, screen_height))

# 3 - Load images
bg_botton = pygame.image.load("res/scene/desktop.png")
grass = pygame.image.load("res/scene/grass.png")
ele0 = pygame.image.load("res/element/0.png")
ele1 = pygame.image.load("res/element/1.png")
ele2 = pygame.image.load("res/element/2.png")
ele3 = pygame.image.load("res/element/3.png")
ele4 = pygame.image.load("res/element/4.png")
ele5 = pygame.image.load("res/element/5.png")
load_images=[ele0,ele1,ele2,ele3,ele4,ele5,]
level_ele=[1,2,1,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,]

chooseframe = pygame.image.load("res/scene/chooseframe.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    #绘制草地
    for x in range(0,screen_width//grass.get_width()+1):
        for y in range(0,screen_height//grass.get_height()+1):
            screen.blit(grass,(x*grass.get_width(),y*grass.get_height()))
    #绘制格子底
    screen.blit(bg_botton, (0,324))
    #绘制格子里的元素
    for i in range(0,35):
        x,y=i%7*65,i//7*65+324
        screen.blit(load_images[level_ele[i]], (x,y))
    
    # 7 - update the screen
    pygame.display.flip()
    
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        # check mouse buttondown
        if event.type==pygame.MOUSEBUTTONDOWN:
            posX,posY=pygame.mouse.get_pos()
            gridIndex=getGridIndex(posX,posY)#获取点击的格子
            if gridIndex!=None:
                #判断选取状态
                if chooseState[0]==0:
                    chooseState[0]=1-chooseState[0]#选中格子
                    chooseState[1]=gridIndex#更新gridIndex
                    screen.blit(chooseframe,getGridPosXY(gridIndex))
                    pygame.display.flip()
                    #break
                if chooseState[0]==1:
                    #判断是否可以交换
                    if ischangeGrid(chooseState,gridIndex)==True:
                        screen.blit(chooseframe,getGridPosXY(gridIndex))
                        pygame.display.flip()
                        changeGrid(chooseState[1],gridIndex,level_ele)
                        chooseState=[0,0]#初始化选取状态
                        #break
                    if ischangeGrid(chooseState,gridIndex)==False:
                        screen.blit(chooseframe,getGridPosXY(gridIndex))
                        pygame.display.flip()
                        chooseState[1]=gridIndex#更新选取的格子
                        #break



