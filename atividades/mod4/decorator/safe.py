"""
Nossa lógica precisa funcionar da seguinte maneira:

1 - Se a função original funcionar, retornamos o resultado dela!
2 - Se ela falhar (der erro) nosso decorator vai capturar o erro, imprimir um aviso no console (com print mesmo) e retornar "None", impedindo que a aplicação trave!

Para alcançar esse objetivo siga as instruções:

1 - Crie um arquivo chamado "safe.py"
2 - Importe functools.
3 - Implemente um decorator chamado safe_run. (Lembre-se dos *args e **kwargs no wrapper!)
4 - Dentro do wrapper utilize uma estrutura semelhante a essa:
    try:
      return funcao_original(*args, **kwargs)
    execept Exception as e:
        #Tratamento de erro aqui!

5 - Crie uma função propositalmente quebrada para testar!
    obs: Para isso basta utilizar: raise Exception("Qualquer mensagem de erro")

6 - Chame a função para executar o teste! Se o resultado da função for None o que acontece?
"""

import functools
def safe_run(funcao_original):
    """Decorador para capturar erros, avisar pelo console e retornar 'None' em caso de falha."""

    @functools.wraps(funcao_original)
    def wrapper(*args, **kwargs):
        """Aqui vem a docsting do wrapper, está vai ser substituída!"""
        
        try:
            return funcao_original(*args, **kwargs)
        except Exception as e:
            print(f"Erro esperado '{e}' capturado pelo wrapper")
            return None
        
    return wrapper

@safe_run
def funcao_quebrada():
    print('Tudo funcionando até que....')
    raise Exception("Sou uma mensagem de um erro grave!")
    print('nao vou imprimir')

funcao_quebrada()