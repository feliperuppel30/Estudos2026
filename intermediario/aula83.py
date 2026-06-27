pessoa = {
    'nome':'Livia',
    'sobrenome': 'Dutra'
    }
dados_pessoa = {
    'idade':23,
    'altura':1.53
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

def mostro_args_nomeados(*args, **kwargs):
    print(f'náo nomeados= {args} cabou')
    for chave, valor in kwargs.items():
        print(f'nomeadas= {chave}: {valor}')
# mostro_args_nomeados(1, 2, 'Livia', sobrenome = 'Dutra',numero = 2)
# mostro_args_nomeados(**pessoa_completa)
