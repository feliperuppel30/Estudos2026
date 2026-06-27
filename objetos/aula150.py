from contextlib import contextmanager

@contextmanager
def MyContextManager(caminho_arquivo, modo):
    try:    
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    # except Exception as e:
    #     print('ocorreu erro', e)
    finally:    
        print('fechando o arquivo')
        arquivo.close()

with MyContextManager('aula150.txt', 'w') as arquivo:
    arquivo.write('linha 1 \n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')
    print('with', arquivo)