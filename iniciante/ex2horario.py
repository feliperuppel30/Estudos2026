# horario = input('Que horas são agora?')
# horarioint = int(horario)

# if horarioint >= 0 and horarioint < 12:
#     print('Bom dia')
# elif horarioint >=12 and horarioint < 18:
#     print('Boa tarde')
# elif horarioint >=18 and horarioint < 24:
#     print('Boa noite')

try:
    horario = input('Que horas são agora?')
    horarioint = int(horario)

    if horarioint >= 0 and horarioint < 12:
        print('Bom dia')
    elif horarioint >= 12 and horarioint < 18:
        print('Boa tarde')
    elif horarioint >= 18 and horarioint < 24:
        print('Boa noite')
    else:
        print('Por favor, digite um horário válido.')
except:
    print('Por favor, digite um número inteiro válido.')