# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#   LISTA DE EXERCICIOS 04 #

# 1 #
print("1")
#   CARREGAMENTO DOS DADOS #
arquivo = "C:\\Users\\yurih\\Documents\\Programações\\CIDA\\dados_imposto_empresa.csv"
dados_originais = pd.read_csv(arquivo, header=2)
dados_dict = dados_originais.to_dict('list')
print(dados_dict)
classe = round(1+3.32*np.log10(len(dados_dict['Imposto (%)'])))
plt.hist(dados_dict['Imposto (%)'], bins=classe, ec='white')
plt.show()