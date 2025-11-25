class LeitorDeMov:
    """Adapter 1: Converte mov para mp4."""
    def converter(self, caminho):
        print('ADAPTER MOV:Convertendo o Mov para MP4')
        print('Procesando espere...')
        print('Conversao concluida')
        return f'novo_{caminho}'

class LeitorDeAvi:
    """Adapter 2: Converte AVI para MP4"""
    def converter(self, caminho):
        print('ADAPTER AVI: Carregando avi configs')
        print('Convertendo...')
        print('Conversao concluida')
        return f'novo_{caminho}'
