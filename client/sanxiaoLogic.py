import pygame
from pygame.locals import *
from config import *

screen=pygame.display.set_mode(screen_size)

#3x logic
#坐标转换
def getGridXYbyPosXY(posX,posY):
    '''根据posX,Y获得gridX,Y'''
    if posY>=324:
        gridX,gridY=posX//65*65,(posY-324)//65*65+324
        return gridX,gridY

def getIndexXYbyPosXY(posX,posY):
    '''根据posX,Y获取格子的索引indexX,Y'''
    iX,iY=posX//65,(posY-324)//65
    return iX,iY

def getGridXYbyIndexXY(iX,iY):
    '''根据格子IndexXY，获取所在格子的gridXY'''
    gridX,gridY=iX*65,iY*65+324
    return gridX,gridY

def getGridIndex(posX,posY):
    '''根据鼠标位置posX,Y判断所在格gridIndex'''
    if posY>=324:
        gridX,gridY=posX//65,(posY-324)//65
        gridIndex=gridX+7*gridY
        return gridIndex
    else:
        return None

def recordMousePos(posX,posY):
    '''记录最近2次鼠标点击格子区域的gridXY in mousePos'''
    if posY>=324:
        iX,iY=getIndexXYbyPosXY(posX,posY)
        if mousePos[1]==None:
            mousePos[1]=(iX,iY)
        else:
            mousePos[0]=mousePos[1]
            mousePos[1]=(iX,iY)
        return mousePos

def isCanExchange(mousePos):
    '''判断是否可以交换'''
    if mousePos[0]!=None:
        return True
    else:
        return False

def Exchange(mousePos):
    '''交换格子里的元素'''
    i1,i2=mousePos[0][0]+7*mousePos[0][1],mousePos[1][0]+7*mousePos[1][1]
    #print (i1,i2)
    level_ele[i1],level_ele[i2]=level_ele[i2],level_ele[i1]

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

def chooseFrame(gridIndex):
    pass

'''       
def changeGrid(gridIndex,chooseGrid1=None,chooseGrid2=None):
    if gridIndex!=None:
        #判断选取状态
        if chooseGrid1==None:
            chooseGrid1=gridIndex#更新gridIndex
            screen.blit(chooseframe,getGridXYbyGridIndex(gridIndex))
            pygame.display.flip()
            #break
        if chooseGrid1!=None:
            #判断是否可以交换
            chooseGrid2=gridIndex
            if ischangeGrid(chooseGrid1,chooseGrid2)==True:
                screen.blit(chooseframe,getGridXYbyGridIndex(gridIndex))
                pygame.display.flip()
                level_ele[chooseGrid1],level_ele[chooseGrid2]=level_ele[chooseGrid2],level_ele[chooseGrid1]
                chooseGrid1,chooseGrid2=None,None#初始化选取状态
                #break
            if ischangeGrid(chooseGrid1,chooseGrid2)==False:
                screen.blit(chooseframe,getGridXYbyGridIndex(gridIndex))
                pygame.display.flip()
                chooseGrid1=chooseGrid2#更新选取的格子
                #break
'''

