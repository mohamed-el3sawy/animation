from graphics import *

class Player:
    def __init__(self,screen,context,color,direction):
        self.screen = screen
        self.ctx = context
        self.color = color
        self.dir = direction
        
    def head(self):
        self.head = Circle(self.ctx, 24)
        self.head.setOutline(self.color)
        self.head.setFill(self.color)
        self.head.draw(self.screen)
        return self.head
        
    def body(self):
        self.body = Line(
    	    Point(self.ctx.getX()-10 if self.dir =='R' else self.ctx.getX()+10, self.ctx.getY()),
    	    Point(self.ctx.getX()+5 if self.dir =='R' else self.ctx.getX()-5, self.ctx.getY()+100))
        self.body.setOutline(self.color)
        self.body.setWidth(16)
        self.body.draw(self.screen)
        return self.body
        
    def leftHand(self):
        self.lhand = Line(
            Point(self.ctx.getX()-10 if self.dir =='R' else self.ctx.getX()+10, self.ctx.getY()),
            Point(self.ctx.getX()+6 if self.dir =='R' else self.ctx.getX()-6, self.ctx.getY()+55),)
        self.ldhand = Line(
            Point(self.ctx.getX()+6 if self.dir =='R' else self.ctx.getX()-6, self.ctx.getY()+55),
    	    Point(self.ctx.getX()+14 if self.dir =='R' else self.ctx.getX()-14, self.ctx.getY()+105))
        self.lhand.setOutline('#B40707' if self.color == 'red' else '#280000')
        self.lhand.setWidth(10)
        self.lhand.draw(self.screen)
        self.ldhand.setOutline('#B40707' if self.color == 'red' else '#280000')
        self.ldhand.setWidth(10)
        self.ldhand.draw(self.screen)
        return self.lhand, self.ldhand
        
    def rightHand(self):
        self.rhand = Line(
            Point(self.ctx.getX()-12 if self.dir =='R' else self.ctx.getX()+12, self.ctx.getY()),
            Point(self.ctx.getX()-14 if self.dir =='R' else self.ctx.getX()+12, self.ctx.getY()+55),)
        self.rdhand = Line(
            Point(self.ctx.getX()-14 if self.dir =='R' else self.ctx.getX()+12, self.ctx.getY()+55),
    	    Point(self.ctx.getX()-10 if self.dir =='R' else self.ctx.getX()+10, self.ctx.getY()+110))
        self.rhand.setOutline(self.color)
        self.rhand.setWidth(10)
        self.rhand.draw(self.screen)
        self.rdhand.setOutline(self.color)
        self.rdhand.setWidth(10)
        self.rdhand.draw(self.screen)
        return self.rhand, self.rdhand
        
    def leftLeg(self):
        self.lleg = Line(
            Point(self.ctx.getX()+5 if self.dir =='R' else self.ctx.getX()-5, self.ctx.getY()+100),
            Point(self.ctx.getX()+15 if self.dir =='R' else self.ctx.getX()-15, self.ctx.getY()+155),)
        self.ldleg = Line(
            Point(self.ctx.getX()+15 if self.dir =='R' else self.ctx.getX()-15, self.ctx.getY()+155),
            Point(self.ctx.getX()+25 if self.dir =='R' else self.ctx.getX()-25, self.ctx.getY()+210))
        self.lleg.setOutline('#B40707' if self.color == 'red' else '#280000')
        self.lleg.setWidth(13)
        self.lleg.draw(self.screen)
        
        self.ldleg.setOutline('#B40707' if self.color == 'red' else '#280000')
        self.ldleg.setWidth(13)
        self.ldleg.draw(self.screen)
        
        return self.lleg, self.ldleg
        
    def rightLeg(self):
        self.rleg = Line(
            Point(self.ctx.getX()+6 if self.dir =='R' else self.ctx.getX()-6, self.ctx.getY()+100),
            Point(self.ctx.getX()-2 if self.dir =='R' else self.ctx.getX()+2, self.ctx.getY()+155))
        self.rdleg = Line(
            Point(self.ctx.getX()-2 if self.dir =='R' else self.ctx.getX()+2, self.ctx.getY()+155),
            Point(self.ctx.getX()-10 if self.dir =='R' else self.ctx.getX()+10, self.ctx.getY()+210))
        self.rleg.setOutline(self.color)
        self.rleg.setWidth(13)
        self.rleg.draw(self.screen)
        self.rdleg.setOutline(self.color)
        self.rdleg.setWidth(13)
        self.rdleg.draw(self.screen)
        return self.rleg, self.rdleg
        
    def moveAll(self,x,y):
        self.head.move(x,y)
        self.ctx.move(x,y)
        self.body.move(x,y)
        self.lhand.move(x,y)
        self.ldhand.move(x,y)
        self.rhand.move(x,y)
        self.rdhand.move(x,y)
        self.lleg.move(x,y)
        self.ldleg.move(x,y)
        self.rleg.move(x,y)       
        self.rdleg.move(x,y)    
        
    def moveHead(self,dx,dy):
        self.head.move(dx,dy)
        self.ctx.move(dx,dy)
        
    def moveBody(self, slope, tallness=100, ifsleep = 0):    
        self.body.undraw()
        self.body.p1 = Point(self.ctx.getX()-8 if self.dir =='R' else self.ctx.getX()+8, self.ctx.getY()+ifsleep)
        self.body.p2 = Point(self.ctx.getX()-slope if self.dir =='R' else self.ctx.getX()+slope, self.ctx.getY()+tallness)
        self.body.draw(screen)
        
    def moveLeftHand(self,p2,p3,ifSleepy = 20, ifSleepx = 10):    
        self.lhand.undraw()
        self.ldhand.undraw()
        self.lhand = Line(
    	    Point(self.ctx.getX()-ifSleepx if self.dir =='R' else self.ctx.getX()+ifSleepx, self.ctx.getY()+ifSleepy),p2)
        self.ldhand = Line(p2,p3)
        self.lhand.setOutline(self.color)
        self.ldhand.setOutline(self.color)
        self.lhand.setWidth(10)
        self.ldhand.setWidth(10)
        self.lhand.draw(screen)    
        self.ldhand.draw(screen) 
        
    def moveRightHand(self,p2,p3,ifSleepy = 15,ifSleepx = 12):    
        self.rhand.undraw()
        self.rdhand.undraw()
        self.rhand = Line(
    	    Point(self.ctx.getX()-ifSleepx if self.dir =='R' else self.ctx.getX()+ifSleepx, self.ctx.getY()+ifSleepy),p2)
        self.rdhand = Line(p2,p3)
        self.rhand.setOutline(self.color)
        self.rdhand.setOutline(self.color)
        self.rhand.setWidth(10)
        self.rdhand.setWidth(10)
        self.rhand.draw(screen)    
        self.rdhand.draw(screen)     
        
    def moveLeftLeg(self,p2,p3):    
        self.lleg.undraw()
        self.ldleg.undraw()
        self.lleg = Line(self.body.getP2(),p2)
        self.ldleg = Line(p2,p3)
        self.lleg.setOutline(self.color)
        self.ldleg.setOutline(self.color)
        self.lleg.setWidth(13)
        self.ldleg.setWidth(13)
        self.lleg.draw(screen)    
        self.ldleg.draw(screen)     
        
    def moveRightLeg(self,p2,p3):    
        self.rleg.undraw()
        self.rdleg.undraw()
        self.rleg = Line(self.body.getP2(),p2)
        self.rdleg = Line(p2,p3)
        self.rleg.setOutline(self.color)
        self.rdleg.setOutline(self.color)
        self.rleg.setWidth(13)
        self.rdleg.setWidth(13)
        self.rleg.draw(screen)    
        self.rdleg.draw(screen)         
        
    def undrawAll(self):
        self.head.undraw()
        self.body.undraw()
        self.rhand.undraw()    
        self.rdhand.undraw()    
        self.lhand.undraw()    
        self.ldhand.undraw()    
        self.lleg.undraw()    
        self.ldleg.undraw()    
        self.rleg.undraw()    
        self.rdleg.undraw()    

