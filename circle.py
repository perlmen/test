        import turtle
t = turtle.Pen()
number_of_circies = int (turtle.numinput("количество окружностей", "сколько окружностей в вашей розетке?",6))
for x in range(number_of_circies):
    t.circle(100)
    t.left(360/number_of_circies)
