import os 

caminho = os.path.join('desktop','curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)
print( extensao_arquivo)
print(os.path.exists(caminho))