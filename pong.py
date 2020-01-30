import pygame as py
import time,random

py.init()
displaywidth=1500
displayheight=800

display=display=py.display.set_mode((displaywidth,displayheight))
clock=py.time.Clock()


black=[0,0,0]
white=[255,255,255]
gray=[200,200,200]
mincolour=150

def game():
    gameexit=False
    gameover=False
    
    userheight=30
    userwidth=200
    userx=round(displaywidth/2-userwidth/2)
    usery=displayheight-userheight*2
    dx=0
    
    ballsize=20
    ballx=userx+round(userwidth/2)
    bally=usery-ballsize
    balldx=0
    balldy=0
    
    blockrows=3
    blockcolumns=20
    blockheight=20
    blockwidth=round(displaywidth/blockcolumns)
    blocks=[]
    for i in range(blockrows):
        blocks.append([])
    for a in range(blockrows):
        for b in range(blockcolumns):
            colour=[random.randint(mincolour,255),random.randint(mincolour,255),random.randint(mincolour,255)]
            blocks[a].append([b+b*blockwidth,a+a*blockheight,colour])
        
    
    while not gameexit:
        while not gameover:
            display.fill(black)
            for event in py.event.get():
                if event.type==py.QUIT:
                    gameexit=True
                    gameover=True
                if event.type==py.KEYDOWN:
                    if event.key==py.K_RIGHT or event.key==py.K_d:
                        if userx+userwidth<displaywidth:
                            userx+=2
                            dx=2
                    elif event.key==py.K_LEFT or event.key==py.K_a:
                        if userx>0:
                            userx-=2
                            dx=-2
                    if event.key==py.K_SPACE and balldx==0:
                        balldx=2
                        balldy=-2
                elif event.type==py.KEYUP:
                    if event.key==py.K_RIGHT or event.key==py.K_d or event.key==py.K_LEFT or event.key==py.K_a:
                        dx=0
            
            if userx<=0 or userx+userwidth>=displaywidth:
                dx=0
            
            userx+=dx
            ballx+=balldx
            bally+=balldy
            
            if ballx+ballsize>=userx and ballx-ballsize<=userx+userwidth and bally+ballsize>=usery and bally-ballsize<=usery+userheight:
                balldy*=-1
            if ballx-ballsize<=0 or ballx+ballsize>=displaywidth:
                balldx*=-1
                
            if bally>=displayheight:
                gameover=True
            
            py.draw.circle(display,gray,[ballx,bally],ballsize)##ball
            py.draw.rect(display,white,(userx,usery,userwidth,userheight))##user
            
            dead=[]
            for a in range(len(blocks)):
                for b in range(len(blocks[a])):
                    block=blocks[a][b]
                    x=block[0]
                    y=block[1]
                    colour=block[2]
                    
                    if ballx+ballsize>=x and ballx-ballsize<x+blockwidth and bally+ballsize>=y and bally-ballsize<=y+blockheight:
                        balldy*=-1
                        dead.append([a,b])
                    py.draw.rect(display,colour,(x,y,blockwidth,blockheight))
            for i in dead:
                a=i[0]
                b=i[1]
                del blocks[a][b]
            
            py.display.update()
            
        if not gameexit:
            game()
    py.quit()
    
game()