contador = 0    

while contador <= 100:
    contador += 1
    if contador >=10 and contador <= 20:
        # print('contador entre 10 e 20')
        continue
    print(contador)
    if contador >= 50:
        break

print('fim do loop')


