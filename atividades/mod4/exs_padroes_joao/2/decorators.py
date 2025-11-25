"""2 - Decorators!

Você tem um sistema que por padrão envia apenas e-mails! Você precisa adicionar opcionalmente a capacidade de enviar também por SMS ou Whatsapp!

1 - Crie uma função enviar_email(email) com uma lógica simulada de envio de e-mail.

2 - Crie então dois decorators sms e whatsapp. Cada um deve implementar a sua respectiva lógica simulada de envio!

3 - Teste a implementação dos dois decorators com a função enviar_email!

Conseguiu fazer todo o exercício? Reflita sobre os seguinte pontos:
1 - Supondo que é o usuário que escolhe como será contactado, vale a pena refatorar a função enviar_email, apenas para enviar() e então implementar um 3 decorator email?
2 - Suponha que os métodos de envio continuem crescendo (slack, teams, telegram, etc) faz sentido continuar criando decorators? Caso sua resposta seja não: qual outro padrão você implementaria?"""

import functools

def enviar_email(email):
    print(f"Coletando os dados do cliente {email}")
    print(f"Conectando ao servidor de envio")
    print(f"E-mail enviado para {email}!")
    return 'Sucesso no envio do e-mail!'

# print(enviar_email("email@mail.com"))

def sms(func):
    @functools.wraps(func)
    def wrapper(telefone):
        resultado = func(telefone)
        print(f"Enviando SMS para {telefone}")
        print(f"SMS enviado para {telefone}!")
        return resultado + ' Sucesso no envio do SMS!'
    return wrapper

def whats(func):
    @functools.wraps(func)
    def wrapper(telefone):
        resultado = func(telefone)
        print("Conectando ao servidor WhatsApp")
        print(f"WhatsApp enviado para {telefone}!")
        return resultado + ' Sucesso no envio do WhatsApp!'
    return wrapper

@sms
def enviar_email_sms(email):
    print(f"Coletando os dados do cliente {email}")
    print(f"Conectando ao servidor de envio")
    print(f"E-mail enviado para {email}!")
    return 'Sucesso no envio do e-mail!'

print(enviar_email_sms("21999998888"))

@whats
def enviar_email_whats(email):
    print(f"Coletando os dados do cliente {email}")
    print(f"Conectando ao servidor de envio")
    print(f"E-mail enviado para {email}!")
    return 'Sucesso no envio do e-mail!'

print(enviar_email_whats("2122223333"))

"""1 - Supondo que é o usuário que escolhe como será contactado, vale a pena refatorar a função enviar_email, apenas para enviar() e então implementar um 3 decorator email?
2 - Suponha que os métodos de envio continuem crescendo (slack, teams, telegram, etc) faz sentido continuar criando decorators? Caso sua resposta seja não: qual outro padrão você implementaria?"""
#Com certeza seria melhor a refatoração para uma função enviar() e implementar um decorator email, assim o código ficaria mais limpo e organizado.

#Usaria o padrao Template Method criando uma classe base de envio e subclasses para cada método de envio específico, podendo assim ter mais clareza na logica e seria fácil a implementação de novas formas.