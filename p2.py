import turtle



joe = turtle.Turtle()
joe.color('red')
colors = ['red','brown','green','blue']
joe.speed(30)

def sq(a):
    for i in range(4):
        joe.forward(++a)
        joe.left(90)

dlina = 40
for i in range(100):
    joe.color(colors[i%4])
    joe.circle(dlina)
    joe.right(10)
    dlina=dlina+5

