somasum = sum((1, 2, 3))
print (somasum)

def soma(*args):
    total = 0
    for numero in args:
        total+= numero
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

numeros = 1,2,3,4,5,6
print(numeros)
print(*numeros) # * desempacota
print(sum((numeros)))
