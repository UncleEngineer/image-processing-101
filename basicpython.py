import turtle
import random
tao = turtle.Turtle() # T ตัวใหญ่
tao.shape('turtle')
# tao.forward(100)
# tao.left(90)
# tao.forward(100)
# tao.left(90)
# tao.forward(100)
# tao.left(90)
# tao.forward(100)
# tao.reset()
for i in range(4):
    tao.forward(100)
    tao.left(90)

tao.penup()
tao.goto(200,200)

tao.clear()
color = ['red', 'green', 'blue', 'orange']
for c in color:
    print(c)
    tao.color(c)
    tao.forward(100)
    tao.left(90)

tao.reset()

def drawCircle():
    for i in range(1,11):
        c = random.choice(color)
        tao.color(c)
        r = random.randint(50,100) #สุ่มค่ารัศมีวงกลม
        tao.circle(r) #วาดวงกลม
        tao.left(36)

drawCircle()

turtle.mainloop()