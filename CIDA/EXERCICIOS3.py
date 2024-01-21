# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

print("==========================================================================================================================================================================================================================================================================================")
'=============================================================================================='
# ATIVIDADE 1 #
'=============================================================================================='
print("ATIVIDADE 1")

# ENTRADA DE DADOS #
dados_pecas = [53.0,70.2,84.3,69.5,77.8,87.5,53.4,82.5,67.3,54.1,70.5,71.4,95.4,51.1,
              74.4,55.7,63.5,85.8,53.5,64.3,82.7,78.5,55.7,69.1,72.3,59.5,55.3,73.0,52.4,50.7]


# PROCESSAMENTO DE DADOS #
Q1 = np.percentile(dados_pecas, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados_pecas, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados_pecas, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1

limite_inferior = np.fmax(50.7, Q1 - 2.5*DQ)
limite_superior = np.fmin(53.0, Q3 + 2.5*DQ)


# APRESENTAÇÃO DOS DADOS #
print("q1 é = ", Q1)
print("q2 é = ", Q2)
print("q3 é = ", Q3)
print("Limite_Inferior=", limite_inferior)
print("Limite_Inferior=", limite_superior)


# CRIÇÃO DO BOXPLOT #
diagrama = plot.boxplot(dados_pecas)
plot.title("PEÇAS DE ALUMINIO")
plot.xlabel("PEÇAS")
plot.ylabel("VALOR DE DUREZA")
plot.show()

'=========================================================='
'=========================================================='
# ATIVIDADE 2 #
'=============================================================================================='
print("==========================================================================================================================================================================================================================================================================================")
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

'=============================================================================================='
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

'=============================================================================================='
# ATIVIDADE 4 #
'=============================================================================================='
print("==========================================================================================================================================================================================================================================================================================")
print("ATIVIDADE 4")
# ENTRADA DE DADOS CSV #
arquivo = 'C:\\Users\\yurih\\Documents\\Programações\\CIDA\\dados_empresa.csv'
dados_originais = pd.read_csv(arquivo, header=0)
dados_empresa = dados_originais.to_dict("list")
print(dados_empresa)

print("A")

# PROCESSAMENTO DOS DADOS #
Bacharel = []
Mestre = []
Doutorado = []
contador = range(len(dados_empresa['Educacao']))
for i in contador:
    if ('Bacharel' in dados_empresa['Educacao'][i]):
        Bacharel.append(dados_empresa['Salario'][i])
    if ('Mestrado' in dados_empresa['Educacao'][i]):
        Mestre.append(dados_empresa['Salario'][i])
    if ('Doutorado' in dados_empresa['Educacao'][i]):
        Doutorado.append(dados_empresa['Salario'][i])

# APRESENTAÇÃO DOS DADOS #
diagrama = plot.boxplot(Bacharel, labels= ["BACHAREL"], positions= [1] )
diagrama1 = plot.boxplot(Mestre, labels= ["MESTRE"], positions= [2] )
diagrama2 = plot.boxplot(Doutorado, labels= ["DOUTOR"], positions= [3] )
plot.title("SALARIOS E EDUCAÇÃO")
plot.ylabel("SALARIOS")
plot.show()

print("B")

# PROCESSAMENTO DOS DADOS #
gestao = []
nao_gestao = []
contador = range(len(dados_empresa['Gestão']))
for i in contador:
    if ('Sim' in dados_empresa['Gestão'][i]):
        gestao.append(dados_empresa['Salario'][i])
    if ('Nao' in dados_empresa['Gestão'][i]):
        nao_gestao.append(dados_empresa['Salario'][i])

# APRESENTAÇÃO DOS DADOS #
diagrama = plot.boxplot(gestao, labels= ["GESTOR"], positions= [1] )
diagrama1 = plot.boxplot(nao_gestao, labels= ["NÂO GESTOR"], positions= [2] )
plot.title("SALARIOS E GESTÂO")
plot.ylabel("SALARIOS")
plot.show()


'=============================================================================================='
# ATIVIDADE 5 #
'=============================================================================================='
print("==========================================================================================================================================================================================================================================================================================")
print("ATIVIDADE 5")

# ENTRADA DE DADOS CSV #
arquivo = 'C:\\Users\\yurih\\Documents\\Programações\\CIDA\\dados_treinamento.csv'
dados_originais = pd.read_csv(arquivo, header=1)
dados_funcionario = dados_originais.to_dict("list")
print(dados_funcionario)

# PROCESSAMENTO DOS DADOS Exercicio A)#
mediana_direito = np.median(dados_funcionario['Direito'])
mediana_politica = np.median(dados_funcionario['Politica'])
mediana_estatistica = np.median(dados_funcionario['Estatistica'])

media_direito = np.mean(dados_funcionario['Direito'])
media_politica = np.mean(dados_funcionario['Politica'])
media_estatistica = np.mean(dados_funcionario['Estatistica'])

desvio_direito = np.std(dados_funcionario['Direito'])
desvio_politico = np.std(dados_funcionario['Politica'])
desvio_estatistica = np.std(dados_funcionario['Estatistica'])

media_notas = [] # Exercicio B)
media_pessoal = []
media_tecnica = []
media_vendas = []
qtd_notas = range(len(dados_funcionario['Direito']))
for i in qtd_notas:
    media = (dados_funcionario['Direito'][i] + dados_funcionario['Politica'][i] + dados_funcionario['Estatistica'][i]) / 3
    media_notas.append(media)
    if dados_funcionario['Secao'][i] == 'Pessoal':
        media_pessoal.append(media)
    if dados_funcionario['Secao'][i] == 'Tecnica':
        media_pessoal.append(media)
    if dados_funcionario['Secao'][i] == 'Vendas':
        media_pessoal.append(media)

# Exercicio D)
media_pessoal = []
media_tecnica = []
media_vendas = []
qtd_notas = range(len(dados_funcionario['Direito']))
for i in qtd_notas:
    media = (dados_funcionario['Direito'][i] + dados_funcionario['Politica'][i] + dados_funcionario['Estatistica'][i]) / 3
    media_notas.append(media)
    if dados_funcionario['Secao'][i] == 'Pessoal':
        media_pessoal.append(media)
    if dados_funcionario['Secao'][i] == 'Tecnica':
        media_tecnica.append(media)
    if dados_funcionario['Secao'][i] == 'Vendas':
        media_vendas.append(media)

# Exibição dos resultados B e C)
diagrama_direito = plot.boxplot(dados_funcionario['Direito'], positions=[1], labels=["Direito!"])
diagrama_politica = plot.boxplot(dados_funcionario['Politica'], positions=[2], labels=["Politica"])
diagrama_estatistica = plot.boxplot(dados_funcionario['Estatistica'], positions=[3], labels=["Estatistica"])
diagrama_medias = plot.boxplot(media_notas, positions=[4], labels=["Média"]) # Exbição C)
plot.show()

# Exibição dos resultados D)
diagrama_pessoal = plot.boxplot(media_pessoal, positions=[1], labels=["Pessoal"])
diagrama_tecnica = plot.boxplot(media_tecnica, positions=[2], labels=["Tecnica"])
diagrama_vendas = plot.boxplot(media_vendas, positions=[3], labels=["Vendas"])
diagrama_medias = plot.boxplot(media_notas, positions=[4], labels=["Média Turma"])
plot.title("Seções e suas médias")
plot.ylabel("Médias")
plot.show()