import pygame as py
import random,time

dwidth=1500
dheight=800
display=py.display.set_mode((dwidth,dheight))
clock=py.time.Clock()
py.init()

black=[0,0,0]
green=[0,255,0]
red=[255,0,0]
white=[255,255,255]
blue=[0,0,255]
yellow=[255,255,0]
silver=[200,200,200]
orange=[255,165,0]
darkblue=[0,0,205]

headx,heady=740,400
dx,dy=0,0
size=20
snake=[[headx,heady]]
snakelen=1

apples=[]
applenum=50
for i in range(applenum):
    add=[random.randint(0,dwidth/size)*size,random.randint(0,dheight/size)*size]
    while add in apples:
        add=[random.randint(0,dwidth/size)*size,random.randint(0,dheight/size)*size]
    apples.append(add)

gameexit=False
fps=10
gameover=False
while not gameexit:
    key=False
    for event in py.event.get():
        if event.type==py.QUIT:
            gameexit=True
        elif event.type==py.KEYDOWN:
            if event.key==py.K_UP:
                if dy!=size:
                    dx,dy=0,-size
                    key=True
            elif event.key==py.K_DOWN:
                if dy!=-size:
                    dx,dy=0,size
                    key=True
            elif event.key==py.K_LEFT:
                if dx!=size:
                    dx,dy=-size,0
                    key=True
            elif event.key==py.K_RIGHT:
                if dx!=-size:
                    dx,dy=size,0
                    key=True
            print(event.key)
        
    if len(snake)>1:
        for i in range(len(snake)-2):
            if snake[i]==[headx,heady]:
                gameover=True
                break
    
    if dx!=0 or dy!=0:
        headx+=dx
        heady+=dy
        snake.append([headx,heady])
        py.draw.rect(display,black,(snake[0][0],snake[0][1],size+2,size+2))
    if len(snake)>snakelen:
        del snake[0]
    if headx+size<=0:
        headx=dwidth-size
    elif headx>=dwidth:
        headx=0
    if heady+size<=0:
        heady=dheight-size
    elif heady>=dheight:
        heady=0
        
    for i in apples:
        if i[0]==headx and i[1]==heady:
            py.draw.rect(display,black,(i[0],i[1],size-1,size-1))
            apples.remove(i)
            add=[random.randint(0,dwidth/size)*size,random.randint(0,dheight/size)*size]
            while add in apples:
                add=[random.randint(0,dwidth/size)*size,random.randint(0,dheight/size)*size]
            apples.append(add)
            snakelen+=7
        else:
            py.draw.rect(display,red,(i[0],i[1],size,size))
    
    for i in snake:
        py.draw.rect(display,blue,(i[0],i[1],size,size),2)
    
    if gameover:
        gameover=False
        display.fill(black)
        headx,heady=740,400
        dx,dy=0,0
        snake=[[headx,heady]]
        snakelen=1
    
    py.display.update()
    clock.tick(fps)
    















