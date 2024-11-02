def draw_python():
    import turtle as t
    t.setup(800, 300, 200, 200)
    t.penup()
    t.fd(-150)
    t.pendown()
    t.seth(-40)
    t.pensize(40)
    t.pencolor("red")
    for i in range(4):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2 / 3)
    t.done()
draw_python()

