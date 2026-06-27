import abc



class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        self.agencia = agencia
        self.saldo = saldo
        self.conta = conta

    

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self,valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'depósito de {valor:.2f} efetuado')
        return self.saldo
    
    def detalhes(self, msg: str='') -> None:
        print(f'{msg} \n o seu saldo é {self.saldo:.2f} ')
    
class ContaPoupanca(Conta):
    def sacar(self,valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo = valor_pos_saque
            self.detalhes(f'saque de {valor:.2f} efetuado')
            return self.saldo
        print(f'saldo insuficiente para sacar {valor:.2f}')
        self.detalhes(f'seu saldo é {self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
                                                          

        if valor_pos_saque >= limite_maximo:
            self.saldo = valor_pos_saque
            self.detalhes(f'saque de {valor:.2f} efetuado')
            return self.saldo
        print(f'saldo insuficiente para sacar {valor:.2f}')
        print(f'limite:{self.limite}')
        self.detalhes()






if __name__ == '__main__':
    # contapoupanca1 = ContaPoupanca(111, 222, 0)
    # contapoupanca1.sacar(2)
    # contapoupanca1.depositar(1200)
    # contapoupanca1.sacar(2)
    # contapoupanca1.sacar(1100)
    # print('##')
    contacorrente1 = ContaCorrente(111, 222, 0, 200)
    contacorrente1.sacar(2)
    contacorrente1.depositar(1200)
    contacorrente1.sacar(2)
    contacorrente1.sacar(1100)
    contacorrente1.sacar(200)
    contacorrente1.sacar(200)
    
