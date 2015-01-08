import pygame
from pygame.locals import *

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
#选中状态
chooseState=[0,None]#[是否选中，选中的gridIndex]
#交换格子里的元素
def ischangeGrid(chooseState,gridIndex):
    grid1,grid2=chooseState[1],gridIndex
    if abs(grid1-grid2)==1 or abs(grid1-grid2)==7:
        return True
    else:
        return False
        
def changeGrid(grid1,grid2,level_ele):
	level_ele[grid1],level_ele[grid2]=level_ele[grid2],level_ele[grid1]



