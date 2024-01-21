# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

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