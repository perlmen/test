import turtle

t = turtle.Pen()
turtle.bgcolor("black")
# настройки спискаиз любых 8 действительных имен цветов
# pyyton
colors = ["red", "yellow", "blue", "green", "orange", "purple", "write", "gray"]
sides = int(turtle.numinput("сколько сторон","сколько сторон вы хотите (1-8)?",1,4,8))
for x in range (360) :
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)