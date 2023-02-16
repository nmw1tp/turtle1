import turtle
import random
     
doe = turtle.Turtle()
doe.speed(20)

def starfill(n,dlina):
    doe.left(random.randint(10,340))
    doe.begin_fill()
    if n %2 != 0:
        for i in range(n):
            doe.forward(dlina)
            angle = n//2 * 360 /n
            doe.left(angle)
    doe.end_fill()

doe.color("yellow")
doe.hideturtle()
window = turtle.Screen()
window.bgcolor("black")
window.setup(700,500)
for i in range(50):
    x = random.randint(-320,320)    
    y = random.randint(-220,220)
    doe.up()
    doe.setposition(x,y)
    doe.down()
    size = random.randint(10,20)
    ize = random.choice([4,5,6,7,8,9,10])
    starfill(ize,size)

def mv(x,y):
    doe.up()
    doe.setposition(x,y)
    doe.down()
    size = random.randint(10,20)
    ize = random.choice([4,5,6,7,8,9,10])
    starfill(ize,size)

window.onclick(mv)
window.listen()
window.mainloop()
