import turtle
from random import random

# Cria a tela e a tartaruga
t = turtle.Turtle()
# t.circle(3, extent=2, steps=25)# faz um circle
# t.shape('circle')
# t.shapesize(0.6)
t.screen.bgcolor('gray')
t.screen.title('Plague Inc')
t.color('green')
t.screen.delay(100)

# t.up() # stops to drawing

for c in range(25):
    steps = int(random() * 12)
    angle = int(random() * 90)
    t.right(angle)
    t.fd(steps)
    
print(t.position())
t.sety(-10)
print(t.position())

print(t.heading())
t.seth(-5)
print(t.heading())

t.tilt(30)
t.fd(50)
t.tilt(30)
t.fd(50)

t.home() #volta ao ponto inicial

# t.mainloop()
turtle.done()

# for steps in range(10):
#     for c in ('blue', 'green', 'red'):
#         t.color(c)
#         t.forward(steps)
#         t.right(20)

# t.fillcolor('blue')

# t.begin_fill()
# for c in range(10):
#     t.forward(200)
#     t.left(170)
# t.end_fill()

# with t.fill():
#     for i in range(4):
#         t.forward(100)
#         t.right(90)

# t.forward(200)

# t.forward(100) #avança 100m
# t.left(120)#qnd  acabar de avanç, gira 120graus
# t.forward(100)
# # t.up() # stops to drawing
# # t.down()  # turn on drawing
# t.left(120) 
# t.forward(100) #avança 100m
# t.forward(100) #avança 100m



        
        

# t.clearscreen() # FECHA A TELA TBM
