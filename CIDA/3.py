# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
# ATIVIDADE 3 #
'=============================================================================================='
print("==========================================================================================================================================================================================================================================================================================")
print("ATIVIDADE 3")

# ENTRADA DE DADOS #
dados_alunas = [154,109,137,115,152,140,154,178,101,103,126,126,137,165,165,129,200,148]
dados_alunos = [108,140,114,91,180,115,126,92,169,146,109,132,75,88,113,151,70,115,187,104]


# PROCESSAMENTO DOS DADOS #
mediana_alunas = np.median(dados_alunas)
mediana_alunos = np.median(dados_alunos)
media_alunas = np.mean (dados_alunas)
media_alunos = np.mean (dados_alunos)

print("A")

# APRESENTAÇÃO DOS DADOS #
' ALUNAS '
print("DADOS DAS ALUNAS: ")
print("MEDIA DAS ALUNAS:", media_alunas)
print("MEDIANA DAS ALUNAS:", mediana_alunas)
print("===============================================")

' ALUNOS '
print("DADOS DOS ALUNOS: ")
print("MEDIA DOS ALUNOS:", media_alunos)
print("MEDIANA DOS ALUNOS:", mediana_alunos)

print("===============================================")

# CRIÇÃO DO BOXPLOT #
' BASQUETE '
boxplot_alunas = plot.boxplot(dados_alunas, positions=[1], labels=["ALUNAS"])

' FUTEBOL '
boxplot_alunos = plot.boxplot(dados_alunos, positions=[2], labels=["ALUNOS"])

# APRESENTAÇÃO DO BOXPLOT#
plot.title("ESCOLA")
plot.ylabel("NOTAS")
plot.show()

"SEM OUTLIER"
dados_alunas.sort()
dados_alunas.pop()
boxplot_alunas1 = plot.boxplot(dados_alunas, positions=[1], labels=["ALUNAS"])
boxplot_alunos1 = plot.boxplot(dados_alunos, positions=[2], labels=["ALUNOS"])
plot.title("ESCOLA")
plot.ylabel("NOTAS")
plot.show()
