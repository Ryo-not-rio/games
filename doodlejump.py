import pygame as py
import time, random

py.init()
displaywidth=600
displayheight=800

display=py.display.set_mode((displaywidth,displayheight))
clock=py.time.Clock()

white=[255,255,255]
black=[0,0,0]
grey=[200,200,200]

    

def game():
    gameover=False
    gameexit=False
    
    global blocks
    blocks=[]
    blockheight=30
    blockwidth=round(displaywidth/4)
    blocknum=6
    for i in range(blocknum):
        blocks.append([random.randint(0,displaywidth-blockwidth),
                       displayheight-blockheight-blockheight*4*i])
    
    usersize=20
    userx=round(displaywidth/2)
    usery=round(displayheight-blockheight-usersize)
    dx=0
    dy=0
    acceleration=0
    dxrate=10 
    
    def movedown(rate,usery):
        delete=[]
        for i in range(len(blocks)):
            minus=blocks[i][1]
            if minus+rate>displayheight:
                delete.append(blocks[i])
            else:
                blocks[i][1]+=rate
        for item in delete:
            blocks.remove(item)
        usery+=rate
        return usery
        
        
       
    
    fps=40
    start=False
    jumpheight=25
    limit=60
    while not gameexit:
        while not gameover:
            display.fill(black)
            for event in py.event.get():
                if event.type==py.QUIT:
                    gameover=True
                    gameexit=True
                elif event.type==py.KEYDOWN:
                    if event.key==py.K_SPACE:
                        if not start:
                            dy=-jumpheight
                            acceleration=1
                            start=True
                    if event.key==py.K_LEFT or event.key==py.K_a:
                        dx=-dxrate
                    if event.key==py.K_RIGHT or event.key==py.K_d:
                        dx=dxrate
                elif event.type==py.KEYUP:
                    if event.key==py.K_LEFT or event.key==py.K_a and dx==-dxrate:
                        dx=0
                    if event.key==py.K_RIGHT or event.key==py.K_d and dx==dxrate:
                        dx=0
            
            if usery-usersize>displayheight:
                gameover=True
            if userx-usersize>=displaywidth:
                userx=0+usersize
            if userx+usersize<=0:
                userx=displaywidth-usersize
            
            userx+=dx
            usery+=dy
            dy+=acceleration
            
            
            if start:
                if usery<displayheight/3:
                    usery=movedown(-dy,usery)
                usery=movedown(1,usery)    
                        
            for i in range(len(blocks)):
                block=blocks[i]
                x=block[0]
                y=block[1]
                if i==len(blocks)-1:
                    if y>limit:
                        blocks.append([random.randint(0,displaywidth-blockwidth),
                       0])
                py.draw.rect(display,grey,(x,y,blockwidth,blockheight))
                if usery+usersize>y and usery+usersize<=y+jumpheight and userx+usersize<x+blockwidth and userx-usersize>x and start:
                    if dy>0:
                        dy=-jumpheight
                        limit+=1
                    
            py.draw.circle(display,white,[userx,usery],usersize)
            py.display.update()
            clock.tick(fps)
        if not gameexit:
            game()
    py.quit()
game()