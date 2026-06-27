string = 'ABCDE'   
lista = ['Felipe', 'Ruppel', 1, 2, 3, 'Livia', 'Dutra']
tupla = 'Python', 'é', 'Legal'


print(*tupla, sep='-')
print(*lista, sep='-')
for nome in lista:
    print(nome, end=' ')
print(lista)