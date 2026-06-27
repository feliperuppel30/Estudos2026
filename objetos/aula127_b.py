import json

from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1=Pessoa(**pessoas[0])
    p2=Pessoa(**pessoas[1])
    p3=Pessoa(**pessoas[2])

    print(p1.__dict__)
    print(p2.__dict__)
    print(p3.__dict__)
                      
