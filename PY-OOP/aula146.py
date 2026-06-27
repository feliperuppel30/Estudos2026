class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    # def __str__(self):
    #     return f'(x={self.x}, y={self.y})'


    def __repr__(self): # para comunicar com desenvolvedores
        class_name = type(self).__name__
        return f'{class_name} (x={self.x}, y={self.y})'
    
p1 = Ponto(1,2)
print(p1)