frase = '  uma frase, duas frases  '
lista_frases_cruas = frase.split(',')
lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
    
print(lista_frases)
print(lista_frases_cruas)

frases_unidas = '-'.join(lista_frases)
print (frases_unidas)