import turtle
t = turtle.Pen ()
turtle.bgcolor("black")
colors = ["red" ,"green" ,"yellow" ,"blue"]
for x in range(100) :
    t.pencolor ( colors [x%4] )
    t.forward (x)
    t.left (91)