class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    @classmethod
    def metodo_classes(cls):
        print('hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('anonimo', idade)
    

pessoa_1 = Pessoa('Felipe',26)
pessoa_2 = Pessoa.criar_com_50_anos('felipe')
pessoa_3 = Pessoa.criar_anonimo(26)

print(pessoa_1.__dict__)
print(vars(pessoa_1))

pessoa_1.metodo_classes()
print(pessoa_2.__dict__)
print(pessoa_3.__dict__)

