import pygame as py
import random,math

py.init()
py.font.init()
font=py.font.SysFont(None,40)

displaywidth=1500
displayheight=800
fps=100
display=py.display.set_mode((displaywidth,displayheight))
clock=py.time.Clock()

black=[0,0,0]
white=[255,255,255]
blue=[100,100,255]
red=[255,0,0]
green=[0,255,0]
silver=[200,200,200]
enemycolours=[blue,red,green]

staticlist=[]
totalpixels=displayheight*displaywidth
staticnum=round(totalpixels/700)
staticspeed=3
valuemax=100
for a in range(random.randint(100,staticnum)):
    value=random.randint(0,valuemax)
    staticlist.append([random.randint(0,displaywidth),random.randint(0,displayheight),
                       [value,value,value],random.randint(1,7)])

def message_to_screen(msg,colour):
    font=py.font.SysFont(None,80)
    screen_text=font.render(msg,True,colour)
    display.blit(screen_text,[displaywidth/2-screen_text.get_width()/2,displayheight/2-screen_text.get_height()/2])

def distance(a,b):
    x1=a[0]
    x2=b[0]
    y1=a[1]
    y2=b[1]
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist


shipwidth=40
shipheight=60
shipx=round(displaywidth/2)
shipy=displayheight-shipheight*2
orshipy=shipy
dx=0

bulletlist=[]
enemybullets=[]
enemybulletsize=4
possibility=1

enemymove=1
enemynum=30
enemysize=20
enemylist=[]
moverate=2


for i in range(enemynum):
    x=i*enemysize*2+enemysize
    y=enemysize*2
    ory=y
    enemylist.append([x,y,random.choice(enemycolours)])


gameexit=False
gameover=False
shoot=0
shootrate=10
shootbool=False
bulletsize=5
bulletspeed=3
level=1
while not gameexit:
    while not gameover:
        if len(enemylist)>0:
            display.fill(black)
            for event in py.event.get():
                if event.type==py.QUIT:
                    gameexit=True
                    gameover=True
                if event.type==py.KEYDOWN:
                    if event.key==py.K_RIGHT or event.key==py.K_d:
                        dx=moverate
                    if event.key==py.K_LEFT or event.key==py.K_a:
                        dx=-1*moverate
                    if event.key==py.K_SPACE:
                        b=False
                        while True:
                            for event in py.event.get():
                                if event.type==py.QUIT:
                                    gameover=True
                                    gameexit=True
                                    b=True
                                if event.type==py.KEYDOWN:
                                    if event.key==py.K_SPACE:
                                        b=True
                            if b:
                                break
                if event.type==py.KEYUP:
                    if event.key==py.K_RIGHT or event.key==py.K_d and dx>0:
                        dx=0
                    if event.key==py.K_LEFT or event.key==py.K_a and dx<0:
                        dx=0
        
        
            shoot+=shootrate
            if round(shoot)%500==0:
                add=[shipx,shipy]
                bulletlist.append(add)
                
            for a in range(len(staticlist)):
                static=staticlist[a]
                py.draw.circle(display,static[2],[static[0],static[1]],static[3])
                if static[1]<displayheight:
                    staticlist[a][1]+=round(staticspeed)
                else:
                    staticlist.remove(static)
                    value=random.randint(0,valuemax)
                    staticlist.append([random.randint(0,displaywidth),0,
                       [value,value,value],random.randint(1,7)])
                        
            if shipx-shipwidth/2+dx<enemysize or shipx+shipwidth/2+dx>displaywidth-enemysize:
                dx=0
            shipx+=dx
                
            i=0 
            for s in range(len(bulletlist)):
                removed=False
                bullet=bulletlist[i]
                x=bullet[0]
                y=bullet[1]
                for j in enemylist:
                    dist=distance(bullet,j)
                    if dist<bulletsize+enemysize:
                        enemylist.remove(j)
                        bulletlist.remove(bullet)
                        removed=True
                if not removed:
                    if y<0:
                        bulletlist.remove(bullet)
                        removed=True
                    else:
                        if len(bulletlist)<1:
                            break
                        py.draw.circle(display,silver,
                                       [x,y],bulletsize)
                        bulletlist[i][1]=y-bulletspeed
                        if i+1==len(bulletlist):
                            break
                        else:
                            i+=1
                        
            ##  enemy bullets
            i=0 
            for s in range(len(enemybullets)):
                removed=False
                ebullet=enemybullets[i]
                ex=ebullet[0]
                ey=ebullet[1]
                colour=ebullet[2]
                if colour[0]>200:
                    enemybulletspeed=9
                elif colour[2]>200:
                    enemybulletspeed=7
                else:
                    enemybulletspeed=5
                dist=distance(ebullet,[shipx,shipy])
                if dist<bulletsize+10:
                    gameover=True
                if not removed:
                    if ey>displayheight:
                        enemybullets.remove(ebullet)
                        removed=True
                    else:
                        if len(enemybullets)<1:
                            break
                        py.draw.circle(display,colour,
                                       [ex,ey],round(enemybulletsize))
                        enemybullets[i][1]=ey+enemybulletspeed
                        if i+1==len(enemybullets):
                            break
                        else:
                            i+=1
                   
                
            ##ship
            py.draw.polygon(display,white,
                         [[shipx,shipy],
                          [shipx-round(shipwidth/2),shipy+shipheight],
                          [shipx+round(shipwidth/2),shipy+shipheight]])
            
            ##enemies
            if len(enemylist)>0:
                leftedgex=enemylist[0][0]
                rightedgex=enemylist[len(enemylist)-1][0]
                
                
                for i in range(len(enemylist)):
                    enemy=enemylist[i]
                    x,y=enemy[0],enemy[1]
                    colour=enemy[2]
                    shootchoice=random.randint(0,1000)
                    if shootchoice<possibility:
                        enemybullets.append([x,y,colour])
                    py.draw.circle(display,colour,
                                   [x,y],enemysize)
                    if leftedgex+enemymove-enemysize>0 and rightedgex+enemymove+enemysize<displaywidth:
                        enemylist[i][0]+=enemymove
                    else:
                        enemymove*=-1
                    
                
                
            py.display.update()
            clock.tick(fps)
        else:
            fps+=10
            possibility+=0.20
            level+=1
            staticspeed+=0.8
            
            for i in range(enemynum):
                x=i*enemysize*2+enemysize
                y=ory
                enemylist.append([x,y,random.choice(enemycolours)])
    

    display.fill(blue)
    for event in py.event.get():
        if event.type==py.QUIT:
            gameexit=True
        if event.type==py.KEYDOWN:
            if event.key==py.K_SPACE:
                gameover=False
                level=1
                shipx=round(displaywidth/2)
                shipy=orshipy
                dx=0
                bulletlist=[]
                enemybullets=[]
                possibility=1
                enemynum=30
                enemylist=[]
                fps=100
                for i in range(enemynum):
                    x=i*enemysize*2+enemysize
                    y=ory
                    enemylist.append([x,y,random.choice(enemycolours)])
                
    show="you got to level "+str(level)
    message_to_screen(show,white)
    py.display.update()
            
    
    
py.quit()







