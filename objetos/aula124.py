class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        
        if self.filmando:
            print(f'{self.nome} já está filmando..,')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        
        if self.filmando:
            print(f'{self.nome} parou de filmar..,')
            self.filmando = False
            return
        
        print(f'{self.nome} nao está filmando...')
        

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return       
        print(f'{self.nome} fotografou!')


camera_1 = Camera('Sony')
camera_2 = Camera('Canon')

print(camera_1.nome)
camera_1.filmar()
camera_2.filmar()

print(camera_1.filmando)
print(camera_2.filmando)

camera_1.filmar()
camera_1.fotografar()
camera_1.parar_filmar()
camera_1.fotografar()
camera_1.parar_filmar()
camera_1.fotografar()
