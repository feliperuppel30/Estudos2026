from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: 0

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':
    pessoa1 = Pessoa('Felipe', 'Ruppel')
    pessoa2 = Pessoa('Livia', 'Dutra')

    print(pessoa1.nome_completo()) 