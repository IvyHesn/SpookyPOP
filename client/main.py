# 1 - Import library
import pygame
from pygame.locals import *
from sanxiaoLogic import *

# 2 - Initialize the game
pygame.init()
pygame.display.set_caption('SpookyPOP!') 
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
    #pygame.display.flip()
    
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
            recordMousePos(posX,posY)
            #print (mousePos)
            if isCanExchange(mousePos):
                Exchange(mousePos)
                mousePos=[None,None]

    #绘制选取框
    if mousePos[1]!=None:
        gridX,gridY=getGridXYbyIndexXY(mousePos[1][0],mousePos[1][1])
        screen.blit(chooseframe,(gridX,gridY))
    pygame.display.update()
    #changeGrid(gridIndex,chooseGrid1,chooseGrid2)


