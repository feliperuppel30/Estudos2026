from pathlib import Path

# caminho_projeto = Path()
# print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

arquivo = Path.home() / 'Desktop' / 'aula177.txt'
arquivo.touch()

print(arquivo)

arquivo.write_text('Hello World!')

print(arquivo.read_text())

arquivo.unlink()