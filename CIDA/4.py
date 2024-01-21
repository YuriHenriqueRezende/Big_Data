# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

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