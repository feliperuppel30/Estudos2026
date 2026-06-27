ANO_ATUAL = 2026

class Pessoa:

    atributo = 'valor'

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return ANO_ATUAL - self.idade
    
pessoa_1 = Pessoa('Felipe', 26)
pessoa_2 = Pessoa('Livia', 24)

print(pessoa_1.get_ano_nascimento())
print(pessoa_2.get_ano_nascimento())