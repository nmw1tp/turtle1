import turtle

x = int(input("1-cub,2-triangle,3-circle,4-xz,choose : "))

if x == 4:
    pen = turtle.Turtle()
    pen.speed(10)
    pen.up()
    pen.setposition(-30,-30)
    pen.down()
    def rg(n,dl):
        sum = (n-2)*180
        if sum%n==0:
            angle = sum//n
            for i in range(n):
                pen.forward(100)
                pen.left(180-angle)
    for i in range(3,11):
        rg(i,50)
        
elif x == 2:
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

elif x == 1:
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
        sq(dlina)
        joe.right(10)
        dlina=dlina+5

elif x == 3:
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