def land(points, color):
    div = Polygon(points)
    div.setOutline(color)
    div.setFill(color)
    div.draw(screen)   
    return div                   
   
def lightningElement(p1,p2,width):
    l = Line(p1, p2)
    l.setOutline('white')
    l.setWidth(width)
    l.draw(screen)
    return l   

def lightning1():
    l1 = lightningElement(Point(200, 0),Point(230, 20), 7)
    l2 = lightningElement(Point(230, 20),Point(280, 100), 6)
    l3 = lightningElement(Point(280, 100),Point(270, 120), 6)
    l4 = lightningElement(Point(270, 120),Point(265, 150), 5)
    l5 = lightningElement(Point(265, 150),Point(295, 200), 5)
    l6 = lightningElement(Point(295, 200),Point(300, 300), 4)
    return l1,l2,l3,l4,l5,l6

def lightning2():
    l1 = lightningElement(Point(500, 0),Point(430, 30), 7)
    l2 = lightningElement(Point(430, 30),Point(400, 100), 6)
    l3 = lightningElement(Point(400, 100),Point(450, 150), 6)
    l4 = lightningElement(Point(450, 150),Point(490, 200), 5)
    l5 = lightningElement(Point(490, 200),Point(520, 250), 5)
    l6 = lightningElement(Point(520, 250),Point(550, 295), 4)     
    return l1,l2,l3,l4,l5,l6

