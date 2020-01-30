import pygame as py
import random,math
py.init()
displaywidth=1500
displayheight=800

display=display=py.display.set_mode((displaywidth,displayheight))
clock=py.time.Clock()


def dist(a,b,c,d):
    distance=math.sqrt((c-a)**2+(d-b)**2)
    return distance


white=[255,255,255]
black=[0,0,0]
yellow=[255,255,0]

def game():
    gap=350
    obstacles=[]
    obswidth=50
    obsspeed=3
    
    edgelimit=50
    xlimit=edgelimit
    ylimit=displayheight-gap-edgelimit
    obsheight=random.randint(xlimit,ylimit)
        
    x=displaywidth
    y=obsheight+gap
    
    birdx=200
    birdy=round(displayheight/2)
    birdsize=10
    birdspeed=1
    orspeed=birdspeed
    birdadd=0
    acceleration=0.012
    
    gameexit=False
    gameover=False
    fps=1
    limit=300
    count=0
    while not gameexit:
        while not gameover:
            display.fill(black)
            for event in py.event.get():
                if event.type==py.QUIT:
                    gameexit=True
                    gameover=True
                elif event.type==py.KEYDOWN:
                    if event.key==py.K_SPACE:
                        if fps<80:
                            fps=80
                        birdspeed=-8
                        birdadd=0
            
            if birdy-birdsize<=0:
                birdspeed=1
            if birdy+birdsize>displayheight:
                gameover=True
            
            count+=1
            if count%limit==0:
                obsheight=random.randint(xlimit,ylimit)
                x=displaywidth
                y=obsheight+gap
                obstacles.append([x,0,obsheight])
                obstacles.append([x,y,displayheight-y])
                count=0
                if gap>240:
                    gap-=8
                if limit>1:
                    limit-=10
                if limit<200 and edgelimit>gap*2:
                    edgelimit+=5
            
            for i in range(len(obstacles)):
                obstacle=obstacles[i]
                x=obstacle[0]
                y=obstacle[1]
                height=obstacle[2]
                py.draw.rect(display,white,(x,y,obswidth,height))
                
                if birdx+birdsize>x and birdx-birdsize<x+obswidth:
                    if y==0:
                        if birdy-birdsize<height:
                            gameover=True
                    else:
                        if birdy+birdsize>y:
                            gameover=True

                obstacle[0]-=obsspeed
                
                
            py.draw.circle(display,yellow,[birdx,birdy],birdsize)
            birdy+=round(birdspeed)
            birdspeed+=birdadd
            birdadd+=acceleration
            
            py.display.update()
        
            clock.tick(fps)
        if not gameexit:
            game()
    py.quit()
    
    
    
game()