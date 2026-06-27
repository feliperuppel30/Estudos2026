#raise - lançando exceções

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('nao divido por 0')
    return True

def divide(n,d):

    if not isinstance(n, (float, int)):
        raise TypeError('Digite um numero')

    nao_aceito_zero(d)
    return n/d

print(divide(2,2))