def lightning3():
    l1 = lightningElement(Point(490, 200),Point(450, 280), 7)
    l2 = lightningElement(Point(450, 280),Point(500, 295), 5)     
    return l1,l2    

def boom(x,y):
    p = Polygon(Point(x,y), Point(x+15,y-4), Point(x+10,y+4), Point(x+18,y+8), Point(x+9, y+12),Point(x+1,y+12))     
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(screen)
    return p

def boom2(x,y):
    p = Polygon(Point(x,y), Point(x-15,y+4), Point(x-10,y-4), Point(x-18,y-8), Point(x-9, y-12),Point(x-1,y-12))     
    p.setFill('gray')
    p.setOutline('gray')
    p.draw(screen)
    return p   
     
def boom3(x,y,r):
    c = Circle(Point(x,y), r)
    c.setFill('#0D30D8')
    c.setOutline('#0D30D8')
    c.draw(screen)
    return c
        
def boom4(x,y):
    p = Polygon(Point(x,y),Point(x+8,y-20),Point(x+8,y+20),Point(x+10,y-17),Point(x+20,y-4),Point(x-10,y+8))
       
######### The Start ##########       
        
screen = GraphWin("Lol",1000,600) 

land = land([Point(0, 300), Point(1000, 300), Point(1000, 600), Point(0, 600)], color_rgb(218,216,214))

p1 = Player(screen,Point(200,200),'red','R')
p1.head()
p1.leftHand()
p1.body()
p1.rightHand()
p1.leftLeg()
p1.rightLeg()

p2 = Player(screen,Point(800,200),'black','L')
p2.head()
p2.leftHand()
p2.body()
p2.rightHand()
p2.leftLeg()
p2.rightLeg()

for i in range(11):
    p1.moveAll(0,7)
    p2.moveAll(0,7)
    time.sleep(0.04)
    p1.moveAll(0,-7)
    p2.moveAll(0,-7)
    time.sleep(0.04)
    if i == 5:
        screen.setBackground(color_rgb(100,100,100))
        land.setFill(color_rgb(80,80,80))
        land.setOutline(color_rgb(80,80,80))    
    if i == 6:
        light1 = lightning1()   
        screen.setBackground(color_rgb(100,100,100))
    if i == 9:
        for j in range(6):
            light1[j].undraw()
    
for i in range(13):
    p1.moveAll(0,10)
    p2.moveAll(0,10)
    time.sleep(0.04)
    p1.moveAll(0,-10)
    p2.moveAll(0,-10)
    time.sleep(0.04)    
    if i == 2:
        screen.setBackground(color_rgb(100,100,100))
        land.setFill(color_rgb(80,80,80))
        land.setOutline(color_rgb(80,80,80))    
    if i == 6:
        light1 = lightning1()   
        light2 = lightning2()
    if i == 8:
        light3 = lightning3()    
    if i == 10:
        for j in range(6):
            light1[j].undraw()
            light2[j].undraw()
        light3[0].undraw()
        light3[1].undraw()
        screen.setBackground('white')
        land.setFill(color_rgb(218,216,214))
        land.setOutline(color_rgb(218,216,214))
    
