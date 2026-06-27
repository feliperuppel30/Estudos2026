

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError('o nome deve ser uma string')
        self._nome = nome


    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if not isinstance(idade, int):
            raise TypeError('a idade deve ser um inteiro')
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta = None

if __name__ == '__main__':
    import contas
    cliente1 = Cliente('Felipe', 26)
    cliente1.conta = contas.ContaCorrente(123, 456, 100, 200)
    cliente1.conta.depositar(100)
    cliente1.conta.sacar(300)
    print(cliente1)
    print(cliente1.nome)