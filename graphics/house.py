import turtle
import random
from turtle import *
from random import randint

# turtle.bgcolor('light blue')
t1 = turtle.Turtle()
t2 = turtle.Turtle()

### background area ###
#Page setup
setup(800, 500)
speed(0)
bgcolor("midnightblue")

# Function to draw one star
def star():
    color("yellow")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()
hideturtle()

# Draw multiple stars at random area
for i in range(40):
    x = randint(-550, 550)
    y = randint(-50, 400)
    star()
    penup()
    goto(x, y)
    pendown()
    
# Draw Moon 
penup()
goto(-500, -270)
pendown()
color("yellow")
begin_fill()
circle(30)
end_fill()
hideturtle()

t1.speed(19)

def randomLine(x, y, a, b):
        for c in range(x):
            t1.seth(random.randint(a, b))
            t1.fd(y)
            
###################### sea ###############
t1.color('black', 'aqua') # water color is aqua
t1.pu()
t1.goto(230, -350)
t1.seth(90)
t1.begin_fill()
t1.fd(100)
t1.goto(230, -250)
t1.pd()
t1.seth(80)
randomLine(35, 25, 175, 185)
t1.seth(270)
t1.fd(100)
t1.end_fill()

def boat(x, y):
    t1.width(2)
    t1.color('black', 'white')
    t1.pu()
    t1.goto(x, y)
    t1.pd()
    t1.begin_fill()
    t1.fd(15)
    t1.seth(0)
    t1.circle(400, extent=15)
    t1.seth(45)
    t1.circle(60, extent=25)
    t1.pu()
    t1.goto(x, y)
    t1.seth(0)
    t1.pd()
    t1.circle(400, extent=15)
    
    t1.lt(10)
    t1.fd(16)
    t1.pu()
    t1.goto(x, y)
    t1.seth(160)
    t1.pd()
    t1.fd(15)
    
    t1.seth(270)
    t1.fd(15)
    t1.seth(280)
    t1.circle(8, extent=115)
    t1.end_fill()
    
    t1.pu()
    t1.goto(x, y)
    t1.begin_fill()
    t1.seth(160)
    t1.fd(15)
    t1.goto(-314.10, -244.87)
    t1.pd()
    t1.seth(0)
    t1.circle(400, extent=5)
    t1.seth(270)
    t1.pu()
    t1.fd(5)
    t1.end_fill()
    
    t1.begin_fill()
    t1.pd()
    
    t1.seth(50)
    t1.fd(8)
    t1.rt(10)
    t1.fd(5)
    t1.seth(15)
    t1.fd(20)
    t1.seth(355)
    t1.fd(10)
    print(t1.position())
    t1.seth(350)
    t1.fd(20)
    t1.seth(12)
    t1.fd(33)
    t1.end_fill()
    
    t1.width(1)
    t1.pu()
    t1.goto(-235, -235)
    t1.pd()
    t1.color('black', 'red')
    t1.begin_fill()
    t1.seth(90)
    t1.fd(15)
    t1.seth(180)
    t1.fd(5)
    t1.seth(270)
    t1.fd(15)
    t1.end_fill()
    
    t1.color('black', 'white')
    t1.pu()
    t1.bk(15)
    t1.seth(180)
    t1.pd()
    t1.begin_fill()
    randomLine(9, 7, 180, 200)
    t1.seth(45)
    t1.circle(250, extent=40)
    t1.seth(268)
    t1.fd(145)
    t1.pu()
    t1.fd(13)
    t1.seth(45)
    t1.pd()
    t1.fd(5)
    t1.seth(89.2)
    t1.fd(145)
    t1.seth(270)
    t1.circle(300, extent=30)
    t1.seth(160)
    t1.fd(45)
    t1.end_fill()
    
    t1.width(2)
    t1.color('black', 'black')
    t1.pu()
    t1.goto(-265, -240)
    t1.seth(270)
    t1.pd()
    t1.fd(7)
    t1.pu()
    t1.goto(-240, -235)
    t1.begin_fill()
    t1.seth(275)
    t1.pd()
    t1.fd(10)
    t1.pu()
    t1.seth(190)
    t1.fd(18)
    t1.seth(90)
    t1.fd(10)
    t1.end_fill()
    
    
    # sys.exit()
    
    
    t1.begin_fill()
    t1.end_fill()
    t1.hideturtle()
    