p1.moveAll(170,0)

p2.moveLeftHand(Point(p2.ctx.getX()+40, 255),Point(p2.ctx.getX()+10, 310))
p2.moveBody(35)
p2.moveRightHand(Point(p2.ctx.getX()+10, 255),Point(p2.ctx.getX()-25, 300))
p2.moveLeftLeg(Point(p2.ctx.getX()+50, 350),Point(p2.ctx.getX()+75, 400))
p2.moveRightLeg(Point(p2.ctx.getX()-1, 350),Point(p2.ctx.getX()+45, 400))

p2.moveAll(-170,0)

p1.moveLeftHand(Point(p1.ctx.getX()-40, 255),Point(p1.ctx.getX()-10, 310))
p1.moveBody(35)
p1.moveRightHand(Point(p1.ctx.getX()-10, 255),Point(p1.ctx.getX()+25, 300))
p1.moveLeftLeg(Point(p1.ctx.getX()-50, 350),Point(p1.ctx.getX()-75, 400))
p1.moveRightLeg(Point(p1.ctx.getX()+1, 350),Point(p1.ctx.getX()-45, 400))

p1.moveAll(50, 0)
p2.moveAll(-50,0)
time.sleep(0.18)

p1.moveLeftHand(Point(p1.ctx.getX()-45, 240),Point(p1.ctx.getX()-15, 200))
p1.moveBody(-5)
p1.moveRightHand(Point(p1.ctx.getX()+40, 230),Point(p1.ctx.getX()+80, 220))
p1.moveLeftLeg(Point(p1.ctx.getX()+15, 350),Point(p1.ctx.getX()+20, 400))
p1.moveRightLeg(Point(p1.ctx.getX()-15, 350),Point(p1.ctx.getX()-30, 400))

p2.moveAll(-30,0)
p1.moveAll(35,0)
time.sleep(0.18)

p2.moveBody(-10)
p2.moveRightHand(Point(p2.ctx.getX()-15, 240),Point(p2.ctx.getX()-25, 190))
p2.moveLeftHand(Point(p2.ctx.getX()-20, 245),Point(p2.ctx.getX()-26, 180))
p2.moveRightLeg(Point(p2.ctx.getX()-15, 350),Point(p2.ctx.getX()-15, 400))
p2.moveLeftLeg(Point(p2.ctx.getX()+5, 350),Point(p2.ctx.getX()+10, 370))

bm1 = boom(520,220)
time.sleep(0.18)
bm1.undraw()

p1.moveLeftHand(p1.ctx, p1.ctx)
p1.moveRightHand(p1.ctx, p1.ctx)
p1.moveHead(-15,-20)
p1.moveBody(-20, 70)
p1.moveLeftLeg(Point(p1.ctx.getX()-7, 350),Point(p1.ctx.getX()-18, 400))
p1.moveRightLeg(Point(p1.ctx.getX()+23, 210),Point(p1.ctx.getX()+32, 140))

time.sleep(0.18)

p2.moveBody(-20)
p2.moveRightHand(p2.ctx,p2.ctx)
p2.moveLeftHand(Point(p2.ctx.getX()+15, 255),Point(p2.ctx.getX()-40, 240))
p2.moveRightLeg(Point(p2.ctx.getX()-20, 350),Point(p2.ctx.getX()-5, 400))
p2.moveLeftLeg(Point(p2.ctx.getX()-40, 350),Point(p2.ctx.getX()-50, 400))

time.sleep(0.18)

p1.moveHead(0,5)
p1.moveLeftHand(p1.ctx,p1.ctx)
p1.moveRightHand(Point(p1.ctx.getX()+20, 180), Point(p1.ctx.getX()+25, 150))
p1.moveHead(-15,-20)
p1.moveBody(-20, 70)
p1.moveLeftLeg(Point(p1.ctx.getX()-7, 350),Point(p1.ctx.getX()-18, 400))
p1.moveRightLeg(Point(p1.ctx.getX()+35, 270),Point(p1.ctx.getX()+75, 370))

