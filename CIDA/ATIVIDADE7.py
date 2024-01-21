# A PARTIR DO ARQUIVO 'DADOS_POP.CSV', IMPLEMENTAR O ARQUIVO EM PYTHON QUE APRESENTE  BOXPLOT (UM DO BRASIL E OUTRO DA REIGÃO SUDESTE). #
# DEPOIS APRESENTE AS CIDADES MENOS A POPULAÇÃO NORDESTE

# CARREGAMENTO DAS BIBLIOTECAS #

import matplotlib.pyplot as plot
import pandas as pd


# ENTRADA DE DADOS #
arquivo = 'C:\\Users\\yurih\\Documents\\Projetos_Software\\dados_pop.csv'
dados_originais = pd.read_csv(arquivo, header=1)
dados = dados_originais.to_dict("list")     # CONVERTE O DATAFRAME PARA DICIONARIO #


# PROCESSAMENTO DOS DADOS #

"SUDESTE"
popula_suldest = []                         # LISTA VAZIA #
tamanho_dados = len(dados["Município"])
contador = range(tamanho_dados)
for i in contador:                          # PERCORRE TODAS AS CIDADES #
    if ((dados["Estado"][i] == "RJ") or
            (dados["Estado"][i] == "SP") or
            (dados["Estado"][i] == "ES") or
            (dados["Estado"][i] == "MG")):
        popula_suldest.append(dados["População"][i])


"NORDESTE"
tupla_nordest = list(zip())                 # LISTA DE TUPLA VAZIA #
estados_nordest = ["BA","SE","AL","RN","CE","MA","PE","PI","PB"]
for i in contador:                          # PERCORRE TODAS AS CIDADES #
    if (dados["Estado"][i] in estados_nordest):
        t = (dados["População"][i], dados["Município"][i]) # SE FOR MUNICIPIO E POPULAÇÃO VAI SER EM ORDEM ALFABETICA, PARA POPULAÇÃO E MUNICIPIO FICA ORDEM CRESCENTE NUMEROS #
        tupla_nordest.append(t)             # COLOCA A TUPLA NA LISTA FINAL #
tupla_nordest.sort()
print(tupla_nordest)
print(tupla_nordest[0], tupla_nordest[1], tupla_nordest[2])


# APRESENTAÇÃO DOS DADOS #
diagrama = plot.boxplot(dados["População"], positions=[1], labels=["Sudeste!!!"])
diagrama = plot.boxplot(popula_suldest, positions=[2], labels=["Sudeste!!!"])
plot.title("COMPARAÇÃO ENTRE AS DISTRIBUIÇÕES DO BRASIL E DO SUDESTE")
plot.ylabel("POPULAÇÃO")
plot.show()