boat(-300, -250)
            
def base():    
    t1.pu()
    t1.goto(230.51, -240.88)
    t1.color('black', 'brown')
    t1.pd()
    t1.begin_fill()
    randomLine(2, 5, 190, 200)
    randomLine(5, 5, 220, 260)
    randomLine(5, 5, 200, 210)
    randomLine(5, 5, 230, 240)
    randomLine(5, 5, 200, 220)
    randomLine(5, 5, 230, 240)
    t1.seth(0)
    t1.fd(200)
    t1.end_fill()
    
    t1.pu()
    t1.color('black', 'black')
    t1.goto(220, -260)
    t1.pd()
    t1.begin_fill()
    randomLine(3, 6, 240, 250)
    randomLine(3, 6, 190, 200)
    randomLine(3, 6, 210, 225)
    randomLine(4, 10, 230, 245)
    t1.end_fill()
    
    t1.pu()
    t1.goto(230, -280)
    t1.pd()
    t1.begin_fill()
    randomLine(5, 6, 250, 260)
    randomLine(3, 6, 190, 210)
    randomLine(3, 6, 200, 225)
    randomLine(3, 6, 240, 260)
    t1.end_fill()
    
    t1.pu()
    t1.goto(240, -295)
    t1.pd()
    t1.begin_fill()
    randomLine(3, 6, 250, 270)
    randomLine(3, 6, 190, 230)
    randomLine(4, 6, 230, 240)
    randomLine(3, 6, 250, 265)
    t1.end_fill()
    
    
    
    
    
    t1.color('black', 'orange') 
    t1.up()
    t1.goto(640, -325)
    t1.pd()
    t1.begin_fill()
    t1.seth(90)
    t1.fd(100)
    t1.seth(160)
    t1.fd(20)
    randomLine(20, 5, 150, 170)
    t1.seth(185)
    t1.pu()
    t1.fd(250)
    t1.pd()
    randomLine(10, 6, 200, 220)
    t1.seth(230)
    t1.fd(5)
    t1.seth(260)
    t1.fd(10)
    randomLine(10, 5, 280, 290)
    randomLine(5, 5, 320, 330)
    randomLine(15, 5, 340, 350)
    t1.end_fill()

t1.speed(19)

base()



def cloud(x, y):
    t1.color('white', "white")
    t1.pu()
    t1.goto(x, y)
    t1.pd()
    t1.begin_fill()
    t1.circle(20, 270)
    t1.rt(100)
    t1.circle(15, 150)
    t1.rt(100)
    t1.circle(15, 180)
    t1.rt(100)
    t1.circle(15, 200)
    t1.rt(70)
    t1.circle(15, 60)
    t1.rt(70)
    t1.circle(15, 100)
    t1.end_fill()


    
cloud(-100, 200)
cloud(-150, 250)
cloud(-500, 250)
cloud(450, 230)
cloud(490, 230)
cloud(200, 250)
cloud(300, 40)
cloud(550, 40)
cloud(-300, 100)



t1.color('black')
t2.color('black')

def curve(x, y, z):
        for x in range(x):
            t1.fd(y)
            t2.fd(y)
            t1.lt(z)
            t2.rt(z)
            
