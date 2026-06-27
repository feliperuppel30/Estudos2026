import os


lista = []
while True:
    
    print('Digite uma opção')
    opcao = input('Digite [i]inserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('digite um valor: ')
        lista.append(valor)
    
    elif opcao == 'a':          
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except IndexError:
            print('este indice nao esta na lista')
        except ValueError:
            print('digite um numero inteiro')
        except Exception:
            print('erro desconhecido')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print ('nada para listar')

        for i, valor in enumerate(lista):
            print(i,valor)


    else:
        print('digite uma opcao válida')