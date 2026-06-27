#faç uma lisat que mostra a soma dos iteraveis de duas listas

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4]

lista_soma = [x+y for x,y in zip(l1,l2)]

print(lista_soma)

# for i in range(len(l2)):
#     print(i)
#     lista_soma.append(l1[i]+l2[i])

# print(lista_soma)
