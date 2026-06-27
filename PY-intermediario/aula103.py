def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        resultado += ' qqer coisa'
        print(f'o seu resultado foi {resultado}')
        print('ok, decorado')
        return resultado
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')
    
@criar_funcao #aplica a funcao @ no lugar da funcao atual
def inverte_string(string):
    return string[::-1]

invertida = inverte_string('ruppel bueno')
print(invertida)