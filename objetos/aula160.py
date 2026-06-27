from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])
as_espadas = Carta('A', 'Espadas')
print(as_espadas)