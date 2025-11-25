from adaptador import LeitorDeArquivosAdapter

def cliente_processa_video(tipo, caminho):
    if tipo == 'mp4':
        print(f'Processando video no caminho "{caminho}"')
        return 'Cliente feliz'
    else:
        raise Exception
#o cliente nao aceita outro tipo de arquivo
#suponha que a api somente retorna mov ou avi

def chamar_api(endereco):
    print('Chamando api')
    print(f'API do endereco {endereco} retrornando sucesso')
    if endereco == 1:
        return ('mov', r'/caminho/video.mov')
    else:
        return ('avi', r'/caminho/video.avi')

