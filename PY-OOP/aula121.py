# métodos em instâncias de classes 

# class Carro:
#     def __init__(self, nome):
#         self.nome = nome

#     def acelerar(self):
#         print(f'{self.nome} esta acelerando' )

# fusca = Carro( 'fusca')
# print(fusca.nome)
# fusca.acelerar()

# celta = Carro('celta ')
# print(celta.nome)
# celta.acelerar()


class Carro():
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('fusca')
# celta = Carro('celta')
Carro.acelerar(fusca)

# print(fusca.nome)
# fusca.acelerar()
# print(celta.nome)
# celta.acelerar()
print(Carro())