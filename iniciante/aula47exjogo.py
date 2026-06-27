
import os

password = 'love'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra:')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    print('bora')
    if letra_digitada in password:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in password:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
            
        else: 
            palavra_formada += '*'
    
    print(palavra_formada)

    if letras_acertadas == password:
        os.system('cls')
        print('voce descubriu a password!')
        print('a password era love')
        print(f'Voce tentou {tentativas} vezes')
        letras_acertadas = ''
        tentativas = 0
        
        

        
           
    