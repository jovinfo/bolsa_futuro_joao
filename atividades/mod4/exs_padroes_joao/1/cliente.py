# 7. No seu código cliente, instancie um `ProcessadorCSV` e chame apenas o método `processar()`. Depois, faça o mesmo com `ProcessadorTXT`.
from processador import ProcessadorCSV, ProcessadorTXT

processador_csv = ProcessadorCSV()
resultado_csv = processador_csv.processar("dados.csv")
print(resultado_csv)
print('\n')
processador_txt = ProcessadorTXT()
resultado_txt = processador_txt.processar("dados.txt")
print(resultado_txt)

"""Conseguiu fazer todo o exercício? Reflita sobre os dois seguintes pontos:
1 - Você fez tudo no mesmo arquivo? Se sim, como você poderia dividir em mais de um arquivo para que sua aplicação fique mais organizada?
2 - Pesquise sobre Template Method, este foi o padrão implementado aqui?"""
#Dividi entre 2 arquivos, um para o processador e outro para o cliente.
#Sim, o padrão Template Method foi implementado aqui no qual temos um esqueleto de processador e cada tipo de arquivo tem sua implementação específica.