
class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

pessoa_1 = Pessoa('Felipe',26)

print(pessoa_1.__dict__)
print(vars(pessoa_1))