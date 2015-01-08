import pygame
from pygame.locals import *

# 3 - Load images
screen_width, screen_height = 454, 648
screen=pygame.display.set_mode((screen_width, screen_height))

bg_botton = pygame.image.load("res/scene/desktop.png")
grass = pygame.image.load("res/scene/grass.png")
ele0 = pygame.image.load("res/element/0.png")
ele1 = pygame.image.load("res/element/1.png")
ele2 = pygame.image.load("res/element/2.png")
ele3 = pygame.image.load("res/element/3.png")
ele4 = pygame.image.load("res/element/4.png")
ele5 = pygame.image.load("res/element/5.png")
load_images=[ele0,ele1,ele2,ele3,ele4,ele5,]
chooseframe = pygame.image.load("res/scene/chooseframe.png")

level_ele=[1,2,1,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,]

#3x logic
#根据鼠标位置判断所在格
def getGridIndex(posX,posY):
    if posY>=324:
        gridX,gridY=posX//65,(posY-324)//65
        gridIndex=gridX+7*gridY
        return gridIndex
    else:
        return None
#根据gridIndex得到这个格子的坐标
def getGridPosXY(gridIndex):
    x,y=gridIndex%7,gridIndex//7
    posX,posY=x*65,y*65+324
    return (posX,posY)

#选中状态，选中就记录选中的格子
gridIndex=None
chooseGrid1=None
chooseGrid2=None
#交换格子里的元素
def ischangeGrid(chooseGrid1,chooseGrid2):
    if chooseGrid1==None or chooseGrid2==None:
        print (None)
    else:
        if abs(chooseGrid1-chooseGrid2)==1 or abs(chooseGrid1-chooseGrid2)==7:
            return True
        else:
            return False
            
def changeGrid(gridIndex,chooseGrid1=None,chooseGrid2=None,level_ele=level_ele):
    if gridIndex!=None:
        #判断选取状态
        if chooseGrid1==None:
            chooseGrid1=gridIndex#更新gridIndex
            screen.blit(chooseframe,getGridPosXY(gridIndex))
            pygame.display.flip()
            #break
        if chooseGrid1!=None:
            #判断是否可以交换
            chooseGrid2=gridIndex
            if ischangeGrid(chooseGrid1,chooseGrid2)==True:
                screen.blit(chooseframe,getGridPosXY(gridIndex))
                pygame.display.flip()
                level_ele[chooseGrid1],level_ele[chooseGrid2]=level_ele[chooseGrid2],level_ele[chooseGrid1]
                chooseGrid1,chooseGrid2=None,None#初始化选取状态
                #break
            if ischangeGrid(chooseGrid1,chooseGrid2)==False:
                screen.blit(chooseframe,getGridPosXY(gridIndex))
                pygame.display.flip()
                chooseGrid1=chooseGrid2#更新选取的格子
                #break


