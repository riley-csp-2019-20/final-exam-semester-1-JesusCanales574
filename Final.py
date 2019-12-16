import turtle as trtl

maker = trtl.Turtle()

maker.pensize(20)

maker.penup()
maker.pencolor("red")
maker.speed(0)
maker.ht()
maker.goto(-400,300)
maker.pendown()


gamer = trtl.Turtle()
gamer.shape("turtle")
gamer.pensize(2)




#make the etch a sketch
def drawgameBorad():
    maker.fd(800)
    maker.rt(90)
    maker.fd(500)
    maker.rt(90)
    maker.fd(800)
    maker.rt(90)
    maker.fd(500)

    maker.penup()
    maker.bk(400)
    maker.rt(90)
    maker.fd(10)
    maker.pendown()

    maker.pensize(40)
    maker.fd(780)
    maker.rt(90)
    maker.fd(95)
    maker.rt(90)
    maker.fd(780)
    maker.rt(90)
    maker.fd(90)
    maker.bk(50)
    maker.rt(90)
    maker.fd(780)
    maker.lt(90)
    maker.fd(35)
    maker.lt(90)
    maker.fd(780)
    maker.penup()
    maker.rt(180)
    maker.goto(-385,285)


    

    

drawgameBorad()
wn = trtl.Screen()

def bigger():
    gamer.pensize(+1)


def Up():
    gamer.setheading(90)
    gamer.forward(15)

def Down():
    gamer.setheading(270)
    gamer.forward(15)

def Left():
    gamer.setheading(180)
    gamer.forward(15)

def Right():
    gamer.setheading(0)
    gamer.forward(15)

wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onkeypress(Left,"Left")
wn.onkeypress(Right,"Right")
wn.onkeypress(bigger,"bigger")
wn.listen()


wn.mainloop()