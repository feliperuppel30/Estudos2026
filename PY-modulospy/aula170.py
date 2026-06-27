##D:\projeto2026\exemploimgs

import os

caminho = 'D:\\projeto2026\\exemploimgs'
print(caminho)
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(caminho_completo_pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)