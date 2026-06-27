salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'Joao', 'Livia', (0, 1, 2, 3, 4)]
    ]

for sala in salas:
    for aluno in sala:
        print(aluno)
print(*salas, sep='\n')