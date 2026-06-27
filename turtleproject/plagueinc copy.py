import turtle as t
import random
from itertools import combinations
import time
import matplotlib.pyplot as plt
import threading



WIDTH, HEIGHT = 800, 600
MAX_TIME_INFECTION = 400
IMUNE_TIME = 300
LIFETIME = 2200
FERTILITY_PROB = 0.0001
INFECTION_PROB = 0.1
LIFERISK = 0.001


class Cell:
    SPEED = 3 
    COLLISION_DIST = 30

    def __init__(self, x, y, status='healthy'):
        self.status = status
        self.age = 0
        self.time_infection = 0
        self.time_immune = 0
        self.time_procriation = 0

        self.turtle = t.Turtle()
        self.turtle.shape('circle')
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(random.randint(0, 360))
        self._apply_color()

    def _apply_color(self):
        colors = {'healthy': 'green', 'infected': 'red', 'immune': 'blue'}
        self.turtle.color(colors[self.status])

    def set_status(self, new_status):
        self.status = new_status
        self._apply_color()

    def move(self, largura, altura, parede, velocidade):
        self.turtle.fd(self.SPEED)
        self.turtle.left(random.randint(-10, 10))
        x, y = self.turtle.xcor(), self.turtle.ycor()
        #bordas janela 
        if x >= largura // 2:  self.turtle.goto(-largura //2, y)
        elif x <= -largura // 2: self.turtle.goto(largura //2, y)
        if y >= altura // 2: self.turtle.goto(x, -altura //2)
        elif y <= -altura // 2: self.turtle.goto(x, altura //2)

        if parede.collides_with(x,y):
            self.turtle.setheading(self.turtle.heading() + 180)
    

    def age_tick(self, lifetime=LIFETIME, liferisk=LIFERISK):
        self.age += 1
        self.time_procriation += 1
        if self.age > lifetime and random.random() < liferisk:
            return False  # sinaliza morte
        return True

    def infection_tick(self, max_time=MAX_TIME_INFECTION, liferisk=LIFERISK):
        """Devolve False se a célula morreu."""
        if self.status == 'infected':
            self.time_infection += 1
            if self.time_infection >= max_time:
                if random.random() < liferisk:
                    return False  # morreu
                self.set_status('immune')
                self.time_immune = IMUNE_TIME
                self.time_infection = 0
        elif self.status == 'immune':
            self.time_immune -= 1
            if self.time_immune <= 0:
                self.set_status('healthy')
        return True

    def hide(self):
        self.turtle.hideturtle()


def check_collisions(population):
    """Verifica infecções e reproduções entre pares de células."""
    new_cells = []
    for c1, c2 in combinations(population, 2):
        if c1.turtle.distance(c2.turtle) > Cell.COLLISION_DIST:
            continue

        # infecção
        if c1.status == 'infected' and c2.status == 'healthy':
            if random.random() < 0.02:
                c2.set_status('infected')
        elif c2.status == 'infected' and c1.status == 'healthy':
            if random.random() < 0.02:
                c1.set_status('infected')

        # reprodução
        if (c1.status == 'healthy' and c2.status == 'healthy'
                and c1.time_procriation >= 100 and c2.time_procriation >= 100):
            if random.random() < 0.005:
                baby = Cell(c1.turtle.xcor(), c1.turtle.ycor(), status='immune')
                baby.time_immune = IMUNE_TIME
                new_cells.append(baby)
                c1.time_procriation = 0
                c2.time_procriation = 0

    population.extend(new_cells)


def atualizar_celulas(population, largura, altura, parede, velocidade):
    to_remove = []
    for cell in population:
            alive = cell.age_tick()
            if alive:
                alive = cell.infection_tick()
            if not alive: 
                cell.hide()
                to_remove.append(cell)
            else:
                cell.move(largura, altura, parede, velocidade)

    for dead in to_remove:
            population.remove(dead)


def contar_populacao(population):
    saudaveis  = [c for c in population if c.status == 'healthy']
    infectadas = [c for c in population if c.status == 'infected']
    imunes     = [c for c in population if c.status == 'immune']
    return saudaveis, infectadas, imunes


