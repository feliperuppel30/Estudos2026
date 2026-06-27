
import random
import sys

for _ in range(20):
    nove_digitos = ''
    for numeros in range(9):
        nove_digitos += str(random.randint(0,9))
    print (nove_digitos)



    contador_regressivo_1 = 10
    contador_regressivo_2 = 11

    resultado_digito1 = 0
    resultado_digito2 = 0

    for digito in nove_digitos:
        resultado_digito1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito1*10 % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0
    print (digito_1)

    dez_digitos = nove_digitos + str(digito_1)


    for digito in dez_digitos:
        resultado_digito2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito2*10%11)
    digito_2 = digito_2 if digito_2 <= 9 else 0
    print(digito_2)

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado)




    

