import pygame as py,random,time


dwidth,dheight=1500,800
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

def creategoal(num):
    operators=["+","-","*","/"]
    yay=False
    ornum=num[:]
    def addops(numlist):
        for i in range(1,len(numlist)+len(numlist)-1,2):
            numlist.insert(i,random.choice(operators))
        ornumlist=numlist[:]
        if len(numlist)>0:
            try:
                numlist=eval("".join(numlist))
                answers.append("".join(ornumlist))
            except:
                numlist=["1","/","3"]
            return numlist
        else:
            del numlist
    def brackets(numb):
        global answers
        answers=[]
        while len(numb)>1:
            bracketnum=random.randint(1,len(numb))
            newnum=[]
            for i in range(bracketnum):
                newnum.append([])
            for i in numb:
                random.choice(newnum).append(i)
            numb=list(map(addops,newnum))
            answers.append("|")
            numb=list(filter(None.__ne__, numb))
            numb=list(map(lambda x: str(x),numb))
        return "".join(numb),answers    
            
    while not yay:  
        num=ornum  
        random.shuffle(num)
        num=list(map(lambda x:str(x),num))
        num,method=brackets(num)
        integer=False
        try:
            int(num)
            integer=True
        except:
            None
        if integer:
            if len(list(num))==3 and int(num)>0:
                yay=True
    return num,method
            
gameexit=False

fontsize=120
font=py.font.SysFont(None,fontsize)
numbers=[]
goal=0

reset=False
while not gameexit:
    if reset:
        small=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        big=[25,50,75,100]
        display.fill(black)
        numbers=[]
        for i in range(biglen):
            add=random.choice(big)
            big.remove(add)
            numbers.append(add)
        for i in range(6-biglen):
            add=random.choice(small)
            small.remove(add)
            numbers.append(add)
        goal,method=creategoal(numbers[:])
        reset=False
    for event in py.event.get():
        if event.type==py.QUIT:
            gameexit=True
        elif event.type==py.KEYDOWN:
            if event.key==py.K_0:
                reset=True
                biglen=0
            elif event.key==py.K_1:
                reset=True
                biglen=1
            elif event.key==py.K_2:
                reset=True
                biglen=2
            elif event.key==py.K_3:
                reset=True
                biglen=3
            elif event.key==py.K_4:
                reset=True
                biglen=4
            elif event.key==py.K_SPACE:
                reset=True
                biglen=random.randint(0,4)
            elif event.key==py.K_RETURN:
                font=py.font.SysFont(None,60)
                label=font.render(", ".join(method),False,yellow)
                display.blit(label,(0,0))
                font=py.font.SysFont(None,fontsize)
    
    label=font.render(str(goal),False,white)
    display.blit(label,(dwidth/2-round(fontsize/3),round(dheight/3)))
    
    for i in range(len(numbers)):
        label=font.render(str(numbers[i]),False,white)
        display.blit(label,((i+1)*125+i*125-fontsize/4,dheight/2+125-fontsize/4))
        py.draw.rect(display,white,(i*250,dheight/2,250,250),3)        
    py.display.update()











