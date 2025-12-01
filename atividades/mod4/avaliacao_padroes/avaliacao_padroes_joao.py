from abc import ABC, abstractmethod
import functools

class Notificador(ABC):
    def postar_aviso(self, mensagem : str):
        mensagem_formatada = mensagem + "\n| Ass: Bolsa Futuro Digital"
        self.enviar(mensagem_formatada)

    @abstractmethod
    def enviar(self, mensagem_formatada: str):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensagem_formatada: str):
        print(f"Enviando E-MAIL: {mensagem_formatada}")

class NotificadorZap(Notificador):
    def enviar(self, mensagem_formatada: str):
        print(f"Enviando ZAP: {mensagem_formatada}")

def auditoria(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("--- Início do Processo ---")
        result = func(*args, **kwargs)
        print("--- Fim do Processo ---")
        return result
    return wrapper

@auditoria
def cliente_enviar(notificador, mensagem):
    notificador.postar_aviso(mensagem)

mail = NotificadorEmail()
zap = NotificadorZap()

cliente_enviar(mail, "Mensagem do EMAIL pro aluno")
print('')
cliente_enviar(zap, "Oi aluno do WHatsapp")