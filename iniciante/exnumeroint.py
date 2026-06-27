numero1 = input('digite um numero:')

if numero1.isdigit():
    numero1int = int(numero1)
    if numero1int % 2 == 0:
        print(f'o numero {numero1int} é par')
    else:
        print (f'o numero {numero1int} é impar')
else:
    print('Por favor, digite um número inteiro válido.')
