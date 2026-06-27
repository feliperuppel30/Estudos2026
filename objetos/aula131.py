class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None

    # def get_cor(self):
    #     return self.cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.cor = 'Verde'
caneta2 = Caneta('preta')
caneta2.cor_tampa = 'transparente'


print(caneta.cor)
print(caneta2.cor, caneta2.cor_tampa)
# print(caneta.get_cor())