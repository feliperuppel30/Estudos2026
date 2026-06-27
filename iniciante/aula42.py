frase = 'o Python é uma linguagem de programação'\
        'ultiparadigma o Python foi criado pelo Holandes'
i= 0
qtd_apareceu_mais_x = 0
letra_apareceu_mais_x = ''

while i < len(frase):
    letraatual = frase[i]
   
    if letraatual == ' ':
        i+=1
        continue


    qtd_apareceu_mais_vezes_atual = frase.count(letraatual)

    if qtd_apareceu_mais_x < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_x = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_x = letraatual

    i+=1

print(letra_apareceu_mais_x, qtd_apareceu_mais_x)
   

    