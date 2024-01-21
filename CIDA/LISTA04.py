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
print('===============================================================================================================================================================================')
# 2 #
print("2")
# CARREGAMENTO DOS DADOS #
hrsSemDormir = [8,8,12,12,16,16,20,20,24,24]
erros = [6,8,6,12,8,14,12,14,12,16]
m = [hrsSemDormir,erros]
poh = np.corrcoef(m)
print(poh)
print('===============================================================================================================================================================================')
# 3 #
print("3")
# CARREGAMENTO DOS DADOS #
unidades = [40,60,80,100,120,140,160]
rendimento = [15.9,18.8,21.6,25.2,28.7,30.4,30.7]
m = [unidades,rendimento]
roh = np.corrcoef(m)
print(roh)
plt.scatter(unidades,rendimento)
plt.show()
print('===============================================================================================================================================================================')
# 4 #
print("4")
# CARREGAMENTO DOS DADOS #
dados = pd.read_csv("C:\\Users\\yurih\\Documents\\Programações\\CIDA\\Ex4.csv")
lista = dados.to_dict('list')
print(lista)
temp = lista['Temperatura']
prod = lista['Produtividade']
plt.scatter(prod,temp)
plt.show()
m = [temp,prod]
print(np.corrcoef(m))