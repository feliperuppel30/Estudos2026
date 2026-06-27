'''var1 = None
var2 = True

if var1 and var2:
    print('as duas variaveis são verdadeiras')
elif var1 or var2:
    print('uma das variaveis é verdadeira')
else:
    print('as duas variaveis são falsas')
'''
login = (input('Digite login:'))
senha = (input('Digite senha:'))
if login and senha:
    print('voce logou')
elif login and not senha:
    print('voce esqueceu da senha')
elif not login and senha:
    print('voce esqueceu do login')
else:
    print('voce esqueceu do login e da senha')
    

if 0.0 or 1:
    print(0.112 )