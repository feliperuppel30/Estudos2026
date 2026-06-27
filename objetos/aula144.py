from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Email enviando:', self.mensagem)

class NotificacaoWpp(Notificacao):
    def enviar(self):
        print('WPP enviando:', self.mensagem)  
        return True      

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('notificacao enviada')
    print('notificacao NAO enviada')


notificacao_email = NotificacaoEmail('testando email')
notificar(notificacao_email)

notificacao_wpp = NotificacaoWpp('testando Wpp')
notificar(notificacao_wpp)
    
