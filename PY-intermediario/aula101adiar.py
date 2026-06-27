# adiando execuçao de funções

def soma(x,y):
    return x+y

def multiplica(x,y):
    return x*y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna
    

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_2 = criar_funcao(multiplica, 2)
print(soma_com_cinco( 52))
print(multiplica_por_2( 37))