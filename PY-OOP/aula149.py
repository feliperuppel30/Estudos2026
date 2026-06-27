class MyContextManager:

    def __init__(self, caminho_arquivo, modo):
        print('init')
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('abrindo arquivo no enter')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('fechando arquivo no exit')
        self._arquivo.close()

instancia = MyContextManager('aula149.txt', 'w')

with instancia as arquivo:
    arquivo.write('linha 1 \n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')
    print('with', arquivo)