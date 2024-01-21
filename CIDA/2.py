# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plot

print("ATIVIDADE 2")

# ENTRADA DE DADOS #
dados_basquete = [1,2,4,4,7,3,3,2,4,5,2,4,3,5,3,2,4,3,6,5,5,6,4,6,5]
dados_futebol = [1,7,7,6,1,2,6,1,7,2,1,3,2,7,5,6,1,7,4,1,5,7,6,3,2]


# PROCESSAMENTO DOS DADOS #

' BASQUETE '
media_b = np.mean(dados_basquete)
mediana_b = np.median(dados_basquete)
desviopadrao_b = np.std(dados_basquete)

'FUTEBOL'
media_f = np.mean(dados_futebol)
mediana_f = np.median(dados_futebol)
desviopadrao_f = np.std(dados_futebol)


# APRESENTAÇÃO DOS DADOS #

' BASQUETE '
print("DADOS DO BASQUETE: ")
print("MEDIA DO BASQUETE", media_b)
print("MEDIANA DO BASQUETE", mediana_b)
print("DESVIO-PADRÃO DO BASQUETE", desviopadrao_b)
print("===============================================")

' FUTEBOL '
print("DADOS DO FUTEBOL: ")
print("MEDIA DO FUTEBOL", media_f)
print("MEDIANA DO FUTEBOL", mediana_f)
print("DESVIO-PADRÃO DO FUTEBOL", desviopadrao_f)


# CRIÇÃO DO BOXPLOT #

' BASQUETE '
boxplot_b = plot.boxplot(dados_basquete, positions=[1], labels=["BASQUETE"])

' FUTEBOL '
boxplot_f = plot.boxplot(dados_futebol, positions=[2], labels=["FUTEBOL"])

# APRESENTAÇÃO DO BOXPLOT#
plot.title("COLETAS DE LESÕES")
plot.xlabel("ALUNOS")
plot.ylabel("LESÕES")
plot.show()