bm1 = boom(500,370)
time.sleep(0.18)
bm1.undraw()

p1.moveHead(-20,20)
p1.moveLeftHand(p1.ctx,p1.ctx)
p1.moveRightHand(Point(p1.ctx.getX()+20, 220), Point(p1.ctx.getX()+25, 155))
p1.moveBody(10, 100)
p1.moveLeftLeg(Point(p1.ctx.getX()+10, 350),Point(p1.ctx.getX()+5, 400))
p1.moveRightLeg(Point(p1.ctx.getX()+15, 300),Point(p1.ctx.getX()+23, 350))

p2.moveAll(-24,0)
p2.moveHead(-25,0)
p2.moveBody(28)
p2.moveRightHand(Point(p2.ctx.getX()-35, 200),Point(p2.ctx.getX()-70, 190))
p2.moveLeftHand(Point(p2.ctx.getX()+40, 220),Point(p2.ctx.getX()-25, 240))
p2.moveRightLeg(Point(p2.ctx.getX()+20, 350),Point(p2.ctx.getX()+40, 400))
p2.moveLeftLeg(Point(p2.ctx.getX()+10, 350),Point(p2.ctx.getX()+50, 370))

bm2 = boom2(435,190)
time.sleep(0.18)
bm2.undraw()

p2.moveRightHand(Point(p2.ctx.getX()-35, 240),Point(p2.ctx.getX()-70, 260))
p2.moveLeftHand(Point(p2.ctx.getX()+20, 240),Point(p2.ctx.getX()+30, 270))
p2.moveRightLeg(Point(p2.ctx.getX()+25, 350),Point(p2.ctx.getX()+50, 400))
p2.moveLeftLeg(Point(p2.ctx.getX()+5, 350),Point(p2.ctx.getX()-20, 400))
p2.moveAll(-25,0)

bm3 = boom2(415,265)
time.sleep(0.18)
bm3.undraw()

p2.moveRightHand(Point(p2.ctx.getX()-20, 250),Point(p2.ctx.getX()-30, 280))

p1.moveLeftHand(Point(p1.ctx.getX()-45, 240),Point(p1.ctx.getX()-15, 200))
p1.moveBody(-5)
p1.moveRightHand(Point(p1.ctx.getX()+40, 230),Point(p1.ctx.getX()+80, 220))
p1.moveLeftLeg(Point(p1.ctx.getX()+15, 350),Point(p1.ctx.getX()+20, 400))
p1.moveRightLeg(Point(p1.ctx.getX()-15, 350),Point(p1.ctx.getX()-30, 400))

p2.moveAll(0,-30)
p1.moveRightHand(Point(p1.ctx.getX()+40, 215),Point(p1.ctx.getX()+80, 195))

p2.moveBody(5)
p2.moveRightHand(Point(p2.ctx.getX()+12,p2.ctx.getY()+55), Point(p2.ctx.getX()+12,p2.ctx.getY()+110))
p2.moveLeftHand(Point(p2.ctx.getX()-6,p2.ctx.getY()+55), Point(p2.ctx.getX()-9,p2.ctx.getY()+110))
p2.moveRightLeg(Point(p2.ctx.getX()+6,p2.ctx.getY()+150), Point(p2.ctx.getX()+8,p2.ctx.getY()+200))
p2.moveLeftLeg(Point(p2.ctx.getX()-6,p2.ctx.getY()+150), Point(p2.ctx.getX()-8,p2.ctx.getY()+200))

time.sleep(0.18)

p1.moveLeftHand(Point(p1.ctx.getX()-35, 240),Point(p1.ctx.getX()-65, 250))
bm4 = boom3(342,250, 3)
time.sleep(0.3)
bm4.undraw()
bm5 = boom3(342,250, 7)
time.sleep(0.3)
bm5.undraw()
bm6 = boom3(342,250, 15)
time.sleep(0.3)
p1.moveLeftHand(Point(p1.ctx.getX()+40, 230),Point(p1.ctx.getX()+75, 235))
bm6.move(135, -15)
bm6.undraw()

