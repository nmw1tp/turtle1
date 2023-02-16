import turtle



joe = turtle.Turtle()
joe.color('red')
colors = ['red','brown','green','blue']
joe.speed(30)

def sq(a):
    for i in range(4):
        joe.forward(a)
        joe.left(135)
        joe.forward(a)
        joe.left(110)
        joe.forward(70)

dlina = 90
for i in range(100):
    joe.color(colors[i%4])
    sq(dlina)
    joe.right(10)
    dlina=dlina+10