def tower(x, y):
    
    #circle#
    t1.speed(9)
    t2.speed(9)
    t1.pu()
    t2.pu()
    t1.goto(x, y)
    t2.goto(x,y)
    t2.pd()
    t1.pd()
    t1.width(2)
    t2.width(2)
    t1.circle(3, extent=360, steps=10)
    
    #triangle#
    t1.seth(210)
    t2.seth(330)
    t1.fd(35)
    t2.fd(35)
    t1.seth(5)
    t2.seth(175)
    t2.fd(30)
    t1.fd(30)
    
    #3d#
    t1.pu()
    t2.pu()
    t1.goto(x-30, y-17)
    t2.goto(x+30, y-17)
    t1.pd()
    t2.pd()
    t1.seth(345)
    t1.fd(10)
    t2.seth(195)
    t2.fd(10)
    
    #window#   
    t1.goto(x-20, y-17)
    t2.goto(x+20, y-17)
    t1.seth(270)
    t2.seth(270)
    t1.fd(20)
    t2.fd(20)
    t1.pu()
    t2.pu()
    t1.goto(x-10, y-17)
    t2.goto(x+10, y-17)
    t1.pd()
    t2.pd()
    t1.fd(18.5)
    t2.fd(18.5)
    
    t1.pu()
    t2.pu()
    t1.goto(x, y-36)
    t2.goto(x, y-36)
    t1.pd()
    t2.pd()
    t1.seth(180)
    t2.seth(0)
    
    for x in range(3):
        t1.fd(10)
        t2.fd(10)
        t1.lt(5)
        t2.rt(5)
    t1.seth(270)
    t2.seth(270)
    t1.fd(20)
    t2.fd(20)
    t1.seth(0)
    t2.seth(180)
    
    #fence#
    t1.pu()
    t2.pu()
    t1.goto(x+348, y-56)
    t2.goto(x+348, y-56)
    t1.pd()
    t2.pd()
    t1.seth(180)
    t2.seth(0)
    curve(4, 11, 5)
    t1.pu()
    t2.pu()
    t1.goto(350, y-42)
    t2.goto(350, y-42)
    t1.pd()
    t2.pd()
    t1.seth(180)
    t2.seth(0)
    curve(4, 11, 5)
    print(t1.position())
    
    t1.seth(270)
    t2.seth(270)
    t1.fd(18)
    t2.fd(18)
    
    t1.pu()
    t2.pu()
    t1.goto(350, y-60)
    t2.goto(350, y-60)
    t1.pd()
    t2.pd()
    t1.seth(180)
    t2.seth(0)
    curve(4, 11, 5)
    t1.pu()
    t2.pu()
    t1.goto(307, y-49)
    t2.goto(392, y-49)
    t1.pd()
    t2.pd()
    t1.seth(345)
    t2.seth(195)
    t1.fd(12)
    t2.fd(12)
    
    #bottom fence#
    t1.pu()
    t2.pu()
    t1.goto(350, y-70)
    t2.goto(350, y-70)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(3, 10, 8)
    t1.seth(135)
    t1.fd(12)
    t2.seth(45)
    t2.fd(12)
    
    t1.pu()
    t2.pu()
    t1.goto(350, y-85)
    t2.goto(350, y-85)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(3, 10.1, 8)
   
    t1.pu()
    t2.pu()
    t1.goto(350, y-180)
    t2.goto(350, y-180)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(4, 10, 7.5)
    
    t1.pu()
    t2.pu()
    t1.goto(350, y-195)
    t2.goto(350, y-195)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(4, 10, 7.5)
    
    t1.pu()
    t2.pu()
    t1.goto(350, y-310)
    t2.goto(350, y-310)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(5, 10.3, 5)

    t1.pu()
    t2.pu()
    t1.goto(350, y-340)
    t2.goto(350, y-340)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(5, 10.5, 5)
    
    t1.pu()
    t2.pu()
    t1.goto(322, y-475)
    t2.goto(322, y-475)
    t1.seth(180)
    t2.seth(0)
    t1.pd()
    t2.pd()
    curve(5,7.3, 2)
    
    t1.pu()
    t1.goto(x+319, y-75)
    t2.pu()
    t2.goto(x+378, y-75)
    t1.pd()
    t2.pd()
    t1.seth(265)
    t2.seth(275)
    t1.fd(420)
    t2.fd(340)
     
     
    # t1.hideturtle()
    # t2.hideturtle()
    
    
    
    


########### house #############

# def verticalCurve():

def curve1(length):
    a = 2
    t1.seth(245)    
    for x in range (5):
        t1.fd(length)
        t1.rt(a)
        a += 2
def curve2(length):
    a = 2
    t2.seth(295)    
    for x in range (5):
        t2.fd(length)
        t2.lt(a)
        a += 2
        
def curve3(length):
    a = 1
    t1.seth(195)    
    for x in range (5):
        t1.fd(length)
        t1.rt(a)
        a += 2
        
        
    
        