p2.moveAll(50,10)
p2.moveHead(30,10)
p2.moveBody(65, 60)
p2.moveRightHand(Point(p2.ctx.getX()-35, 200),Point(p2.ctx.getX()-70, 180))
p2.moveLeftHand(Point(p2.ctx.getX()+40, 220),Point(p2.ctx.getX()-25, 240))
p2.moveRightLeg(Point(p2.ctx.getX()+30, 300),Point(p2.ctx.getX()-30, 350))
p2.moveLeftLeg(Point(p2.ctx.getX()+30, 300),Point(p2.ctx.getX()-40, 350))
for i in range (15):
    p2.moveAll(14,4)
    time.sleep(0.1)

p2.moveHead(130,160)
p2.moveBody(-80, 10, 12)
p2.moveRightHand(Point(p2.ctx.getX()-40, 388),Point(p2.ctx.getX()-55, 370),15,-12)
p2.moveLeftHand(Point(p2.ctx.getX()+30, 445),Point(p2.ctx.getX()+50, 450),20,-10)
p2.moveRightLeg(Point(p2.ctx.getX()-130, 400),Point(p2.ctx.getX()-160, 400))
p2.moveLeftLeg(Point(p2.ctx.getX()-130, 420),Point(p2.ctx.getX()-169, 430))

p1.moveLeftHand(Point(p1.ctx.getX()+10, 250),Point(p1.ctx.getX()+16, 300),20)
p1.moveRightHand(Point(p1.ctx.getX()-12, 250),Point(p1.ctx.getX()-8, 300),20)
p1.moveRightLeg(Point(p1.ctx.getX()-10, 350),Point(p1.ctx.getX()-20, 400))

time.sleep(0.6)

p2.moveHead(-50,-45)
p2.moveBody(-45,+60)
p2.moveRightHand(Point(p2.ctx.getX()-35, 388),Point(p2.ctx.getX()-55, 395),15,-12)
p2.moveLeftHand(Point(p2.ctx.getX()+20, 420),Point(p2.ctx.getX()+40, 440),20,-10)
p2.moveRightLeg(Point(p2.ctx.getX()-90, 400),Point(p2.ctx.getX()-125, 410))
p2.moveLeftLeg(Point(p2.ctx.getX()-90, 420),Point(p2.ctx.getX()-132, 430))

time.sleep(0.5)

screen.setBackground(color_rgb(100,100,100))
land.setOutline(color_rgb(100,100,100))
land.setFill(color_rgb(100,100,100))

p2.moveAll(-300,-100)

m1 = Circle(Point(400,350), 200)
m1.setFill('black')
m1.setOutline('black')
m2 = Polygon(Point(450,350),Point(440,700),Point(620,700))
m2.setFill('black')
m2.setOutline('black')
m2.setWidth(50)
m1.draw(screen)
m2.draw(screen)

re = Oval(Point(260,355),Point(320,425))
re.setFill('#DFDFDF')
re.setOutline('#DFDFDF')
re.draw(screen)

le = Oval(Point(360,355),Point(420,425))
le.setFill('#DFDFDF')
le.setOutline('#DFDFDF')
le.draw(screen)

rel = Line(Point(260,370),Point(330,390))
rel.setWidth(50)
rel.draw(screen)

lel = Line(Point(350,385),Point(420,365))
lel.setWidth(50)
lel.draw(screen)

time.sleep(1.6)
for i in range(5):
    m1.move(20,-12)
    m2.move(16,-10)
    re.move(20,-12)
    rel.move(20,-12)
    le.move(20,-12)
    lel.move(20,-12)
    time.sleep(0.1)
time.sleep(0.2)

rel.undraw()
lel.undraw()
re.setFill('#FFFFFF')
re.setOutline('#FFFFFF')
le.setFill('#FFFFFF')
le.setOutline('#FFFFFF')
time.sleep(1.2)

m1.undraw()
m2.undraw()
re.undraw()
le.undraw()
rel.undraw()
lel.undraw()

p2.moveAll(200,100)
p1.moveAll(-150,0)

