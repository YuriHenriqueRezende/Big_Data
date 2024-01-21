import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dados = pd.read_csv("F:\\eu\\DataCience\\Lista04\\Ex4.csv")
lista = dados.to_dict('list')
print(lista)
temp = lista['Temperatura']
prod = lista['Produtividade']
plt.scatter(prod,temp)
plt.show()
m = [temp,prod]
print(np.corrcoef(m))