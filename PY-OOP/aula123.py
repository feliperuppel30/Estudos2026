class Animal:
    # nome = 'Leão'
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        # print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args,**kwargs)
        
zebra = Animal('zebra')

print(zebra.nome)
# print(zebra.comendo('capim'))
print(zebra.executar('capim limao'))