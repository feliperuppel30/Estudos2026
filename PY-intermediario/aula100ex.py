# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 4', 'preco': 105.87},
    {'nome': 'Produto 5', 'preco': 69.90},
]
novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
    
    ]

#ordenar produto por nome decrescente 5-1

produtos_ordenados = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse= True
)

#ordenar produto por preço crescente

produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['preco'],
)


print(*produtos, sep= '\n')
print('')
print( *novos_produtos,sep= '\n')
print('')
print( *produtos_ordenados,sep= '\n')
print('')
print( *produtos_ordenados_preco,sep= '\n')