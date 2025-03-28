# SpiralMyName.py - печатать цветную спираль из имени
# пользователя

import turtle # установка графики turtie

from name import your_name

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

# запрос имени пользователя с помощью всплывающего окна
# texinput
your_name = turtle.textinput("ведите своё имя",
                             "как тебя зовут")

# нарисовать на экране спираль из имени, повторенного 100 раз
for x in range(100):
    t.pencolor(colors[x%4]) # по очереди выбрать все 4 цвета
    t.penup() # не рисовать обычные линии спирали
    t.forward(x*4) # просто переместить черепашку по экрану
    t.pendown() # написать имя пользователя, увеличивая
                                # каждый раз шрифт
    t.write(your_name, font = ("Arial", int( (x + 4) / 4),"bold"))
    t.left(92)
