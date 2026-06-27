import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Felipe', 26)
p2 = Pessoa('Livia', 24)
p3 = Pessoa('Nemo', 0.9)

bd=[(p1.__dict__),
    (p2.__dict__),
    (p3.__dict__)]


def fazer_dump():
    print('fazendo dump')
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, indent=1)