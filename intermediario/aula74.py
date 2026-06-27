def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

dar_bomdia = criar_saudacao('bom dia')
dar_boanoite = criar_saudacao('boa noite')

for nome in ['Felipe','Livia', 'Nemo']:
    print(dar_bomdia(nome))
    print(dar_boanoite(nome)) 