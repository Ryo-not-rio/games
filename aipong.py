import pygame as py
import random
import math


dwidth,dheight=1000,800
display=py.display.set_mode((dwidth,dheight))
clock=py.time.Clock()
py.init()

def distance(a,b,c,d):
    return math.sqrt((c-a)**2+(d-b)**2)

def updateupos():
    global urect
    global uxv
    
    urect.x+=uxv
    
    if urect.x+uwidth>dwidth or urect.x<0:
        uxv=0

def drawline(y):
    if ballvy<0:
        m=ballvy/(ballvx+0.01)
        c=bally-m*ballx
        return int((y-c)/m)
    else:
        return ballx

def updateenemypos():
    global enemyurect
    global enemyvx
        
    if enemyvx=="AI":
        if enemyurect.x>0 and enemyurect.x+uwidth<dwidth:
            if ballvy<0:
                target=drawline(20+uheight)
                if target<0:
                    target*=-1
                elif target>dwidth:
                    target=2*dwidth-target
                difference=target-enemyurect.x-uwidth/2
            else:
                difference=dwidth/2-enemyurect.x-uwidth/2
                
            if difference<-5:
                enemyurect.x-=velocity
            elif difference>5:
                enemyurect.x+=velocity
        else:
            if enemyurect.x<0:
                enemyurect.x=1
            else:
                enemyurect.x=dwidth-uwidth-1
    else:
        enemyurect.x+=enemyvx 
        if enemyurect.x+uwidth>dwidth or enemyurect.x<0:
            enemyvx=0           
    

def updateballpos():
    global ballx
    global bally
    global ballvx
    global ballvy
    global bounce
    global fps
    global uscore
    global enemyscore
    global label1
    global label2
    
    
    if ballx<radius or ballx+radius>dwidth:
        ballvx*=-1
        bounce+=1
    
    if urect.collidepoint((ballx,bally)) or enemyurect.collidepoint((ballx,bally)):
        ballvy*=-1
        bally+=ballvy
        ballvx+=random.randint(-2,2)
        bounce+=1

    if (bounce+1)%10==0:
        if random.randint(0,100)<30:
            if ballvy<=0:
                ballvy-=1
            else:
                ballvy+=1
        else:
            fps+=5
        bounce+=1

    ballx+=ballvx
    bally+=ballvy
    
    if bally<0:
        uscore+=1
        label1=font.render(str(uscore),False,py.Color("white"))
        reset()

    elif bally>dheight:
        enemyscore+=1
        label2=font.render(str(enemyscore),False,py.Color("white"))
        reset()
    
def reset():
    global ux
    global uy
    global urect
    global uxv
    global enemyux
    global enemyuy
    global enemyurect
    global ballx
    global bally
    global ballvx
    global ballvy
    global bounce
    global fps
    global enemyvx
    
    ux,uy=int(dwidth/2-uwidth/2),dheight-20-uheight
    urect=py.Rect(ux,uy,uwidth,uheight)
    uxv=0
    
    
    enemyux,enemyuy=ux,20
    enemyurect=py.Rect(enemyux,enemyuy,uwidth,uheight)
    enemyvx="AI"
    
    ballx,bally=int(dwidth/2),radius+20+uheight
    ballvx,ballvy=-0,0
    
    bounce=0
    
    fps=60
    
uwidth,uheight=180,25
uscore=0
enemyscore=0

velocity=6



radius=10


gameexit=False

fontsize=70
font=py.font.Font(None,fontsize)

reset()
label1=font.render(str(uscore),False,py.Color("white"))
label2=font.render(str(enemyscore),False,py.Color("white"))

while not gameexit:
    display.fill(py.Color("black"))
    for event in py.event.get():
        if event.type==py.QUIT:
            gameexit=True
        if event.type==py.KEYDOWN:
            if event.key==py.K_RIGHT and urect.x+uwidth<dwidth:
                uxv=velocity
            elif event.key==py.K_LEFT and urect.x>0:
                uxv=-velocity
                
            if event.key==py.K_d and enemyurect.x+uwidth<dwidth:
                enemyvx=velocity
            elif event.key==py.K_a and enemyurect.x>0:
                enemyvx=-velocity
            
        elif event.type==py.KEYUP:
            if event.key==py.K_RIGHT and uxv==velocity:
                uxv=0
            elif event.key==py.K_LEFT and uxv==-velocity:
                uxv=0
            elif event.key==py.K_SPACE and ballvy==0:
                ballvx,ballvy=-5,5
                
            if event.key==py.K_d and enemyvx==velocity:
                enemyvx=0
            elif event.key==py.K_a and enemyvx==-velocity:
                enemyvx=0
        
    updateupos()
    updateenemypos()

    
    updateballpos()
    
    py.draw.circle(display,py.Color("yellow"),(ballx,bally),radius)
    py.draw.rect(display,py.Color("gray"),urect)
    py.draw.rect(display,py.Color("gray"),enemyurect)
    
    display.blit(label1,(int(dwidth/2),int(dheight/2+fontsize)))
    display.blit(label2,(int(dwidth/2),int(dheight/2-fontsize)))
    
    #py.draw.line(display,py.Color("red"),(ballx,bally),(drawline(0),0),2)
    
    py.display.update()    
    clock.tick(fps)
    #print(clock.get_fps())



























