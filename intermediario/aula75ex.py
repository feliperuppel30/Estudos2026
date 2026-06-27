





def multiplicador(multiplicador):
    
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)
print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))