def calcula_tempo(tempo_inicio):
    agora = time.time()
    segundos_passados = float(agora - tempo_inicio)
    minutos = int(segundos_passados // 60)
    segundos = int(segundos_passados % 60)
    return minutos, segundos, segundos_passados


def atualizar_hud(escritor, minutos, segundos, saudaveis, infectadas, imunes):
    escritor.clear()
    escritor.goto(-390, 180)
    escritor.write(
        f'Tempo: {minutos:02d}:{segundos:02d}\n'
        f'Saudáveis: {len(saudaveis)}\n'
        f'Infectadas: {len(infectadas)}\n'
        f'Imunes: {len(imunes)}\n',
        font=('Arial', 14,'normal')
    )


def verificar_vitoria(saudaveis, infectadas, estavel_desde, escritor, screen):
    if len(saudaveis) >= 5 and len(infectadas) >=5: 
        if estavel_desde is None:
            estavel_desde = time.time()

        tempo_estavel = time.time() - estavel_desde

        if tempo_estavel >= 60:
            escritor.goto(0,0)
            escritor.write(
                f'vitória! população estável por 1 minuto!',
                align='center', font=('Arial', 24, 'bold')
            )
            screen.update()
            time.sleep(5)
            return estavel_desde, True
    else: 
        estavel_desde = None
    return estavel_desde, False


historico = {
    'saudaveis':[],
    'infectadas':[],
    'imunes':[]
}


def registrar_historico(historico, saudaveis, infectadas, imunes, segundos_passados, ultimo_registro):
    if segundos_passados > ultimo_registro:
        ultimo_registro = segundos_passados
        historico['saudaveis'].append(len(saudaveis))
        historico['infectadas'].append(len(infectadas))
        historico['imunes'].append(len(imunes))
    return ultimo_registro


def loop_grafico():
    plt.ion()
    while True:
        plt.clf()
        plt.plot(historico['saudaveis'], label = 'saudaveis', color='green')
        plt.plot(historico['infectadas'], label = 'infectadas', color='red')
        plt.plot(historico['imunes'], label = 'imunes', color='blue')
        plt.pause(1)
def spawn_seguro(parede):
    while True:
        x = random.randint(-WIDTH//2, WIDTH//2)
        y = random.randint(-HEIGHT//2, HEIGHT//2)
        if not parede.collides_with(x,y):
            return Cell(x,y)
class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def collides_with(self, cell_x, cell_y, margem = 15):
        dentro_x = (self.x - self.width //2 - margem) <= cell_x <= (self.x + self.width /2 + margem)
        dentro_y = (self.y - self.height //2 - margem) <= cell_y <= (self.y + self.height /2 + margem)
        return dentro_x and dentro_y
    
    def desenhar(self, screen):
        parede = t.Turtle()
        parede.hideturtle()
        parede.penup()
        parede.goto(self.x - self.width//2, self.y - self.height//2)  # canto inferior esquerdo
        parede.color('gray')
        parede.begin_fill()        # começa a preencher
        parede.pendown()
        for _ in range(4):         # desenha 4 lados
            parede.fd(self.width)
            parede.left(90)
        parede.end_fill()          # termina o preenchimento
        parede.penup()


def main():
    screen = t.Screen()
    screen.tracer(0)

    parede = Wall(0,0,100,100)
    parede.desenhar(screen)

    population = [spawn_seguro(parede)
                  for _ in range(200)]
    population[0].set_status('infected')
    population[2].set_status('infected')

    escritor = t.Turtle()
    escritor.hideturtle()  
    escritor.penup()

    tempo_inicio = time.time()
    estavel_desde = None
    ultimo_registro = 0 

    pausado = False
    velocidade = 1

    def pausar():
        nonlocal pausado
        pausado = not pausado

    def  set_velocidade(v):
        nonlocal velocidade
        velocidade = v
        
    screen.listen()
    screen.onkey(pausar, 'space')
    screen.onkey(lambda: set_velocidade(1), '1')
    screen.onkey(lambda: set_velocidade(3), '3')
    screen.onkey(lambda: set_velocidade(5), '5')
    screen.onkey(lambda: set_velocidade(10), '0')

    while True:
        if pausado:
            screen.update()
            continue


        largura = screen.window_width()
        altura = screen.window_height()

        for _ in range(velocidade):    # ← repete N vezes por frame
            atualizar_celulas(population, largura, altura, parede, 1)
            
        check_collisions(population)

        saudaveis, infectadas, imunes = contar_populacao(population)

        minutos, segundos, segundos_passados = calcula_tempo(tempo_inicio)

        ultimo_registro = registrar_historico(historico, saudaveis, infectadas, imunes, segundos_passados, ultimo_registro)

        atualizar_hud(escritor, minutos, segundos, saudaveis, infectadas, imunes)

        estavel_desde, vitoria = verificar_vitoria(saudaveis, infectadas, estavel_desde, escritor, screen)
        if vitoria:
            break

        screen.update()
        
thread = threading.Thread(target=loop_grafico, daemon=True)

thread.start()
main()
