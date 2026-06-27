def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
        par = total % 2 == 0
        if par: print(f'{total} é par')
        else: print(f'{total} é ímpar')
    return total
    
 
multiplicacao(21,3,3)
