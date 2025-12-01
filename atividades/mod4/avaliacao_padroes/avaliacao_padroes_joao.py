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
cliente_enviar(zap, "Oi aluno do WHatsapp")
    
"""Para resolver este problema, você deve implementar o código seguindo os passos abaixo:
1. Padrão Template Method
• Crie uma classe abstrata chamada Notificador.
• Implemente nela o método concreto postar_aviso(mensagem). Ele deve:
1. Concatenar a string " | Ass: Bolsa Futuro Digital" ao final da mensagem recebida.
2. Chamar o método enviar(mensagem_formatada) passando a nova mensagem.
• Defina o método enviar como abstrato (@abstractmethod).
• Crie duas classes filhas concretas:
1. NotificadorEmail: O método enviar deve imprimir: Enviando E-MAIL: [texto].
2. NotificadorZap: O método enviar deve imprimir: Enviando ZAP: [texto].
2. Padrão Decorator
• Crie um decorator de função chamado auditoria.
• Este decorator deve envolver a execução da função decorada.
• Antes de executar a função, imprima: "--- Início do Processo ---".
• Após executar a função, imprima: "--- Fim do Processo ---".
3. Código Cliente
• Crie uma função chamada cliente_enviar(notificador, mensagem).
• Decore esta função com @auditoria.
• Dentro dela, chame o método postar_aviso do objeto notificador recebido.
• Instancie as classes concretas e faça um teste de envio para cada uma"""