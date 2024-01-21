# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd


# ENTRADA DE DADOS #
#dados = {"RAMO":["AUTO", "SAUDE", "INCENDIO", "VIDA", "RISCOS DIVERSOS", "HABITAÇÃO", "TRANSPORTE", "ACIDENTES PESSOAIS", "OBRIGATORIO VEICULO", "RISCO DE ENGENHARIA", "RESPONSABILIDADE CIVIL", "OUTROS"], #
#         "%":[33.6,14.0,12.9,12.2,5.5,5.3,3.1,2.9,1.7,1.0,0.9,6.9]} # DICIONARIO #
arquivo = 'C:\\Users\\yurih\Documents\\dados_seguros.csv'
dados_originais = pd.read_csv(arquivo, header=1) # LE O ARQUIVO A PARTIR DA LINHA 1 #
dados = dados_originais.to_dict("list") # CONVERTE O DATAFRAME PARA DICT

# PROCESSAMENTO DOS DADOS #
Q1 = np.percentile(dados["Fatia de Mercado"],25, method="averaged_inverted_cdf")
Q3 = np.percentile(dados["Fatia de Mercado"],75, method="averaged_inverted_cdf")
DQ = Q3 - Q1
lim_inf = np.fmax(min(dados["Fatia de Mercado"]), Q1 - 1.5 - DQ)
lim_sup = np.fmin(max(dados["Fatia de Mercado"]), Q3 - 1.5 + DQ)


# IDENTIFICAÇÃO DO OUTLIER
tamanho_total = len(dados["Fatia de Mercado"])         # FAZ UMA CONTAGEM DE 0 ATE O TAMANHO #
contador = range(tamanho_total)         # FAZ UMA CONTAGEM DE 0 ATE O TAMANHO #

for i in contador: # LOOP QUE PERCOBRRE  CADA ELEMENTO DA LISTA #
    if ((dados["Fatia de Mercado"][i] > lim_sup) or (dados["Fatia de Mercado"][i] < lim_inf)):
        print("OUTLIER", dados["Ramo"][i], " - ", dados["Fatia de Mercado"][i])
    else:
        print("VALORES NÃO OUTLIER DE i =", i)

# APRESENTAÇÃO DOS DADOS #
print("LIMITE INFERIOR = ", lim_inf)
print("LIMITE INFERIOR = ", lim_sup)
print(dados)


# APRESENTAÇÃO E CONFIGURAÇÃO DO BOXPLOT #
diagrama = plot.boxplot(dados["Fatia de Mercado"])
plot.title("BOXPLOT DOS DOADOS DE SEGURO!!!!!")
plot.ylabel("FATIA DE MERCADO (%)")
plot.show()