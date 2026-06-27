while True:
    numero_1 = input('digite o primeiro numero')
    numero_2 = input('digite o segundo numero')
    operador = input('digite um dos operadors: /*-+:')
    numero_valido = None
    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print('algum numero nao é valido')
        continue

    operador_valido = '/*-+'

    if operador not in operador_valido:
        print('operador invalido')
    # else:
    #     resultado = (numero_1,(operador), numero_2)
    # print(resultado)
    if operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '+':
        print(num1_float + num2_float)

    sair = input('digite "s" para sair ').lower().startswith('s')

    if sair is True:
        break