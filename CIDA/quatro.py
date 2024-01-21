# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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