def house(x, y):
    t1.speed(9)
    t2.speed(9)
    t1.pu()
    t2.pu()
    t1.goto(x, y)
    t2.goto(x, y)
    t1.pd()
    t2.pd()
    curve1(14)
    curve2(14)
    
    t1.pu()
    t2.pu()
    t1.goto(x, y)
    t2.goto(x, y)
    t1.pd()
    t1.seth(90)
    t2.seth(90)
    t1.fd(8)
    t2.fd(8)
    t2.pd()
    curve1(15)
    print(t1.position())
    curve2(15)
    t1.lt(95)
    t1.fd(6)
    t2.rt(95)
    t2.fd(6)
    
    t1.pu()
    t2.pu()
    t1.goto(x, y+8)
    t1.seth(210)
    t1.pd()
    t1.fd(25)
    t1.pu()
    t1.fd(15)
    t1.pd()
    curve3(12)
    curve1(9)
    print(t1.position())
    t1.seth(270)
    t1.fd(4)
    t1.seth(4)
    t1.fd(80)
    t1.pu()
    t1.goto(x-117.89, y-58.79)
    t1.pd()
    t1.seth(4)
    t1.fd(78)
    t1.pu()
    t1.seth(268)
    t1.fd(4)
    t1.pd()
    t1.fd(55)
    t1.pu()
    t1.goto(x-110, y-63)
    t1.pd()
    t1.seth(268)
    t1.fd(52)
    t2.seth(270)
    t2.pu()
    t2.goto(x+35, y-55)
    t2.pd()
    t2.fd(9)
    
    
def smallHouse(x, y):
    t1.speed(9)
    t2.speed(9)
    t1.pu()
    t2.pu()
    t1.goto(x, y)
    t2.goto(x, y)
    t1.pd()
    t2.pd()
    curve1(7)
    curve2(7)
    
    t1.pu()
    t2.pu()
    t1.goto(x, y)
    t2.goto(x, y)
    t1.pd()
    t1.seth(90)
    t2.seth(90)
    t1.fd(5)
    t2.fd(5)
    t2.pd()
    curve1(7.5)
    print(t1.position())
    curve2(7.5)
    t1.lt(95)
    t1.fd(3)
    t2.rt(95)
    t2.fd(3)
    
    t1.pu()
    t2.pu()
    t1.goto(x, y+6)
    t1.seth(210)
    t1.pd()
    t1.fd(5)
    t1.pd()
    curve3(8)
    curve1(6.5)
    print(t1.position())
    t1.seth(270)
    t1.fd(2)
    t1.seth(4.1)
    t1.fd(43)
    t1.pu()
    t1.goto(x-61.18, y-29.77)
    t1.pd()
    t1.seth(4)
    t1.fd(43)
    t1.pu()
    t1.seth(268)
    t1.fd(3)
    t1.pd()
    t1.fd(25)
    t1.pu()
    t1.goto(x-55, y-33)
    t1.pd()
    t1.seth(268)
    t1.fd(18)
    t2.seth(270)
    t2.pu()
    t2.goto(x+15, y-27)
    print(t2.position())
    t2.pd()
    t2.fd(27)
    
    
########## window ########## 
def window1(x, y, l, b, w):
    t1.pu()
    t1.width(1)    
    t1.goto(x, y)
    t1.pd()
    t1.seth(180)
    t1.fd(b)
    t1.seth(270)
    t1.fd(l)
    t1.seth(0)
    t1.fd(b)
    t1.seth(90)
    t1.fd(l)
    t1.pu()
    t1.goto(x-2, y-2)
    t1.color('black','aqua')
    t1.begin_fill()
    t1.pd()
    t1.seth(180)
    t1.fd(b-4)
    t1.seth(270)
    t1.fd(l-4)
    t1.seth(0)
    t1.fd(b-4)
    t1.seth(90)
    t1.fd(l-4)
    t1.end_fill()
    t1.bk((l-4)/2)
    t1.seth(180)
    t1.width(w)
    t1.fd(b-4)
    t1.pu()
    t1.bk((b-4)/2)
    t1.seth(90)
    t1.fd((l-4)/2)
    t1.pd()
    t1.bk(l-4)
    
    