p2.moveHead(-5,-180)
p2.moveBody(-10)
p2.moveRightHand(Point(p2.ctx.getX()+12,p2.ctx.getY()+55), Point(p2.ctx.getX()+12,p2.ctx.getY()+110))
p2.moveLeftHand(Point(p2.ctx.getX()-6,p2.ctx.getY()+55), Point(p2.ctx.getX()-9,p2.ctx.getY()+110))
p2.moveRightLeg(Point(p2.ctx.getX()-15, 350),Point(p2.ctx.getX()-15, 400))
p2.moveLeftLeg(Point(p2.ctx.getX()+5, 350),Point(p2.ctx.getX()+10, 370))

land.setFill(color_rgb(80,80,80))
land.setOutline(color_rgb(80,80,80))   

for i in range(13):
    time.sleep(0.2)    
    if i == 2:
        screen.setBackground(color_rgb(100,100,100))
        land.setFill(color_rgb(80,80,80))
        land.setOutline(color_rgb(80,80,80))    
    if i == 6:
        light1 = lightning1()   
        light2 = lightning2()
    if i == 8:
        light3 = lightning3()    
    if i == 10:
        for j in range(6):
            light1[j].undraw()
            light2[j].undraw()
        light3[0].undraw()
        light3[1].undraw()

time.sleep(1)   
p2.moveRightHand(Point(p2.ctx.getX()+20,p2.ctx.getY()+55), Point(p2.ctx.getX()+40,p2.ctx.getY()+150))
time.sleep(1)   

p2.moveHead(-40,40)
p2.moveLeftHand(Point(p2.ctx.getX()+40, 255),Point(p2.ctx.getX()+10, 290))
p2.moveBody(35)
p2.moveRightHand(Point(p2.ctx.getX()-20,p2.ctx.getY()+10), Point(p2.ctx.getX()+140,p2.ctx.getY()-20))
p2.moveLeftLeg(Point(p2.ctx.getX()+50, 350),Point(p2.ctx.getX()+75, 400))
p2.moveRightLeg(Point(p2.ctx.getX()-1, 350),Point(p2.ctx.getX()+45, 400))

for i in range(12):
    time.sleep(0.02) 
    p2.moveAll(-50,0)
    if i == 6:
        light1 = lightning1()   
        light2 = lightning2()
    if i == 8:
        light3 = lightning3()    
    if i == 10:
        for j in range(6):
            light1[j].undraw()
            light2[j].undraw()
        light3[0].undraw()
        light3[1].undraw()

time.sleep(1.2) 

for i in range(60):
    p1.moveHead(2,3)
    time.sleep(0.05) 
for i in range(1):
    p1.moveHead(0,-5)   
    time.sleep(0.1)  
    p1.moveHead(0,5)  
for i in range(7):
    p1.moveHead(2,0)   
    time.sleep(0.06)  
for i in range(5):
    time.sleep(0.02) 
    if i == 1:
        light1 = lightning1()   
        light2 = lightning2()
    if i == 3:
        light3 = lightning3()    
    if i == 4:
        for j in range(6):
            light1[j].undraw()
            light2[j].undraw()
        light3[0].undraw()
        light3[1].undraw()

for i in range(12):
    time.sleep(0.03) 
    if i == 6:
        light1 = lightning1()   
        light2 = lightning2()
    if i == 8:
        light3 = lightning3()    
    if i == 10:
        for j in range(6):
            light1[j].undraw()
            light2[j].undraw()
        light3[0].undraw()
        light3[1].undraw()

end = ['#4B4B4B', '#3B3B3B','#131313','#000000']
for i in range(4):
    screen.setBackground(end[i])
    land.setFill(end[i])
    land.setOutline(end[i])
    time.sleep(0.4) 
    if i == 1:
        p1.undrawAll()
        p2.undrawAll()
    
t = Text(Point(500,300), 'The End')    
t.setOutline('white')
t.setSize(24)
t.draw(screen)
time.sleep(1.2) 
t.setText('Thanks for watching')
time.sleep(1.2) 
t.setText('By Mohamed Elesawy')
screen.getMouse()