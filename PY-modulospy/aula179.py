from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'
print(CAMINHO_CSV)
with open(CAMINHO_CSV, 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())