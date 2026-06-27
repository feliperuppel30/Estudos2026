class CallMe:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self):
        print (f'ligando para {self.phone}')
    
call1 = CallMe('12312312')
call1()