from logistica import LogisticaTerreste, LogisticaMaritima

# Testando o código
logistica_terrestre = LogisticaTerreste()
logistica_terrestre.planejar_entrega()

print("\n\n")

logistica_maritima = LogisticaMaritima()
logistica_maritima.planejar_entrega()

# 1 - Você construiu todo o código no mesmo arquivo? Se sim, como você poderia repartir em vários arquivos para que sua aplicação fique organizada? Consulte nossos exemplos da aula para refletir sobre o assunto.
# Dividi entre o arquivo principal (controlador.py) e os arquivos transporte.py e logistica.py organizando as classes.