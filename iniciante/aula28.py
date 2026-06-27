nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[-1::-1]}')
    if ' ' in nome:
        print(f'seu nome tem espaços')
    else: 
        print(f'seu nome não tem espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do teu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')