def door(x, y):
    t1.color('black', 'aqua')
    t1.pu()
    t1.goto(x, y)
    t1.pd()
    t1.seth(90)   
    t1.begin_fill()
    t1.fd(17)
    t1.circle(5, extent=180, steps=10)
    t1.fd(16)
    t1.end_fill()
    t1.pu()
    t1.goto(x-2, y)
    t1.pd()
    t1.seth(90)   
    t1.begin_fill()
    t1.fd(17)
    t1.circle(5, extent=180, steps=10)
    t1.fd(16)
    
def tree(x, y, color):
    # turtle.tracer(0, 0)
    t1.pu()
    t1.goto(x, y)
    t1.pd()
    t1.color(color, color)
    t1.begin_fill()
    t1.seth(70)
    t1.fd(10)
    t1.seth(180)
    t1.fd(15)
    t1.seth(30)
    t1.fd(20)
    t1.seth(170)
    t1.fd(10)
    t1.seth(30)
    t1.fd(15)
    t1.lt(20)
    t1.fd(10)
    t1.seth(185)
    t1.fd(13)
    t1.seth(30)
    t1.fd(15)
    t1.lt(50)
    t1.fd(5)
    t1.seth(185)
    t1.fd(8)
    t1.seth(40)
    t1.fd(15)
    t1.seth(80)
    t1.fd(10)
    
    t1.seth(280)
    t1.fd(10)
    t1.seth(300)
    t1.fd(10)
    t1.seth(160)
    t1.fd(5)
    t1.seth(290)
    t1.fd(8)
    t1.seth(320)
    t1.fd(10)
    t1.seth(170)
    t1.fd(10)
    t1.seth(290)
    t1.fd(5)
    t1.lt(20)
    t1.fd(20)
    t1.seth(170)
    t1.fd(15)
    t1.seth(320)
    t1.fd(25)
    t1.seth(165)
    t1.fd(15)
    t1.seth(285)
    t1.fd(10)
    t1.end_fill()
    
    t1.hideturtle()
    
t1.speed(19)  
tree(530, -200, 'green')
tree(550, -220, 'green')
tree(580, -230, 'green')

def bush(x, y, color):
    t1.speed(19)
    t1.pu()
    t1.goto(x, y)
    t1.pd()
    t1.color(color, color)
    t1.begin_fill()
    t1.circle(5, extent=90)
    t1.seth(90)
    t1.circle(5, extent=120)
    t1.seth(90)
    t1.circle(5, extent=180)
    t1.seth(90)
    t1.circle(5, extent=220)
    t1.seth(180)
    t1.circle(6, extent=200)
    t1.seth(270)
    t1.circle(5, extent=230)
    t1.seth(270)
    t1.circle(6, extent=200)
    t1.end_fill()
    
bush(380, -225, 'green')
bush(365, -225, 'green')
bush(415, -240, 'green')
bush(445, -235, 'green')
bush(475, -245, 'green')
bush(505, -250, 'green')




bush(340, -215, 'green')
bush(320, -200, 'green')
bush(295, -215, 'green')




        



def fence(x, y, z):
    a = 7
    b = 7
    t1.pu()
    t1.goto(x, y)
    for c in range(z):
        t1.pu()
        t1.goto(x+a, y-b)
        t1.pd()
        t1.seth(90)
        t1.fd(15)
        t1.pu()
        t1.bk(5)
        t1.seth(160)
        t1.pd()
        t1.fd(16)
        t1.pu()
        t1.bk(16)
        t1.seth(270)
        t1.fd(4)
        t1.seth(160)
        t1.pd()
        t1.fd(16)
        
        a += 15
        b += 5
    
t1.speed(9)
fence(540, -235, 5)
fence (605, -265, 2)



t1.hideturtle()
t2.hideturtle()

    
    

t1.color('black')
t1.color('black')

tower(350, 275)
house(470,-120)   
smallHouse(513, -187)

window1(340, -130 , 32, 24, 2)
window1(370, 40, 23, 18, 1.5)
window1(350, 180, 15, 10, 1)
window1(482.5, -165, 14, 24, 1)
window1(385, -196, 15, 11, 1)
window1(415, -195, 15, 11, 1)
window1(482, -222, 12, 16, 1)
door(517, -240)



turtle.done()
