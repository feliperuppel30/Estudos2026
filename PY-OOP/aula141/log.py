#Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent  / 'log.txt'


class Log:
    def log(self, msg):
        raise NotImplementedError(
            'Implemente o método log'
        )
    
    def log_error(self, msg):
        return self.log(f'Error: {msg}')
    
    def log_sucsess(self, msg):
        return self.log(f'Sucsess: {msg}')

class LogFileMixin(Log):
    def log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('salvando log')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write('salavando log')
            arquivo.write('\n')
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def log(self, msg):
        print (f'{msg}({self.__class__.__name__})')

if __name__ == '__main__':    
    logprint = LogPrintMixin()
    logprint.log_error('qqer coisa')
    logprint.log_sucsess('qqer coisa')
    print(LOG_FILE)
    logfile = LogFileMixin()
    logfile.log_error('qqer coisa')
    logfile.log_sucsess('qqer coisa')
    

