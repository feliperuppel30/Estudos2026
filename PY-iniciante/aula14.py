n = 'felipe'
s = 'Ruppel'
i = 26
string = 'nome:{no1} sobrenome:{so1} idade:{ida1:.2f}'
format = string.format(no1=n, so1=s, ida1=i)
print(format)

#fstring

fstring = f'nome:{n} sobrenome:{s} idade:{i:.2f}'
print (fstring)