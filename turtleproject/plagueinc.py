#project virus spread using turtle  

import turtle as t
import random
import time


# Usar 1 timer só.
WIDTH = 1600
HEIGHT = 800
MAX_TIME_INFECTION = 400
LIFETIME = 1000
FERTILITY_PROB = 0.0001
INFECTION_PROB = 0.1
LIFERISK = 0.1

SPAWN_WIDTH = WIDTH // 2
SPAWN_HEIGHT = HEIGHT // 2

gamewindow = t.Screen()
gamewindow.setup(width=WIDTH, height=HEIGHT)
gamewindow.tracer(0)


population =[]

def spawn_person(posicao, status='healthy', cor='green'):
    cell = t.Turtle()
    cell.shape('circle')
    cell.penup()
    cell.goto(posicao)
    
    cell.setheading(random.randint(0,360))


    # Atributos que você definiu na Imagem 3
    cell.status = status
    cell.color(cor)
    cell.time_infection = 0
    cell.max_time_infection = 400
    cell.time_immune = 200 if status == 'immune' else 0
    cell.age = 0
    cell.time_procriation = 0
    cell.lifetime = 1000
    cell.fertility_prob = 0.1
    cell.infection_prob = 0.1
    cell.liferisk = 0.1
    population.append(cell)
    return cell



for i in range(100): #spawn de 100 pessoas em pontos aleatorios
    new_person = spawn_person((random.randint(-800, 800), random.randint(-400, 400)))

    if i == 0:
        new_person.status = 'infected'
        new_person.color('red')
    

    

game_is_on = True

while game_is_on:       #movimento aleatorio  

    for p in population[:]: # morte natural por idade apenas
        p.age += 1
        if p.age > p.lifetime: 
            if random.random() < p.liferisk:
                p.hideturtle()
                population.remove(p)

    for p1 in population:        #bouncekick
        p1.time_procriation += 1

        if p1.xcor() >= 800:     
            p1.setheading(180)
        if p1.xcor() <= -800:
            p1.setheading(0)
        if p1.ycor() >= 400:
            p1.setheading(270)
        if p1.ycor() <= -400:
            p1.setheading(90)

        p1.fd(3) # velocity
        p1.left(random.randint(-10,10))
        
        if p1.time_infection >= p1.max_time_infection:       #tempo limite de infecção morte ou imunidade
            if random.random() < p1.liferisk:
                p1.hideturtle()
                population.remove(p1)
                continue
            else:  #sobreviveu
                p1.status = 'immune'
                p1.color('blue')
                p1.time_immune = 100
                p1.time_infection = 0
                p1.age = 0
                
            
        elif p1.status == 'immune': # volta a ser healthy depois do tempo immune
            p1.time_immune -= 1
            if p1.time_immune <= 0:   
                p1.status = 'healthy'
                p1.color('green')
                # p1.age = 0

            

        elif p1.status == 'infected':    # checa se ta infectado e infecta com a %
            p1.time_infection += 1
            for p2 in population:
                if p2.status == 'healthy':
                    distance_p1_p2 = p1.distance(p2)
                    if distance_p1_p2 <= 30:
                        if random.random() < p2.infection_prob:
                            p2.status = 'infected'
                            p2.color('red')

        elif p1.status == 'healthy' and p1.time_procriation >= 200:
            for p2 in population:
                if p2.status == 'healthy' and p2.time_procriation >= 200:
                    distance_p1_p2 = p1.distance(p2)
                    if distance_p1_p2 <= 30:
                        if random.random() < p2.fertility_prob:
                            baby = spawn_person((p1.xcor(), p1.ycor()))
                            baby.status = 'immune'
                            p1.time_procriation = 0
                            p2.time_procriation = 0
                    

    time.sleep(0.00001)
    gamewindow.update()



    

# gamewindow.exitonclick()
t.done()



