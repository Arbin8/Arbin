import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('aquamarine')
t = turtle.Turtle()
t.hideturtle()
t3 = turtle.Turtle()
t3.hideturtle()
t3.penup()
t.speed(1)
t.penup()
t.goto(0,150)
t.pendown()
t.write("Things I like",font=("Arial",24,"bold"),align="center")

enter = input("Press Enter To Start")
t.clear()
screen.bgcolor('light blue')

t.write("Favorite foods",font=("Arial",24,"bold"),align="center")

t.penup()
t.goto(0,100)
t.pendown()
t.write("--- Mac and cheese",font=("Arial",12,"bold"),align="center")
turtle.addshape("mac and cheese.gif")
t3.shape("mac and cheese.gif")
t3.goto(-155,50)
a = t3.stamp()

t.penup()
t.goto(0,75)
t.pendown()
t.write("--- Noodles cups",font=("Arial",12,"bold"),align="center")
turtle.addshape("noodle cup.gif")
t3.shape("noodle cup.gif")
t3.goto(-150,-150)
b = t3.stamp()

t.penup()
t.goto(0,50)
t.pendown()
t.write("--- Sweet chicken",font=("Arial",12,"bold"),align="center")
turtle.addshape("sweet chicken.gif")
t3.shape("sweet chicken.gif")
t3.goto(80,-75)
c = t3.stamp()
t3.goto(80,-75)

enter= input("Press Enter To Start")
t.clear()
t3.clear()
screen.bgcolor('red')

t.penup()
t.goto(0,150)
t.write("Hobbies",font=("Arial",24,"bold"),align="center")
t.pendown()

t.penup()
t.goto(0,100)
t.pendown()
t.write("--- Soccer",font=("Arial",12,"bold"),align="center")
turtle.addshape("soccer ball.gif")
t3.shape("soccer ball.gif")
t3.goto(-200,50)
d = t3.stamp()

t.penup()
t.goto(0,75)
t.pendown()
t.write("--- playing video games",font=("Arial",12,"bold"),align="center")
turtle.addshape("games.gif")
t3.shape("games.gif")
t3.goto(-150,-150)
e = t3.stamp()

t.penup()
t.goto(0,50)
t.pendown()
t.write("--- reading online novels",font=("Arial",12,"bold"),align="center")
turtle.addshape("reading.gif")
t3.shape("reading.gif")
t3.goto(150,-75)
f = t3.stamp()

t.penup()
t.goto(0,25)
t.pendown()
t.write("--- that's all",font=("Arial",12,"bold"),align="center")
turtle.addshape("error.gif")
t3.shape("error.gif")
t3.goto(150,-250)
g = t3.stamp()
t3.goto(150,-225)

enter= input("Press Enter To Start")
t.clear()
t3.clear()
screen.bgcolor('gold')

t.penup()
t.goto(0,150)
t.write("Favorite movie",font=("Arial",24,"bold"),align="center")
t.pendown()

t.penup()
t.goto(0,100)
t.pendown()
t.write("--- I don't watch movies",font=("Arial",12,"bold"),align="center")


enter= input("Press Enter To Start")
t.clear()
t3.clear()
screen.bgcolor('orange')

t.penup()
t.goto(0,150)
t.pendown()
t.write("--- Favorite sport",font=("Arial",12,"bold"),align="center")

t.penup()
t.goto(0,100)
t.pendown()
t.write("--- soccer",font=("Arial",12,"bold"),align="center")
turtle.addshape("soccer ball.gif")
t3.shape("soccer ball.gif")
h = t3.stamp()

t.penup()
t.goto(50,100)
t.pendown()
turtle.addshape("soccer ball2.gif")
t3.shape("soccer ball2.gif")
i = t3.stamp()
turtle.done()