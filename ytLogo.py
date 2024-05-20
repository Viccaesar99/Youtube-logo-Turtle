import turtle

window = turtle.Screen()
window.title("Dibujo con Turtle")
window.bgcolor("black")



pen = turtle.Turtle()
pen.speed(1)
pen.pensize(2)
pen.color("red")
pen.ht()
for i in range(2):
    pen.forward(200)
    pen.left(90)
    pen.forward(100)
    pen.left(90)

pen.up()
pen.color("white")
pen.forward(60)
pen.left(90)
pen.forward(10)
pen.down()
pen.forward(80)
pen.right(120)
pen.forward(100)
pen.right(130)
pen.forward(93)

    

window.mainloop()
