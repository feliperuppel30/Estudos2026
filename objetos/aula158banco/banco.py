import contas
import pessoas


class Banco:
    def __init__(
          self, 
          agencias:list[int]| None=None,
          clientes:list[pessoas.Pessoa]| None=None,
          contas:list[contas.Conta]| None=None):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta) -> bool:
        if conta.agencia in self.agencias:
            print('checa_agencia', True)
            return True
        return False


    def _checa_cliente(self, cliente)-> bool:
        if cliente in self.clientes:
            print('checa_cliente', True)
            return True
        return False
    
    def _checa_conta(self,conta)-> bool:
        if conta in self.contas:
            print('checa_conta', True)
            return True
        return False
    
    def _checa_conta_certa(self, cliente, conta):
        if conta is cliente.conta:
            print('checa conta certa', True)
            return True
        print('checa conta certa', False)
        return False
    

    def autenticar(self, cliente: pessoas.Pessoa, conta:contas.Conta)-> bool:
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_conta_certa(cliente, conta)
            
    

    
if __name__ == '__main__':
    import contas

    cliente1 = pessoas.Cliente('Felipe', 26)
    cc1 = contas.ContaCorrente(111, 222, 100, 200)
    cliente1.conta = cc1

    cliente2 = pessoas.Cliente('Livia', 24)
    cp1 = contas.ContaPoupanca(123, 456, 100)
    cliente2.conta = cp1

    banco = Banco()
    banco.clientes.extend([cliente1, cliente2])
    banco.contas.extend([cc1,cp1])
    banco.agencias.extend([111, 123])

    if banco.autenticar(cliente1, cc1):
        cc1.depositar(100)
        cc1.sacar(20)
        cc1.sacar(300)


    