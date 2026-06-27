












perguntas = [
    {
        'Pergunta': 'quanto é 2+2',
        'Opções': ['1','2','4','6'],
        'resposta': '4',
    },
      {
        'Pergunta': 'quanto é 2*3',
        'Opções': ['1','2','4','6'],
        'resposta': '6',
    },
     {
        'Pergunta': 'quanto é 8/4',
        'Opções': ['1','2','4','6'],
        'resposta': '2',
    },
]
contador = 0
for p in perguntas:
    print (p['Pergunta'])

    opcoes = p['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)


    escolha = input('Digite sua resposta:')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <qtd_opcoes:
            if opcoes[escolha_int] == p['resposta']:
                print('voce acertou')
                contador+=1
            else: print('voce errou')



    

print(f'voce acertou {contador} de 3')