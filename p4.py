import turtle
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
